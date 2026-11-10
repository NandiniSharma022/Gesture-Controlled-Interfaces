
import cv2
import mediapipe as mp

import pyautogui
from gesture_logic import get_screen_coordinates, calculate_distance

# Step 1: Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils

hands = mp_hands.Hands(
    max_num_hands=1,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7
)

# Step 2: Start camera
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Camera not found!")
    hands.close()
    exit()

print("Hand tracking started!")
previous_mouse_position = None
pyautogui.FAILSAFE = True

pinch_was_active = False

# Step 3: Capture video continuously
while True:

    success, frame = cap.read()

    if not success:
        print("Unable to capture video")
        break

    # Mirror the camera
    frame = cv2.flip(frame, 1)

    # Convert BGR to RGB
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Step 4: Detect hands
    results = hands.process(rgb_frame)

    # Step 5: Detect raised fingers
    if results.multi_hand_landmarks:

        for hand_landmarks in results.multi_hand_landmarks:

            landmarks = hand_landmarks.landmark

            # Step 9: Detect index and middle finger
            index_up = landmarks[8].y < landmarks[6].y
            middle_up = landmarks[12].y < landmarks[10].y

            # Step 10: Activate mouse movement
            if index_up and not middle_up:

                index_tip = landmarks[8]

                # Convert camera position to screen position
                current_position = get_screen_coordinates(index_tip)

                # Move mouse cursor
                pyautogui.moveTo(
                    current_position[0],
                    current_position[1]
                )

                cv2.putText(
                    frame,
                    "MOUSE CONTROL ACTIVE",
                    (30, 110),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.8,
                    (0, 255, 0),
                    2
                )

            # Finger tip and joint positions
            finger_tips = [8, 12, 16, 20]
            finger_joints = [6, 10, 14, 18]

            finger_count = 0

            # Check which fingers are raised
            for tip, joint in zip(finger_tips, finger_joints):

                if landmarks[tip].y < landmarks[joint].y:
                    finger_count += 1

            # Display finger count
            cv2.putText(
                frame,
                f"Fingers: {finger_count}",
                (30, 60),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (0, 255, 0),
                2
            )

            # Step 12: Detect pinch gesture

            thumb_tip = landmarks[4]
            index_tip = landmarks[8]

            pinch_distance = calculate_distance(
                thumb_tip,
                index_tip
            )

            # Step 13: Perform mouse click
            if pinch_distance < 0.04:

                if not pinch_was_active:
                    pyautogui.click()
                    pinch_was_active = True
                    print("Mouse Clicked!")

            else:
                pinch_was_active = False

            
            # Step 14: Gesture Controlled Scrolling

            # Check if index and middle fingers are raised
            # and ring and pinky fingers are lowered

            if (
                landmarks[8].y < landmarks[6].y and
                landmarks[12].y < landmarks[10].y and
                landmarks[16].y > landmarks[14].y and
                landmarks[20].y > landmarks[18].y
            ):

                # Calculate vertical position of two fingertips
                scroll_position = (
                    landmarks[8].y + landmarks[12].y
                ) / 2

                # Scroll down
                if scroll_position > 0.35:
                    pyautogui.scroll(-2)

                # Scroll up
                elif scroll_position < 0.25:
                    pyautogui.scroll(2)
            # Draw hand landmarks
            mp_draw.draw_landmarks(
                frame,
                hand_landmarks,
                mp_hands.HAND_CONNECTIONS
            )

    # Step 6: Display output
    cv2.imshow("Gesture Controlled Interface", frame)

    # Press Q to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Step 7: Release resources
cap.release()
hands.close()
cv2.destroyAllWindows()

import math
import pyautogui

# Get screen dimensions
screen_width, screen_height = pyautogui.size()

# Calculate distance between two points
def calculate_distance(point1, point2):

    x1, y1 = point1.x, point1.y
    x2, y2 = point2.x, point2.y

    distance = math.sqrt(
        (x2-x1)**2 + (y2-y1)**2
    )

    return distance


# Convert camera coordinates into screen coordinates
def get_screen_coordinates(landmark):

    x = int(landmark.x * screen_width)
    y = int(landmark.y * screen_height)

    return x, y
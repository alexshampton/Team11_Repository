import cv2
import numpy as np

# Load the image
image = cv2.imread('dstest2.jpeg')

# Convert the image to HSV (hue, saturation, value) space for better color detection
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# Define the red color range in HSV
lower_red1 = np.array([0, 70, 50])
upper_red1 = np.array([10, 255, 255])
lower_red2 = np.array([170, 70, 50])
upper_red2 = np.array([180, 255, 255])

# Threshold the image to get only red colors
mask1 = cv2.inRange(hsv, lower_red1, upper_red1)
mask2 = cv2.inRange(hsv, lower_red2, upper_red2)
mask = mask1 + mask2

# Use a GaussianBlur to smooth the image and reduce noise
blurred = cv2.GaussianBlur(mask, (9, 9), 0)

# Detect circles using HoughCircles
circles = cv2.HoughCircles(blurred, cv2.HOUGH_GRADIENT, dp=1.2, minDist=50,
                           param1=100, param2=30, minRadius=10, maxRadius=200)

# If circles are detected, process them
if circles is not None:
    circles = np.round(circles[0, :]).astype("int")
    for (x, y, r) in circles:
        # Draw the circle in the output image (you can use this to verify detection)
        cv2.circle(image, (x, y), r, (0, 255, 0), 2)

        # Draw the center of the circle
        # cv2.circle(image, (x, y), 2, (255, 0, 0), 3)

    print(f"Detected {len(circles)} circle(s).")

    # Show the output image with the detected circle
    cv2.imshow("Detected Circle", image)
    cv2.waitKey(0)
else:
    print("No red circle detected.")

# Release resources
cv2.destroyAllWindows()

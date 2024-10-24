import cv2
import numpy as np
import os

image_path = 'dstest2.jpeg'
# Extract the file name without extension
file_name = os.path.splitext(os.path.basename(image_path))[0]

# Load the image
image = cv2.imread(image_path)

# Convert the image to HSV (hue, saturation, value) space for better color detection
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# Define the red color range in HSV
lower_red1 = np.array([0, 100, 100])
upper_red1 = np.array([10, 255, 255])
lower_red2 = np.array([170, 100, 100])
upper_red2 = np.array([180, 255, 255])

# Threshold the image to get only red colors
mask1 = cv2.inRange(hsv, lower_red1, upper_red1)
mask2 = cv2.inRange(hsv, lower_red2, upper_red2)
mask = mask1 + mask2

blurred = cv2.GaussianBlur(mask, (9, 9), 0)

# Find contours in the mask (detected red areas)
contours, _ = cv2.findContours(blurred, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Process each contour
for contour in contours:
    # Approximate the contour to reduce the number of points
    approx = cv2.approxPolyDP(contour, 0.04 * cv2.arcLength(contour, True), True)

    # Use minEnclosingCircle to approximate the contour as a circle
    (x, y), radius = cv2.minEnclosingCircle(contour)

    # Calculate the circularity of the contour (if it's close to 1, it's a circle)
    area_contour = cv2.contourArea(contour)
    if radius > 5 and area_contour > 0:  # Filter out very small contours
        circularity = (4 * np.pi * area_contour) / (cv2.arcLength(contour, True) ** 2)
        
        # Only consider filled circles (circularity close to 1)
        if 0.8 < circularity < 1.2:
            # Draw the filled red circle (optional, here just to visualize detection)
            cv2.circle(image, (int(x), int(y)), int(radius), (0, 255, 0), 2)  # Green outline
            # cv2.circle(image, (int(x), int(y)), 2, (255, 0, 0), -1)  # Blue center dot

print(f"Detected {len(contours)} possible filled red circles.")

# Save the output image with the detected filled red circles
output_path = f'{file_name}_detected_filled_red_circles.png'
cv2.imwrite(output_path, image)
print(f"Image saved as {output_path}")

# Optionally, display the image (you can remove this if you don't want to display it)
cv2.imshow("Detected Filled Red Circles", image)

cv2.waitKey(0)

# Release resources
cv2.destroyAllWindows()
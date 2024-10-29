import cv2
import numpy as np

def capture_colored_screen(image_path, output_path="cropped_screen.jpg"):
    # Load the image
    image = cv2.imread(image_path)
    original_image = image.copy()
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Apply a high threshold to isolate the bright and colorful parts
    _, bright_thresh = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY)
    
    # Use morphology to close small gaps and make the screen area more solid
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
    bright_thresh = cv2.morphologyEx(bright_thresh, cv2.MORPH_CLOSE, kernel)
    
    # Find contours in the thresholded image
    contours, _ = cv2.findContours(bright_thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    if contours:
        # Find the largest contour by area, which should ideally be the screen region
        largest_contour = max(contours, key=cv2.contourArea)
        
        # Get the bounding box for the largest contour
        x, y, w, h = cv2.boundingRect(largest_contour)
        
        # Crop the region
        cropped_screen = original_image[y:y+h, x:x+w]
        
        # Save the cropped region
        cv2.imwrite(output_path, cropped_screen)
        print(f"Cropped screen saved as {output_path}")
        return cropped_screen
    else:
        print("No bright region detected.")
        return None

# Example usage
capture_colored_screen("detected/frame377.png")

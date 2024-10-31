import cv2

# Open the camera (1 = server camera, 0 = laptop camera)
cap = cv2.VideoCapture(1)

# Check if the camera opened successfully
if not cap.isOpened():
    print("Error: Could not open video source.")
    exit()

# Check if the camera supports exposure control
if cap.get(cv2.CAP_PROP_AUTO_EXPOSURE):
    # Set auto-exposure to manual mode
    cap.set(cv2.CAP_PROP_AUTO_EXPOSURE, 0)

# Set exposure time (in milliseconds)
# cap.set(cv2.CAP_PROP_EXPOSURE, -5)  # Adjust the value as needed

# Get the default camera's frame width and height
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))

# Define the codec and create a VideoWriter object to save the video
# Specify the path where the video will be saved using one of these three options:

# Option 1: Escape the backslashes
output_path = r'C:\Users\ramen\OneDrive\Documents\WSU Dayton\Fall 2024\(2) Team Projects 2\recorded_videos'
# print(output_path)

out = cv2.VideoWriter("output.mp4", cv2.VideoWriter_fourcc(*'mp4v'), 30, (frame_width, frame_height)) 
# Capture video frame by frame
while True:
    # Read the current frame
    ret, frame = cap.read()

    if not ret:
        print("Error: Failed to capture image.")
        break

    # Write the frame to the output file
    out.write(frame)

    # Save the frame in the output_path
    # cv2.imwrite(output_path, out)

    # Display the frame in a window
    cv2.imshow('Webcam Video', frame)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the capture and video writer objects
cap.release()
out.release()

# Close all OpenCV windows
cv2.destroyAllWindows()

# print(f"Video saved at: {output_path}")
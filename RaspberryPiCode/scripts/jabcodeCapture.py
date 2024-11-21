import cv2
import os
import time

# Open a connection to the camera

start_time = time.time()

cap = cv2.VideoCapture(1)  # Use 0 for the default camera
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 3840) 
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 2160)
# Create an array to store frames
frames = []

end_time = time.time()

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Append each frame to the frames array
    frames.append(frame)
    
    # Display the frame
    cv2.imshow('Preview', frame)

    # Exit on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera
cap.release()
cv2.destroyAllWindows()

duration = end_time - start_time
print(f"It takes {duration} seconds to load up the camera")

# Create a directory to save the frames
output_dir = 'camera_frames'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Save frames to the directory
for i, frame in enumerate(frames):
    frame_filename = os.path.join(output_dir, f'frame_{i:04d}.jpg')
    cv2.imwrite(frame_filename, frame)

print(f'Saved {len(frames)} frames to the directory: {output_dir}')

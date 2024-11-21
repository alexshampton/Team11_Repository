from picamera2 import Picamera2
import cv2
import os
import time
import numpy as np

# Initialize Picamera2
picam2 = Picamera2()
camera_config = picam2.create_still_configuration({"size": (3840, 2160)})
picam2.configure(camera_config)

start_time = time.time()

# Start the camera
picam2.start()
time.sleep(2)  # Allow the camera to warm up

end_time = time.time()

frames = []

try:
    while True:
        # Capture a frame
        frame = picam2.capture_array()
        frames.append(frame)

        # Convert the frame to BGR format for OpenCV compatibility
        frame_bgr = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

        # Display the frame
        cv2.imshow('Preview', frame_bgr)

        # Exit on 'q' key press
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
except KeyboardInterrupt:
    print("Camera preview interrupted.")

# Stop the camera
picam2.stop()
cv2.destroyAllWindows()

# Print the time it took to load the camera
duration = end_time - start_time
print(f"It takes {duration} seconds to load up the camera")

# Create a directory to save the frames
output_dir = 'camera_frames'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Save frames to the directory
for i, frame in enumerate(frames):
    frame_bgr = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
    frame_filename = os.path.join(output_dir, f'frame_{i:04d}.jpg')
    cv2.imwrite(frame_filename, frame_bgr)

print(f'Saved {len(frames)} frames to the directory: {output_dir}')

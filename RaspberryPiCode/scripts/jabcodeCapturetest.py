import os
import subprocess
import time

# Create a directory to save the frames
output_dir = 'camera_frames'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

start_time = time.time()

try:
    for i in range(10):  # Capture 10 frames as an example
        frame_filename = os.path.join(output_dir, f'frame_{i:04d}.jpg')

        # Run the libcamera-jpeg command to capture a frame
        subprocess.run([
            'libcamera-jpeg',
            '-o', frame_filename,        # Output file
            '--width', '3840',           # Set width
            '--height', '2160',          # Set height
            '--quality', '90',           # JPEG quality (adjust as needed)
            '-n'                         # Suppress preview window
        ])

        print(f"Captured: {frame_filename}")
        time.sleep(1)  # Wait 1 second between captures

except Exception as e:
    print(f"An error occurred: {e}")

end_time = time.time()
duration = end_time - start_time
print(f"Captured frames in {duration} seconds")
print(f"Saved frames to: {output_dir}")

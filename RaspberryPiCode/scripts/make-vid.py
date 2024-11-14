# importing libraries
import os
import cv2
from PIL import Image
import ffmpeg

# TODO update these variables
num_dupe_frames = 0  # number for num of time to duplicate each frame
path = "frames"  # where all the images are
final_file_name = "incrementing"  # output file

mean_height = 0
mean_width = 0

num_of_images = len(os.listdir(path))

print(os.getcwd())
for file in os.listdir(path):
    im = Image.open(os.path.join(path, file))
    width, height = im.size
    mean_width += width
    mean_height += height

# forces an average size for each image so all images make it into the video
mean_width = int(mean_width / num_of_images)
mean_height = int(mean_height / num_of_images)

# Video Generating function
in_name = final_file_name + ".avi"
out_name = final_file_name + ".mp4"

images = [
    img
    for img in os.listdir(path)
    if img.endswith(".jpg") or img.endswith(".jpeg") or img.endswith("png")
]

images = (num_dupe_frames + 1) * images
images.sort()
frame = cv2.imread(os.path.join(path, images[0]))

# setting the frame width, height width
# the width, height of first image
height, width, layers = frame.shape

video = cv2.VideoWriter(in_name, 0, 60, (width, height))

# Appending the images to the video one by one
for image in images:
    video.write(cv2.imread(os.path.join(path, image)))

# Deallocating memories taken for window creation
cv2.destroyAllWindows()
video.release()

ffmpeg.input(in_name).output(out_name).run()
os.remove(in_name)

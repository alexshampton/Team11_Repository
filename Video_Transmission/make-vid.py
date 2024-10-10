# importing libraries
import os
import cv2
from PIL import Image
import ffmpeg

# Checking the current directory path
print(os.getcwd())

# Folder which contains all the images
# from which video is to be generated
os.chdir("frames")
path = "."

mean_height = 0
mean_width = 0

num_of_images = len(os.listdir("."))
# print(num_of_images)

print(os.getcwd())
for file in os.listdir("."):
    # print(os.path.join(path, file))
    im = Image.open(file)
    width, height = im.size
    mean_width += width
    mean_height += height
    # im.show() # uncomment this for displaying the image

# Finding the mean height and width of all images.
# This is required because the video frame needs
# to be set with same width and height. Otherwise
# images not equal to that width height will not get
# embedded into the video
mean_width = int(mean_width / num_of_images)
mean_height = int(mean_height / num_of_images)

# Video Generating function
image_folder = "frames/"  # make sure to use your folder
fileName = "incrementing"
video_name = fileName + ".avi"
os.chdir("..")

images = [
    img
    for img in os.listdir(image_folder)
    if img.endswith(".jpg") or img.endswith(".jpeg") or img.endswith("png")
]

# Array images should only consider
# the image files ignoring others if any
# print(images)
images.sort()
# print(images)
frame = cv2.imread(os.path.join(image_folder, images[0]))

# setting the frame width, height width
# the width, height of first image
height, width, layers = frame.shape

video = cv2.VideoWriter(video_name, 0, 60, (width, height))

# Appending the images to the video one by one
for image in images:
    video.write(cv2.imread(os.path.join(image_folder, image)))

# Deallocating memories taken for window creation
cv2.destroyAllWindows()
video.release()  # releasing the video generated

in_name = "incrementing.avi"
out_name = "incrementing.mp4"

ffmpeg.input(in_name).output(out_name).run()
os.remove(in_name)

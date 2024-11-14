from ultralytics import YOLO
import os
import shutil

inp = "all-images"
weights = "jabcode.pt"

model = YOLO(weights)  # load model

images = []  # list of all images
for i, file in enumerate(os.listdir(inp)):
    if file.endswith(".jpg") | file.endswith(".png"):
        images.append(inp + "/" + file)

images.sort()

results = model(images)  # run images through model

# detected = []  # all relevant info from detected death star images
# for i, result in enumerate(results):
#     if len(result):
#         detected.append([images[i].split("/")[-1], max(result.boxes.conf), result])
# detected.sort(key=lambda tup: tup[1], reverse=True)

# keep = detected[0:10]  # keep 10 best

# for image in detected:  # store raw and confidence images
#     shutil.copy(inp + "/" + image[0], "detected/raw/" + image[0])
#     image[2].save("detected/conf/" + image[0])

# results = model("path/to/image.jpg")
for result in results:
    # print(result.boxes)  # Print detection boxes
    # result.show()  # Display the annotated image
    result.save_crop(".")
    # result.save(filename="result.jpg")  # Save annotated image

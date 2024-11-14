from ultralytics import YOLO
import os
import shutil

inp = "Assets/all_images"
weights = "Assets/model/ds.pt"

model = YOLO(weights)  # load model

images = []  # list of all images
for i, file in enumerate(os.listdir(inp)):
    if file.endswith(".jpg") | file.endswith(".png"):
        images.append(inp + "/" + file)

results = model(images)  # run images through model

detected = []  # all relevant info from detected death star images
for i, result in enumerate(results):
    if len(result):
        detected.append([images[i].split("/")[-1], max(result.boxes.conf), result])
detected.sort(key=lambda tup: tup[1], reverse=True)

keep = detected#[0:10]  # keep 10 best

for image in keep:  # store raw images
    shutil.copy(inp + "/" + image[0], "Assets/death_star_images/" + image[0])
    # image[2].save("detected/conf/" + image[0])

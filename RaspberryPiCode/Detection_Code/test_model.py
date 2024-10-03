from imageai.Detection.Custom import CustomObjectDetection
import os
import shutil

detector = CustomObjectDetection()
detector.setModelTypeAsYOLOv3()
detector.setModelPath("images/models/yolov3_images_mAP-0.94921_epoch-36.pt")
detector.setJsonPath("images/json/images_yolov3_detection_config.json")
detector.loadModel()

rootdir = "all-images"
for subdir, dirs, files in os.walk(rootdir):
    for i, file in enumerate(files):
        detections = detector.detectObjectsFromImage(
            input_image=os.path.join(subdir, file),
            # output_image_path="detected/" + str(file),
            display_percentage_probability=True,
            display_object_name=False,
            minimum_percentage_probability=48,
        )
        for detection in detections:
            shutil.copy("test-images/" + file, "death_star_images/" + file)
            print(
                file,
                " : ",
                # detection["name"],
                # " : ",
                detection["percentage_probability"],
                # " : ",
                # detection["box_points"],
                # " : image num ",
                # num,
            )

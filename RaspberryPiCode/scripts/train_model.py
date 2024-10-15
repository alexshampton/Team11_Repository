from imageai.Detection.Custom import DetectionModelTrainer

trainer = DetectionModelTrainer()
trainer.setModelTypeAsYOLOv3()
trainer.setDataDirectory(data_directory="images")
trainer.setTrainConfig(
    object_names_array=["death star"],
    num_experiments=200,
    train_from_pretrained_model="images/models/yolov3.pt",
)
trainer.trainModel()

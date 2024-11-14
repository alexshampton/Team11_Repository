from ultralytics import YOLO

# Load a model
model = YOLO("yolo11n.pt")  # load a pretrained model (recommended for training)

# Train the model
results = model.train(
    data="./images/data.yaml", epochs=100, imgsz=640, batch=16, workers=4
)

model.val()

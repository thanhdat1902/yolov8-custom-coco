from ultralytics import YOLO

model = YOLO("yolov8n-pose.pt")  # load an official model

# # Use the model
# model.train(data="yolov8-pose.yaml", epochs=30, batch=4, save_period=10, device=0, workers=4, resume=True)  # train the model
# metrics = model.val()  # evaluate model performance on the validation set


# Load a model
# model = YOLO("yolov8n-pose.pt")  # load a pretrained model (recommended for training)

# Train the model
# results = model.train(data="yolov8-pose.yaml", epochs=100)

results = model("../dataset/test_xworld/020000000004.jpg")  # return a list of Results objects


# results = model("./demo-img/020000001041.jpg")  # return a list of Results objects

for result in results:
    boxes = result.boxes  # Boxes object for bounding box outputs
    masks = result.masks  # Masks object for segmentation masks outputs
    keypoints = result.keypoints  # Keypoints object for pose outputs
    probs = result.probs  # Probs object for classification outputs
    obb = result.obb  # Oriented boxes object for OBB outputs
    result.show()  # display to screen
    result.save(filename="result.jpg")  # save to disk
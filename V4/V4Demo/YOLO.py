from ultralytics import YOLO
from PIL import Image


model = YOLO('yolov8n.pt')




path = "HamVeri/ (78).jpg"
im1 = Image.open(path)
sonuc = model.predict(source=im1,save=True)


from ultralytics import YOLO
from PIL import Image


model = YOLO('yolov8n.pt')


im1 = Image.open("HamVeri/ (95).jpg")
sonuc = model.predict(source=im1,save=True)


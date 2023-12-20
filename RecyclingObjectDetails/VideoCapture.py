from ultralytics import YOLO
import cv2
import time

cap = cv2.VideoCapture(0)



model = YOLO('yolov8n.pt')
while True:
    ret ,img = cap.read()
    img1 = model.predict(source=img, save=True)
    fps = cap.get(cv2.CAP_PROP_FPS)
    cv2.imshow("image", img)
    if cv2.waitKey(50) & 0xFF == ord('x'):
     break

cap.release()
cv2.destroyAllWindows()
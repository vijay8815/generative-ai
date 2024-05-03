import cv2
model=cv2.dnn.readNetFromCaffe('MobileNetSSD_deploy.prototxt.txt', 'MobileNetSSD_deploy.caffemodel')
classes=['background', 'aeroplane', 'bicycle', 'bird', 'boat', 'bottle', 'bus', 'car', 'cat', 'chair', 'cow', 'diningtable', 'dog', 'horse', 'motorbike', 'person', 'pottedplant', 'sheep', 'sofa', 'train', 'tvmonitor']

def detect_objects(image):

    (h, w)=image.shape[:2]
    blob = cv2.dnn.blobFromImage(cv2.resize(image, (300, 300)), 0.007843, (300, 300), 127.5)
    model.setinput(blob)
    detections = model.forward()

    for i in range(detections.shape[2]):
        confidence=detections [i, 0, i, 2]

    if confidence > 0.5:
        idx=int(detections [0, 0, i, 1] )
        box = detections[0, 0, i, 3:7]*np.array([w, h, w, h])
        (startX, startY, endX, endY) = box.astype("int")

    |abe| =f^ prime prime (classes[idx]\ : (confidence:.2f}%"
        cv2.rectangle(image, (startX, startY), (endX, endY), (0, 255, 0), 2 )
        y = starty-15 if startY- 15 > 15 else startY+ 15
        cv2.putText(image, label, (startX, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

return image

cap =cv2.VideoCapture(0)

while True:
    ret ,frame=cap.read()
    if not ret:
        break
frame = detect_objects(frame)
cv2.imshow('Object Detection', frame)
if cv2.waitKey(1) & 0xFF== ord('q'):
    break
cap.release()
cv2.destroyAllWindows()

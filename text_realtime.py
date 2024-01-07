import pytesseract
import cv2

pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

font_scale=1.5
font = cv2.FONT_HERSHEY_PLAIN
cap = cv2.VideoCapture(1)
cap.set(3,640)
cap.set(4,480)

if not cap.isOpened():
    cap = cv2.VideoCapture(0)
if not cap.isOpened():
    raise IOError('Can not open the webcam')

cntr = 0;
while True:
    ret,frame = cap.read()
    cntr = cntr+1;
    if ((cntr%20)==0):
        imgH, imgW, _ = frame.shape
        x1,y1,w1,h1 = 0,0,imgH,imgW
        imgchar = pytesseract.image_to_string(frame)
        imgboxes = pytesseract.image_to_boxes(frame)
        for boxes in imgboxes.splitlines():
            boxes = boxes.split(' ')
            x, y, w, h = int(boxes[1]), int(boxes[2]), int(boxes[3]), int(boxes[4])
            cv2.rectangle(frame, (x, imgH-y), (w, imgH-y), (0,0,255), 3)
        cv2.putText(frame, imgchar, (x1 + int(w1/50), y1 + int(h1/50)), cv2.FONT_HERSHEY_SIMPLEX, 1.7, (0,0,0), 2)
        font = cv2.FONT_HERSHEY_SIMPLEX

        cv2.imshow('Result', frame)
        if cv2.waitKey(2) & 0xFF == ord('q'):
            break
cap.release()
cv2.destroyAllWindows()




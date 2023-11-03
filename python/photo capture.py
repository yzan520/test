import cv2
import time

cap = cv2.VideoCapture(2)
ret, frame = cap.read()
if ret:
    time.sleep(5)
    cv2.imshow('show', frame)
    cv2.imwrite("screenshot.jpg", frame)
cap.release()
cv2.destroyAllWindows()
import cv2
import matplotlib.pyplot as plt

# 打开视频文件
video = cv2.VideoCapture("./videos/video2.avi")
num = 1080
save_step = 15
while True:
    ret, frame = video.read()
    if not ret:
        break
    num += 1
    if num % save_step == 0:
        cv2.imwrite("./images/" + str(num) + ".jpg", frame)

import cv2

# 捕获摄像头
cap = cv2.VideoCapture(2)
# 设置视频保存路径
video_path = '/home/zps/test/python/videos/video15.avi'
# 设置视频编码格式
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter(video_path, fourcc, 30.0, (640, 480))

while cap.isOpened():
    ret, frame = cap.read()
    if ret:
        cv2.imshow('video', frame)
        out.write(frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
# 获取帧的属性：宽，高，以及fps
# frame_width = capture.get(cv2.CAP_PROP_FRAME_WIDTH)  # 宽
# frame_height = capture.get(cv2.CAP_PROP_FRAME_HEIGHT)  # 高
# 获取视频帧数
fps = cap.get(cv2.CAP_PROP_FPS)
print(fps)
# 释放资源
cap.release()
out.release()
cv2.destroyAllWindows()

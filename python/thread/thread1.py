import cv2
import threading
import queue

# 创建一个队列用于传递视频帧
frame_queue = queue.Queue(maxsize=10)

# 定义一个全局变量用于控制线程是否退出
exit_flag = False

# 定义一个函数用于读取视频流
def read_camera(camera_id):
    global exit_flag
    cap = cv2.VideoCapture(camera_id)

    while not exit_flag:
        ret, frame = cap.read()
        if not ret:
            break

        # 将帧放入队列
        frame_queue.put(frame)

    cap.release()

# 定义一个函数用于处理图像
def process_frames():
    global exit_flag
    while not exit_flag:
        try:
            frame = frame_queue.get(timeout=1)
            
            # 在这里可以添加处理视频帧的代码
            # 例如，可以对帧进行分析、处理或显示
            
            # 为了示例，这里只是简单地显示帧
            cv2.imshow("Processed Frame", frame)
            cv2.waitKey(1)
        except queue.Empty:
            pass

# 创建两个线程，一个用于读取摄像头0，另一个用于处理图像
thread1 = threading.Thread(target=read_camera, args=(0,))
thread2 = threading.Thread(target=process_frames)

# 启动线程
thread1.start()
thread2.start()

# 主线程等待用户按下'q'键以退出
while True:
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 设置全局退出标志以退出循环
exit_flag = True

# 等待线程结束
thread1.join()
thread2.join()

cv2.destroyAllWindows()

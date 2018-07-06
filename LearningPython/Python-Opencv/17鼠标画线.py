import cv2
import numpy as np

# 创建空帧
frame = np.zeros((800, 800, 3), np.uint8)

# 测量坐标
last_measurement = current_measurement = np.array((2, 1), np.float32)
# 鼠标运动预测
last_prediction = current_predication = np.zeros((2, 1), np.float32)


def mousemove(event, x, y, s, p):
    # 设置全局变量
    global frame, measurements, current_measurement, last_measurement, current_predication, last_prediction
    last_prediction = current_predication
    last_measurement = current_measurement
    current_measurement = np.array([[np.float32(x)], [np.float32(y)]])
    kalman.correct(current_measurement)
    current_predication = kalman.predict()

    # 实际移动起始点
    lmx, lmy = last_measurement[0], last_measurement[1]
    cmx, cmy = current_measurement[0], current_measurement[1]
    # 预测线起止点
    lpx, lpy = last_prediction[0], last_prediction[1]
    cpx, cpy = current_predication[0], current_predication[1]

    # 绘制连线
    cv2.line(frame, (lmx, lmy), (cmx, cmy), (0, 100, 0))  # 绿色
    cv2.line(frame, (lpx, lpy), (cpx, cpy), (0, 0, 200))  # 红色


# 创建窗体
cv2.namedWindow('mouse_detection')
# 注册鼠标事件的回调函数
cv2.setMouseCallback('mouse_detection', mousemove)

# 卡尔曼滤波器
kalman = cv2.KalmanFilter(4, 2)
kalman.measurementMatrix = np.array([[1, 0, 0, 0], [0, 1, 0, 0]], np.float32)
kalman.transitionMatrix = np.array([[1, 0, 1, 0], [0, 1, 0, 1], [0, 0, 1, 0], [0, 0, 0, 1]], np.float32)
kalman.processNoiseCov = np.array([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]], np.float32) * 0.03

while (True):
    cv2.imshow('mouse_detection', frame)
    if cv2.waitKey(30) & 0xFF == 27:
        break

cv2.destroyAllWindows()

#import cv2
# import numpy as np
# 
# # 读取图像
# img = cv2.imread('C.jpg', 0)
# # 构造一个3×3的结构元素
# element = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
# # 膨胀图像 cv2.dilate(图像,元素结构)
# dilate = cv2.dilate(img, element)
# # 腐蚀图像 cv2.erode(图像,元素结构)
# erode = cv2.erode(img, element)
# 
# # 将两幅图像相减获得边，第一个参数是膨胀后的图像，第二个参数是腐蚀后的图像
# result = cv2.absdiff(dilate, erode)
# 
# # 上面得到的结果是灰度图，cv2.threshold将其二值化以便更清楚的观察结果
# # cv2.threshold(src , thresh, maxval, type[, dst])  返回retval、dst
# # cv2.threshold(图像, 阈值  , 最大值, 阈值类型)     返回值类型、返回处理后图像
# # 阈值类型：THRESH_BINARY、THRESH_BINARY_INV、THRESH_TRUNC、THRESH_TOZERO、THRESH_TOZERO_INV
# retval, result = cv2.threshold(result, 40, 255, cv2.THRESH_BINARY)
# 
# # 反色，即对二值图每个像素取反
# result = cv2.bitwise_not(result)
# # 显示图
# cv2.imshow("origin", img)  # 原图
# cv2.imshow("result", result) # 边缘检测图
# 
# cv2.waitKey(0)
# cv2.destroyAllWindows()

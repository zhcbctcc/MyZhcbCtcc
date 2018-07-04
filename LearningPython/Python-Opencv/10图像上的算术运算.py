# # 10.2图像混合 需要两张宽和高一样的图片
# import cv2
# import numpy as np
#
# img1 = cv2.imread('A.jpg')
# img2 = cv2.imread('B.jpg')
# # print(img1.size)
# # print(img2.size)
# dst = cv2.addWeighted(img2,0.7,img1,0.3,0)
#
# cv2.imshow('dst',dst)
# cv2.waitKey(0)
# cv2.destroyWindow()

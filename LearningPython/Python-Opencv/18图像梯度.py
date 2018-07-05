# 第十个程序：图像梯度
# 
# import cv2
# import numpy as np
# from matplotlib import pyplot as plt
# 
# img = cv2.imread('A.jpg')
# 
# laplacian = cv2.Laplacian(img,cv2.CV_64F)
# 
# sobelx = cv2.Sobel(img,cv2.CV_64F,1,0,ksize=5)
# 
# sobely = cv2.Sobel(img,cv2.CV_64F,0,1,ksize=5)
# 
# plt.subplot(2,2,1),plt.imshow(img,cmap='gray')
# plt.title('Original'),plt.xticks([]),plt.yticks([])
# plt.subplot(2,2,2),plt.imshow(laplacian,cmap='gray')
# 
# plt.show()

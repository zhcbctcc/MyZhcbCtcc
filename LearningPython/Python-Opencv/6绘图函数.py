# #第五个程序：画图
# import numpy as np
# import cv2
# 
# img = np.zeros((512,512,3),np.uint8)
# cv2.line(img,(0,0),(512,512),(255,0,0),10)
# cv2.rectangle(img,(384,0),(510,128),(0,255,0),3)
# cv2.circle(img,(384,0),63,(0,0,255),-1)
# cv2.ellipse(img,(256,256),(100,50),0,0,180,255,-1)
# 
# pts = np.array([[10,5],[20,30],[70,20],[50,10]],np.int32)
# pts = pts.reshape((-1,1,2))
# 
# font = cv2.FONT_HERSHEY_SIMPLEX
# cv2.putText(img,'OpenCV',(20,500),font,4,(255,255,255),2)
# 
# 
# winname = 'exampple'
# cv2.namedWindow(winname)
# cv2.imshow(winname,img)
# cv2.waitKey(0)
# cv2.destroyWindow()

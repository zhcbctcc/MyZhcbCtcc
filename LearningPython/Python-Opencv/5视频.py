import numpy as np
# import cv2
#
# cap = cv2.VideoCapture(0)
#
# while(True):
#     ret,frame = cap.read()
#     gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
#     cv2.imshow('frame',gray)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
#
# cap.release()
# cv2.destroyAllWindows()

#第四个程序：从摄像头中捕捉视频，沿水平方向旋转每一帧并保存
# import numpy as np
# import cv2
# 
# cap = cv2.VideoCapture(0)
# 
# fourcc = cv2.VideoWriter_fourcc(*'XVID')
# out = cv2.VideoWriter('output.avi',fourcc,20.0,(640,480))
# 
# while(cap.isOpened()):
#     ret,frame = cap.read()
#     if ret == True:
#         frame = cv2.flip(frame,0)
# 
#         out.write(frame)
# 
#         cv2.imshow('frame',frame)
#         if cv2.waitKey(1) &0xFF == ord('q'):
#             break
#         else:
#             break
# 
# cap.release()
# out.release()
# cv2.destroyAllWindows()

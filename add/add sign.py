import cv2
import numpy as np
import imutils

sign = cv2.imread('G:\python project\\add\cyberpunk.jpg')
bg = cv2.imread('G:\python project\\add\witcher.jpg')

rows, cols, channels = sign.shape
roi = bg[0:rows, 571:cols+571]    # 在背景上取下要放标志的区域

lower_white = np.array([0, 0, 221])
upper_white = np.array([180, 30, 255])
hsv = cv2.cvtColor(sign, cv2.COLOR_BGR2HSV)
mask_white = cv2.inRange(hsv, lower_white, upper_white)
mask_sign = cv2.bitwise_not(mask_white)  # 获取把logo的区域取反 按位运算

sign_inv = cv2.bitwise_not(mask_sign)
res_1 = cv2.bitwise_and(roi, roi, mask=sign_inv)    # 背景
res_2 = cv2.bitwise_and(sign, sign, mask=mask_sign)     # 字

res_final = cv2.add(res_1, res_2)
bg[0:rows, 571:cols+571] = res_final
cv2.imshow('res', imutils.resize(bg, 1000))

cv2.waitKey(0)
cv2.destroyAllWindows()

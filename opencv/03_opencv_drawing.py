import cv2
import numpy as np

# Create a black image
img = np.zeros((512, 512, 3), np.uint8)

# Draw it!



# 加入文字(畫布, 文字內容, 起點, 字體, 大小, 顏色, 粗度)
cv2.putText(img, 'Myname', (350,480), cv2.FONT_HERSHEY_TRIPLEX, 1.0, (0,255,0), 2)

cv2.imwrite('/home/arg/oop-python-nycu/images/drawing.png', img)

# Show the image
cv2.imshow('Drawing', img)
cv2.waitKey(0)
cv2.destroyAllWindows()


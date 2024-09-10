import cv2
import numpy as np

# Create a black image
image_array = np.zeros((512, 512, 3), np.uint8)

# Draw a dog shape on the image
cv2.circle(image_array, (256, 256), 200, (0, 255, 255), -1)
cv2.line(image_array, (245, 256), (245, 300), (0, 0, 255), 4)
cv2.line(image_array, (264, 256), (264, 330), (0, 0, 255), 4)
cv2.circle(image_array, (180, 200), 50, (255, 255, 255), -1)
cv2.circle(image_array, (332, 200), 50, (255, 255, 255), -1)
cv2.circle(image_array, (180, 200), 25, (0, 0, 0), -1)
cv2.circle(image_array, (332, 200), 25, (0, 0, 0), -1)
cv2.ellipse(image_array, (256, 350), (100, 50), 0, 0, 180, (0, 0, 0), -1)
cv2.ellipse(image_array, (256, 350), (70, 40), 0, 0, 180, (255, 255, 255), -1)
cv2.circle(image_array, (180, 200), 20, (255, 0, 0), -1)
cv2.circle(image_array, (332, 200), 20, (255, 0, 0), -1)

# Show the image
cv2.imshow('Dog', image_array)
cv2.waitKey(0)
cv2.destroyAllWindows()


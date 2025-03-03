import cv2
import numpy as np
from matplotlib import pyplot as plt

# Load the Lena testing image
img = cv2.imread('../images/lena.png')

# Apply a 5x5 average filter
f_size = 20
kernel = np.ones((f_size, f_size),np.float32)/ (f_size * f_size)
filtered_img = cv2.filter2D(img, -1, kernel)

# Display the original and filtered images
plt.subplot(121),plt.imshow(img[:,:,::-1])
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(filtered_img[:,:,::-1])
plt.title('Filtered Image'), plt.xticks([]), plt.yticks([])

plt.show()


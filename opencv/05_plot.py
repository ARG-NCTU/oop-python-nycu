import matplotlib.pyplot as plt
import cv2

data_path = '/home/arg/oop-python-nycu/images/'
data_name = 'smarties'
data_type = '.png'

# Load three images
img1 = cv2.imread(data_path + data_name + data_type)
img2 = cv2.imread(data_path + data_name + '_gray' + data_type)
img3 = cv2.imread(data_path + data_name + '_circle' + data_type)

# Create a figure with 3 subplots
fig, axs = plt.subplots(1, 3, figsize=(10, 10))

# Display the first image in the first subplot
axs[0].imshow(cv2.cvtColor(img1, cv2.COLOR_BGR2RGB))
axs[0].set_title('Raw')

# Display the second image in the second subplot
axs[1].imshow(cv2.cvtColor(img2, cv2.COLOR_BGR2RGB))
axs[1].set_title('Gray')

# Display the third image in the third subplot
axs[2].imshow(cv2.cvtColor(img3, cv2.COLOR_BGR2RGB))
axs[2].set_title('Hough Detect')

# Show the plot
plt.show()

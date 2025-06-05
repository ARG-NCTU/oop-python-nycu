import cv2
import numpy as np
import matplotlib.pyplot as plt

def show_img(img, title="Image"):
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    plt.imshow(img_rgb)
    plt.title(title)
    plt.axis('off')
    plt.show()

### === DEMO 1 === ###
# Step 0. Load crying emoji image
img = cv2.imread('crying.png')  # 請自行確認檔名
if img is None:
    raise ValueError("哭臉圖片找不到，請確認檔案名稱。")
show_img(img, "Original Crying Emoji")

# Step 1. Detect yellow region
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
lower_yellow = np.array([20, 100, 100])
upper_yellow = np.array([30, 255, 255])
mask = cv2.inRange(hsv, lower_yellow, upper_yellow)
contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
img_contours = img.copy()
cv2.drawContours(img_contours, contours, -1, (0, 255, 0), 2)
show_img(img_contours, "Yellow Color Contours")

# Step 2. Draw ROI boxes
img_blobs = img.copy()
for cnt in contours:
    x, y, w, h = cv2.boundingRect(cnt)
    cv2.rectangle(img_blobs, (x, y), (x + w, y + h), (255, 0, 0), 2)
show_img(img_blobs, "ROI Bounding Box")

# Step 3. Replace region with smiley face
smile = cv2.imread('smiley.png')  # 請自行確認檔名
if smile is None:
    raise ValueError("笑臉圖片找不到，請確認檔案名稱。")
for cnt in contours:
    x, y, w, h = cv2.boundingRect(cnt)
    smile_resized = cv2.resize(smile, (w, h))
    img[y:y+h, x:x+w] = smile_resized
show_img(img, "Smiley Face Replaced")

### === DEMO 2 === ###
img2 = cv2.imread("cbum.jpg")
if img2 is None:
    raise ValueError("Demo2 圖片找不到")
gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

# Histogram Equalization
equalized = cv2.equalizeHist(gray)

# CLAHE
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
enhanced = clahe.apply(gray)

# Plot all
img_rgb = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)
eq_rgb = cv2.cvtColor(equalized, cv2.COLOR_GRAY2RGB)
clahe_rgb = cv2.cvtColor(enhanced, cv2.COLOR_GRAY2RGB)

plt.figure(figsize=(15, 5))
titles = ["Original", "Histogram Equalized", "CLAHE Enhanced"]
images = [img_rgb, eq_rgb, clahe_rgb]

for i in range(3):
    plt.subplot(1, 3, i+1)
    plt.imshow(images[i])
    plt.title(titles[i])
    plt.axis('off')

plt.tight_layout()
plt.show()

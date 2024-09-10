import cv2
import numpy as np


def find_and_draw_contours(image):
    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # Apply Canny edge detection to the grayscale image
    edged = cv2.Canny(gray, 30, 200)
    # Find the contours in the edged image using RETR_EXTERNAL mode
    contours, hierarchy = cv2.findContours(edged, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    # Draw the contours on the original image
    cv2.drawContours(image, contours, -1, (0, 255, 0), 3)

    # Print the number of contours found
    print("Number of Contours found = " + str(len(contours)))

    # Return the original image with the contours drawn
    return image


if __name__ == "__main__":
    image = cv2.imread('/home/arg/oop-python-nycu/images/potter.jpg')
    cv2.imshow('Input Image', image)
    cv2.waitKey(0)
    #the input image is too big, resize the image into 800*500
    image = cv2.resize(image, (800, 500))
    image = find_and_draw_contours(image)
    cv2.imwrite('/home/arg/oop-python-nycu/images/potter_contour.jpg', image)
    cv2.imshow('Contours', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

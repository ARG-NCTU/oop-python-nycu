import cv2
import numpy as np


def find_and_draw_contours(image):
    # Convert the image to grayscale
    
    # Apply Canny edge detection to the grayscale image
    
    # Display the edged image with contours
    
    # Find the contours in the edged image using RETR_EXTERNAL mode
    
    # Draw the contours on the original image
    #print("Number of Contours found = " + str(len(contours)))
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

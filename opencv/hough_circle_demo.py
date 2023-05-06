import sys
import cv2 as cv
import numpy as np


def main(argv):
    ## [load]
    data_path = '/home/arg/oop-python-nycu/images/'
    data_name = 'screen'
    data_type = '.png'
    default_file = data_path + data_name + data_type

    filename = argv[0] if len(argv) > 0 else default_file

    # Loads an image
    src = cv.imread(cv.samples.findFile(filename), cv.IMREAD_COLOR)

    # Check if image is loaded fine
    if src is None:
        print ('Error opening image!')
        print ('Usage: hough_circle.py [image_name -- default ' + default_file + '] \n')
        return -1
    ## [load]

    ## [convert_to_gray]
    # Convert it to gray
    gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
    saved_name = data_name + '_gray'
    saved_file = data_path + saved_name + data_type
    cv.imwrite(saved_file, gray)
    ## [convert_to_gray]

    ## [reduce_noise]
    # Reduce the noise to avoid false circle detection
    gray = cv.medianBlur(gray, 5)
    ## [reduce_noise]

    ## [houghcircles]
    rows = gray.shape[0]
    # Demo 1 : Let the hough circle detect work !
    circles = cv.HoughCircles(gray, cv.HOUGH_GRADIENT, 1, rows / 8,
                               param1=100, param2=30,
                               minRadius=1, maxRadius=30)
    # Please Know what is changing when you adjust every argument!!
    ## [houghcircles]
    
    ## [draw]
    if circles is not None:
        circles = np.uint16(np.around(circles))
        for i in circles[0, :]:
            center = (i[0], i[1])
            # circle center
            cv.circle(src, center, 1, (0, 100, 100), 3)
            # circle outline
            radius = i[2]
            cv.circle(src, center, radius, (255, 0, 255), 3)
    ## [draw]

    saved_name = data_name + '_circle'
    saved_file = data_path + saved_name + data_type
    cv.imwrite(saved_file, src)

    return 0


if __name__ == "__main__":
    main(sys.argv[1:])

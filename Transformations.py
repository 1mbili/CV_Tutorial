import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

def value_change():
    pass

def createImages(image):
    """
    Args:
    ------
    - 'image` : Path to image
    Returns:
    ------
    Two openCV imshows. One with picture from path. Second image after edge detection with two trackbasrs to choese min and max thresholds. 
    """
    
    img = cv.imread(image, 0)
    messi = cv.namedWindow('Messi')

    cv.createTrackbar('MinThres', 'Messi', 0, 255, value_change)
    cv.createTrackbar('MaxThres', 'Messi', 0, 255, value_change)

    while(1):
        minThres = cv.getTrackbarPos('MinThres', messi)
        maxThres = cv.getTrackbarPos('MaxThres', messi)

        k = cv.waitKey(5) & 0xFF
        if k==ord('q'):
            break

        edges = cv.Canny(img, minThres, maxThres)
        cv.imshow('image', img)
        cv.imshow('Messi', edges)

    cv.destroyAllWindows()     
    cv.waitKey()




def main():
    createImages('Messi.jpg')


if __name__ == "__main__":
    main()

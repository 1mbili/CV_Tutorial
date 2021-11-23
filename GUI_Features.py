#!/usr/bin/python3
import numpy as np
import cv2 as cv

def drawCvLogo(n : int) -> np.ndarray:
    """
    
    Args:
    ------
    - `n` : size of square side in which CV logo will be created
    
    Returns:
    ------
    - Return array with created CV logo. Raise error if side is smaller than 0.
    """
    
    if n < 0:
        print("Size of a square side must be greater than 0")
        raise AttributeError 

    border = int(n/40)
    radius = int(n/4)
    radiusSmall = int(n/8)
    img = np.ones((n,n,3), np.uint8)
    cv.ellipse(img,(radius,n-radius),(radius-border,radius-border),0,0,285,(0,255,0),-1)
    cv.ellipse(img,(radius*3-border,n-radius),(radius-border,radius-border),305,0,285, (255,0,0),-1)
    cv.ellipse(img,(radius*2-border,n-radius*3+border),(radius-border,radius-border),130,0,285, (0,0,255),-1)
    cv.circle(img,(radius*2-border,n-radius*3+border), radiusSmall, (0,0,0), -1)
    cv.circle(img,(radius,n-radius), radiusSmall, (0,0,0), -1)
    cv.circle(img,(radius*3-border,n-radius), radiusSmall, (0,0,0), -1)
    return img

def main():
    img = drawCvLogo(500)        
    cv.imshow("foo",img)
    cv.waitKey()
    
if __name__ == '__main__':
    main()
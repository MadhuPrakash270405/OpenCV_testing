import cv2
import numpy as np




def test_Template_matching():
    # Load the input image and the template
    src = cv2.imread('./images/TM_Input1.jpg')
    template_img = cv2.imread('./images/TM_Input2.jpg')
    src = cv2.cvtColor(src, cv2.COLOR_RGB2GRAY)
    temp = cv2.cvtColor(template_img, cv2.COLOR_RGB2GRAY) 
    methods = [cv2.TM_CCOEFF, cv2.TM_CCOEFF_NORMED, cv2.TM_CCORR,
             cv2.TM_CCORR_NORMED, cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED] 
    height, width =src.shape
    H, W = temp.shape
    for method in methods:
        src2 = src.copy()
        result = cv2.matchTemplate(src2, temp, method)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
        print(min_loc, max_loc)
        if method in [cv2.TM_SQDIFF,cv2.TM_CCORR]:
            lacation = min_loc
        else:
            location = max_loc
        bottom_right = (location[0] + W, location[1] + H)
        cv2.rectangle(src2, location,bottom_right, 255, 5)
        cv2.imshow('Final Image', src2)
        cv2.waitKey(0)
        cv2.destroyAllWindows() 

if __name__ == '__main__':
    test_Template_matching()

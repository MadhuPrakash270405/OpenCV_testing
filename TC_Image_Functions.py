import sys
import cv2
import os


def get_size_of_the_image(filename):
    if os.path.exists(filename):
        print(filename)
        img = cv2.imread(filename,0)
        height, width = img.shape[:2]
        print(f'height:{height} width:{width}')
        return height,width
    return 0,0

#cv2.imread() function reads an image correctly.
def read_image(filename):
    if os.path.exists(filename):
        print(filename)
        img = cv2.imread(filename)
        return img.shape
    return (0,0,0)


#cv2.resize() function resizes an image correctly.
def image_resize(filename):
    if os.path.exists(filename):
        print(filename)
        img = cv2.imread(filename)
        resized_img = cv2.resize(img, (256, 256))
        return resized_img.shape
    return (0,0)
    

# cv2.threshold() function threshold an image correctly
def image_threshold(filename):
    if os.path.exists(filename):
        print(filename)
        img = cv2.imread(filename, 0)
        ret, thresh = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
        return thresh.shape
    return (0,0)


# cv2.cvtColor() function converts an image to the desired color space.
def image_cvt_color(filename):
    if os.path.exists(filename):
        print(filename)
        img = cv2.imread('test.jpg')
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        return gray.shape
    return (0,0)


def imread_imshow_integration(filename):
    if os.path.exists(filename):
        print(filename)
        img = cv2.imread('test.jpg')
        cv2.imshow('image', img)
        cv2.destroyAllWindows()
    

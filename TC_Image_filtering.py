import pytest
import cv2
import numpy as np
# Define the image filtering function
def image_filtering(img_path):
    # Load the image
    img = cv2.imread(img_path)

    # Apply a Gaussian filter with a 5x5 kernel and a sigma of 0
    blur = cv2.GaussianBlur(img, (5, 5), 0)

    # Apply a median filter with a kernel size of 3
    median = cv2.medianBlur(img, 3)

    # Apply a bilateral filter with a kernel size of 9 and a sigma values of 75 and 75
    bilateral = cv2.bilateralFilter(img, 9, 75, 75)

    # Return the filtered images
    return blur, median, bilateral


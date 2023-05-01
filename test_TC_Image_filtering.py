
import pytest
import numpy as np
import cv2
from TC_Image_filtering import image_filtering


img_path = './images/sample_image_2.jpg'
img = cv2.imread(img_path)
blur, median, bilateral = image_filtering(img_path)


def test_gaussian_filter():    
    # Check that the output image has the same shape as the input image
    assert blur.shape == img.shape
    # Check that the output image is not identical to the input image
    assert not np.array_equal(blur, img)

def test_median_filter():
    # Check that the output image has the same shape as the input image
    assert median.shape == img.shape
    # Check that the output image is not identical to the input image
    assert not np.array_equal(median, img)

def test_bilateral_filter():    
    # Check that the output image has the same shape as the input image
    assert bilateral.shape == img.shape
    # Check that the output image is not identical to the input image
    assert not np.array_equal(bilateral, img)


def test_images_have_same_shape():
    # Check if the images have the same shape
    assert blur.shape == median.shape == bilateral.shape


def test_if_invalid_file_path_is_given():
    # Test case 2: Test the function with an invalid image path
    with pytest.raises(TypeError):
        image_filtering(123)



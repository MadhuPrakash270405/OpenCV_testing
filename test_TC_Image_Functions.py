import pytest
import cv2
import TC_Image_Functions as IF_func

@pytest.mark.parametrize("file_name, expected", [('./images/sample_image_5.jpg',(3648, 5472, 3)),
                                                 ('./images/sample_image_6.jpg', (0,0,0))])
def test_read_image(file_name,expected):
    assert IF_func.read_image(file_name) == expected


@pytest.mark.parametrize("file_name, expected", [('./images/sample_image_5.jpg', (3648,5472)),
                                                 ('./images/sample_image_6.jpg', (0,0))])
def test_get_size_of_the_image(file_name,expected):
    assert IF_func.get_size_of_the_image(file_name) == expected


@pytest.mark.parametrize("file_name, expected", [('./images/sample_image_5.jpg', (3648, 5472)),
                                                 ('./images/sample_image_6.jpg', (0,0))])
def test_image_threshold(file_name,expected):
    assert IF_func.image_threshold(file_name) == expected


@pytest.mark.parametrize("file_name, expected", [('./images/sample_image_5.jpg', (3648, 5472)),
                                                 ('./images/sample_image_6.jpg', (0,0))])
def test_image_threshold(file_name,expected):
    assert IF_func.image_threshold(file_name) == expected

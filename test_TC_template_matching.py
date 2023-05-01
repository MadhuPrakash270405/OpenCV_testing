import cv2
import pytest

@pytest.fixture
def template_matching_input():
    src = cv2.imread('./images/TM_Input1.jpg')
    template = cv2.imread('./images/TM_Input2.jpg')
    return src, template

def test_template_matching_result(template_matching_input):
    src, template = template_matching_input
    src = cv2.cvtColor(src, cv2.COLOR_RGB2GRAY)
    temp = cv2.cvtColor(template, cv2.COLOR_RGB2GRAY) 
    methods = [cv2.TM_CCOEFF, cv2.TM_CCOEFF_NORMED, cv2.TM_CCORR,
             cv2.TM_CCORR_NORMED, cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED] 
    height, width = src.shape
    H, W = temp.shape
    for method in methods:
        src2 = src.copy()
        result = cv2.matchTemplate(src2, temp, method)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
        if method in [cv2.TM_SQDIFF,cv2.TM_CCORR]:
            location = min_loc
        else:
            location = max_loc
        bottom_right = (location[0] + W, location[1] + H)
        cv2.rectangle(src2, location, bottom_right, 255, 5)
        assert isinstance(src2, type(src))
        assert isinstance(result, type(src))
        assert isinstance(location, tuple)
        assert isinstance(bottom_right, tuple)
        assert len(location) == 2
        assert len(bottom_right) == 2
        # assert isinstance(result[0][0], float)
        # assert isinstance(result[height-1][width-1], float)

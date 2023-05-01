import pytest

import pathlib
import TC_Face_detection as TC_Face_detection

@pytest.mark.parametrize("file_name, expected", [('./images/chris_evans.jpg',1),
                                                 ('./images/no_faces.jpg', 0)])
def test_face_detection_func(file_name,expected):
    assert TC_Face_detection.test_face_detection(file_name) == expected, "No face detected in the test image"



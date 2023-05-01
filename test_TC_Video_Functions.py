

import pytest
import TC_Video_Functions as VF_func

@pytest.mark.parametrize("file_name, expected", [('./videos/SampleVideo_1280x720_1mb.mp4',True),
                                                 ('./images/SampleVideo_2.jpg', False)])
def test_read_image(file_name,expected):
    assert VF_func.video_capture(file_name) == expected


@pytest.mark.parametrize("file_name, expected", [('./videos/SampleVideo_1280x720_1mb.mp4',True),
                                                 ('./images/SampleVideo_2.jpg', False)])
def test_video_writer(file_name,expected):
    assert VF_func.video_writer(file_name) == expected




# @pytest.mark.parametrize("file_name, expected", [('./videos/SampleVideo_1280x720_1mb.mp4',True),
#                                                  ('./images/SampleVideo_2.jpg', False)])
# def test_video_cvt_color(file_name,expected):
#     assert video_cvt_color(file_name) == expected


# @pytest.mark.parametrize("file_name, expected", [('./videos/SampleVideo_1280x720_1mb.mp4',-1),
#                                                  ('./images/SampleVideo_2.jpg', 0)])
# def test_video_capture_imshow_integration(file_name,expected):
#     assert video_capture_imshow_integration(file_name) == expected


# @pytest.mark.parametrize("file_name, expected", [('./videos/SampleVideo_1280x720_1mb.mp4',(-1,True)),
#                                                  ('./images/SampleVideo_2.jpg', (0,False))])
# def test_video_processing_integration(file_name,expected):
#     assert video_processing_integration(file_name) == expected


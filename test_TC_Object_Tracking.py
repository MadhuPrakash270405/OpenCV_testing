import cv2
import pytest


VIDEO_PATH='./videos/captain_america.mp4'
# Initialize the video capture object
cap = cv2.VideoCapture(VIDEO_PATH)

# Test if the video capture object is opened successfully
def test_video_capture():
    assert cap.isOpened() == True

# Read the first frame of the video
def test_read_first_frame():
    ret, frame = cap.read()
    assert ret == True
    assert frame.shape == (720, 1280, 3)

# Test if the ROI is correctly set
def test_set_roi():
    ret, frame = cap.read()
    r, h, c, w = 200, 300, 350, 400
    track_window = (c, r, w, h)
    roi = frame[r:r+h, c:c+w]
    assert roi.shape == (300, 400, 3)

# Test if the histogram is correctly calculated and normalized
def test_calculate_histogram():
    ret, frame = cap.read()
    r, h, c, w = 200, 300, 350, 400
    track_window = (c, r, w, h)
    roi = frame[r:r+h, c:c+w]
    hsv_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)

    mask = cv2.inRange(hsv_roi, (0, 60, 32), (180, 255, 255))
    roi_hist = cv2.calcHist([hsv_roi], [0], mask, [180], [0, 180])

    cv2.normalize(roi_hist, roi_hist, 0, 255, cv2.NORM_MINMAX)

    assert roi_hist.shape == (180, 1)

# Test if the object tracking algorithm is working correctly
def test_object_tracking():
    term_crit = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 1)
    ret, frame = cap.read()
    r, h, c, w = 200, 300, 350, 400
    track_window = (c, r, w, h)
    roi = frame[r:r+h, c:c+w]
    hsv_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)

    mask = cv2.inRange(hsv_roi, (0, 60, 32), (180, 255, 255))
    roi_hist = cv2.calcHist([hsv_roi], [0], mask, [180], [0, 180])
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        dst = cv2.calcBackProject([hsv], [0], roi_hist, [0, 180], 1)
        ret, track_window = cv2.meanShift(dst, track_window, term_crit)

        x, y, w, h = track_window
        frame = cv2.rectangle(frame, (x, y), (x + w, y + h), 255, 2)

        assert frame.shape == (720, 1280, 3)
        assert track_window != (c, r, w, h)

# Test if the video capture object is released and the window is closed
def test_release_and_close():
    cap.release()
    cv2.destroyAllWindows()
    assert cap.isOpened() == False

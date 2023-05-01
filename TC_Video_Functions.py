import sys
import cv2
import os

def video_capture(filename):
    if os.path.exists(filename):
        print(filename)
        cap = cv2.VideoCapture(filename)
        return cap.isOpened()
    return False

def video_writer(filename):
    if os.path.exists(filename):
        print(filename)
        cap = cv2.VideoCapture(filename)
        ret, frame = cap.read()
        height, width, channels = frame.shape
        out = cv2.VideoWriter('output.avi', cv2.VideoWriter_fourcc(*'MJPG'), 30, (width,height))
        out.write(frame)
        return os.path.isfile('output.avi')
    return False

def video_cvt_color(filename):
    if os.path.exists(filename):
        print(filename)
        cap = cv2.VideoCapture(filename)
        ret, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        return gray.shape == frame.shape[:2]
    return False

def video_capture_imshow_integration(filename):
    if os.path.exists(filename):
        print(filename)
        cap = cv2.VideoCapture(filename)
        while(cap.isOpened()):
            ret, frame = cap.read()
            if ret == True:
                cv2.imshow('frame',frame)
                if cv2.waitKey(25) & 0xFF == ord('q'):
                    break
            else:
                break
        cap.release()
        cv2.destroyAllWindows()
        return cv2.getWindowProperty('frame', 0)
    return 0




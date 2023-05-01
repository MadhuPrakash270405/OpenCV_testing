

import cv2

def test_case_1():
    face_cascade = cv2.CascadeClassifier('./xml_files/haarcascade_frontalface_default.xml')
    img = cv2.imread('./images/chris_evans.jpg')
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 2)
    cv2.imshow('img', img)
    cv2.waitKey()


def test_face_detection():
    # Load the cascade
    face_cascade = cv2.CascadeClassifier('./xml_files/haarcascade_frontalface_default.xml')
    # Read the input image
    img = cv2.imread('./images/chris_evans.jpg')
    # Convert into grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Detect faces
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    # Verify that at least one face is detected


# TODO: Test No Faces Detected
    assert len(faces) >= 1, "No face detected in the test image"

# # TODO: Verify that all detected faces have a valid bounding box
#     for (x, y, w, h) in faces:
#         assert x >= 0 and y >= 0 and w >= 0 and h >= 0, "Invalid bounding box detected for a face"

# # TODO: Verify that the face detection is robust to different poses and angles
#     img_pose = cv2.imread('test_image_pose.jpg')
#     gray_pose = cv2.cvtColor(img_pose, cv2.COLOR_BGR2GRAY)
#     faces_pose = face_cascade.detectMultiScale(gray_pose, 1.1, 4)
#     assert len(faces_pose) >= 1, "No face detected in the test image with a different pose"

# #TODO:  Verify that no face is detected in an image with no faces
#     img_no_faces = cv2.imread('test_image_no_faces.jpg')
#     gray_no_faces = cv2.cvtColor(img_no_faces, cv2.COLOR_BGR2GRAY)
#     faces_no_faces = face_cascade.detectMultiScale(gray_no_faces, 1.1, 4)
#     assert len(faces_no_faces) == 0, "Unexpected face detected in the test image with no faces"

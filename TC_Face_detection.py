
import os
import cv2
def test_face_detection(filepath):
    directory, filename = os.path.split(filepath)
    print(f"==============={filename}=======================")
    faceCascade = cv2.CascadeClassifier('./xml_files/haarcascade_frontalface_default.xml')
    image = cv2.imread(filepath)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.3,
        minNeighbors=3,
        minSize=(30, 30)
    )
    print("[INFO] Found {0} Faces!".format(len(faces)))
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
    status = cv2.imwrite(f'./output/{filename}_faces_detected.jpg', image)
    print("[INFO] Image faces_detected.jpg written to filesystem: ", status)
    return len(faces)



# if __name__ == '__main__':
#     test_face_detection('./images/chris_evans.jpg')
#     test_face_detection('./images/no_faces.jpg')
#     test_face_detection('./images/DC.jpg')
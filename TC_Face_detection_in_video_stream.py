import time
import cv2
import numpy as np


def test_face_detection_video_stream():
    # Load the cascade classifier
    face_cascade = cv2.CascadeClassifier('./xml_files/haarcascade_frontalface_default.xml')
    # Start the video stream
    cap = cv2.VideoCapture(0)  # 0 represents the default camera
    # Initialize variables to store the face IDs and their locations
    face_locations = {}
    face_id = 0
    start_time = time.time()
    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()
        if not ret:
            # If the frame cannot be read, break out of the loop
            break
        # Convert the frame to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # Detect faces in the frame
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)
        # Draw rectangles around the faces and label them with their IDs
        for (x, y, w, h) in faces:
            face_center = (int(x + w/2), int(y + h/2))
            matched_face_id = None
            # Check if the detected face matches with a previously detected face
            for fid, loc in face_locations.items():
                distance = ((loc[0]-face_center[0])**2 + (loc[1]-face_center[1])**2)**0.5
                if distance < w/2:
                    matched_face_id = fid
                    break
            # Assign a new ID if no matching face is found
            if matched_face_id is None:
                face_id += 1
                matched_face_id = face_id
            # Store the face location and ID in the dictionary
            face_locations[matched_face_id] = face_center
            # Draw the rectangle and label with the face ID
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(frame, f"Face {matched_face_id}", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
        # Display the resulting frame and the face count
        cv2.putText(frame, f"No. of Faces: {len(face_locations)}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
        cv2.imshow('frame', frame)
            # Check if the time limit has been reached
        elapsed_time = time.time() - start_time
        if elapsed_time >= 15:
            break
        # Exit if 'q' is pressed
        if cv2.waitKey(1) == ord('q'):
            break
    # Release the capture
    cap.release()
    cv2.destroyAllWindows()
    print(f'Total No of Faces:{face_id}')
    return faces,face_locations


# if __name__ == '__main__':
#     test_face_detection_video_stream()
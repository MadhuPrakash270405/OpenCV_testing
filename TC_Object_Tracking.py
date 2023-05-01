import cv2

# Initialize the video capture object
cap = cv2.VideoCapture('./videos/captain_america.mp4')

# Read the first frame of the video
ret, frame = cap.read()

# Select a region of interest (ROI) where the object is located
r, h, c, w = 200, 300, 350, 400  # Set the ROI parameters
track_window = (c, r, w, h)
roi = frame[r:r+h, c:c+w]

# Convert the ROI to the HSV color space
hsv_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)

# Calculate the histogram of the ROI
mask = cv2.inRange(hsv_roi, (0, 60, 32), (180, 255, 255))
roi_hist = cv2.calcHist([hsv_roi], [0], mask, [180], [0, 180])

# Normalize the histogram
cv2.normalize(roi_hist, roi_hist, 0, 255, cv2.NORM_MINMAX)

# Set the termination criteria
term_crit = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 1)

while True:
    # Read a new frame from the video
    ret, frame = cap.read()

    # If there are no more frames, break out of the loop
    if not ret:
        break

    # Convert the frame to the HSV color space
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Calculate the back projection of the histogram
    dst = cv2.calcBackProject([hsv], [0], roi_hist, [0, 180], 1)

    # Apply meanshift to get the new position of the object
    ret, track_window = cv2.meanShift(dst, track_window, term_crit)

    # Draw a rectangle around the object
    x, y, w, h = track_window
    frame = cv2.rectangle(frame, (x, y), (x + w, y + h), 255, 2)

    # Display the resulting frame
    cv2.imshow('Object Tracking', frame)

    # If the user presses 'q', break out of the loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture object and close the window
cap.release()
cv2.destroyAllWindows()

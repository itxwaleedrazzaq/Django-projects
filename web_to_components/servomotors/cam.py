import cv2

# Open a video capture object
cap = cv2.VideoCapture('http://172.24.96.1:56000/mjpeg')  # Use 0 for default camera, or specify the file path for a video file

# Check if the camera or file opened successfully
if not cap.isOpened():
    print("Error: Unable to open camera or file.")
    exit()

# Loop to continuously capture frames
while True:
    # Read a frame from the capture object
    ret, frame = cap.read()

    # Check if the frame was read successfully
    if not ret:
        print("Error: Unable to read frame.")
        break

    # Display the frame (you can perform additional processing here if needed)
    cv2.imshow('Video Stream', frame)

    # Break the loop if the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the capture object and close all windows
cap.release()
cv2.destroyAllWindows()

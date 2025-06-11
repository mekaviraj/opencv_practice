import cv2 as cv

# Replace 'sample_video.mp4' with the actual path to your video file
vid = cv.VideoCapture("C:\\Users\\VIRAJ M\\Desktop\\opencv\\sample_video.mp4")

while vid.isOpened():
    ret, frame = vid.read()  # Read a frame from the video
    if not ret:
        print("Video has ended or cannot be read.")
        break
    
    cv.imshow("Frame", frame)  # Display the frame
    if cv.waitKey(1) & 0xFF == ord('q'):  # Exit if 'q' is pressed
        print("Exiting...")
        break

vid.release()
cv.destroyAllWindows()

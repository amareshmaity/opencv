import cv2 as cv

## load video
video = cv.VideoCapture("./dog-cartoon.mp4")
if video.isOpened():
    print("video loaded successfully")
else:
    print("Error occured while loading the video")

## Play the video framwise
i=1
while True:
    ret, frame = video.read()
    if not ret:
        print("Error: Could not read frame or video ended.")
        break
    cv.imshow(f"frame{i}", frame)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break
    i+=1

video.release()
cv.destroyAllWindows()
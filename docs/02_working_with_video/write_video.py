import cv2 as cv
import os

## Load video
loaded_video = cv.VideoCapture("./dog-cartoon.mp4")
if not loaded_video.isOpened():
    print("Error to load video")
else:
    print("Video loaded successfully")


## write the video
output_folder = "video-frames"
os.makedirs(name=output_folder, exist_ok=True)

i=0
while True:
    ret, frame = loaded_video.read()
    if not ret:
        break
    frame+=20 # modify the video frame
    output_path = os.path.join(output_folder, f"frame_{i}.jpg")
    cv.imwrite(filename=output_path,  img=frame)
    if cv.waitKey(1) & 0xFF == ord("q"):
        break
    i+=1

loaded_video.release()
cv.destroyAllWindows()
print(f"Successfully saved {i-1} frames to {output_folder}")
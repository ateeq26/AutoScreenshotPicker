import cv2
import os

SOURCE_PATH = input("Enter the full path of your video file: ")
DESTINATION_PATH = input(
    "Enter the full path of the folder where images will be saved: ")

TIME_INTERVAL = int(
    input("Enter the time interval in secs of frame capture: "))


vidObj = cv2.VideoCapture(SOURCE_PATH)
fps = vidObj.get(cv2.CAP_PROP_FPS)

print("Frames per second = ", fps)

# Used as counter variable
count = 0

# checks whether frames were extracted
success = 1

while success:

    # vidObj object calls read
    # function extract frames
    success, image = vidObj.read()
    if(count % (fps*TIME_INTERVAL) == 0):
        # Saves the frames with frame-count
        cv2.imwrite(os.path.join(DESTINATION_PATH,
                                 "frame%d.jpg" % (count//(fps*TIME_INTERVAL))), image)

    count += 1

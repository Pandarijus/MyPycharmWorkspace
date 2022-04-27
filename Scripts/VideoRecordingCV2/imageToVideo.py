import cv2
import os
import regex as re

dirName = "out"
image_folder = f"Images/{dirName}"
videoPath = f"Videos/Video[{dirName}].avi"

images = [str(img) for img in os.listdir(image_folder) if img.endswith(".png") or img.endswith(".jpg")]

images.sort(key=lambda f: int(re.sub('\D', '', f)))
#print(images)
frame = cv2.imread(os.path.join(image_folder, images[0]))
height, width, layers = frame.shape

video = cv2.VideoWriter(videoPath, 0,30, (width,height))
print("saving started...")
for image in images:
    video.write(cv2.imread(os.path.join(image_folder, image)))

cv2.destroyAllWindows()
video.release()
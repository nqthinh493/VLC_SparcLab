import cv2
import numpy as np
import glob
import os


vidcap = cv2.VideoCapture('test.mp4')
success,image = vidcap.read()
count = 0

while success:
  if (count % 4 == 0):
    cv2.imwrite(str(count) + '.png', image)

  success, image = vidcap.read()

  print('Read a new frame: ', success)
  count += 1



os.system('ffmpeg -r 24 -f image2 -pattern_type glob -i "*?png" -vcodec libx264 -crf 20 -pix_fmt yuv420p output.mp4')
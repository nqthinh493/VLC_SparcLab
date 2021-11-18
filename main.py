import cv2
import numpy as np
import glob
import os
import math
import matplotlib.pyplot as plt
import matplotlib
from matplotlib.image import imread
import sys
import PyQt5


def column(matrix, i):
  return [row[i] for row in matrix]

vidcap = cv2.VideoCapture('test5.mp4')
fps = int(vidcap.get(cv2.CAP_PROP_FPS))
print(fps)
func = 1

def getNum(n):
  a = 30
  r = n%a
  return (n-r)/30

if fps>30:
  frame_count = int(vidcap.get(cv2.CAP_PROP_FRAME_COUNT))
  vidlength = frame_count/fps
  func = getNum(fps)

success,image = vidcap.read()
count = 0

while success:
  if (count % func == 0):
    cv2.imwrite(str(count) + '.png', image)

  success, image = vidcap.read()

  print('Read a new frame: ', success)
  count += 1

#câu lệnh dưới hiện tại mới áp dụng cho macos
os.system('ffmpeg -r 30 -f image2 -s 1920x1080 -i fig%d.png -vcodec libx264 -crf 25  -pix_fmt yuv420p output1.mp4')

vidcap = cv2.VideoCapture('output0.mp4')
success,frame = vidcap.read()
count = 0

k = 200
while success :
        #averzge pr
        average_line_ox = np.average(frame, axis = 0)
        m = len(average_line_ox)
        x = np.linspace(0, m, m, endpoint=False)

        average_line_oy = np.average(frame, axis = 1)
        n = len(average_line_oy)
        y = np.linspace(0, n, n, endpoint=False)


        thresh = 10  #0: black 255: white

        R, G, B = frame[:,:,0], frame[:,:,1], frame[:,:,2]
        frameGray = 0.2989 * R + 0.5870 * G + 0.1140 * B


        w2=frameGray.shape
        C = np.array(frameGray)
        C[:,1]
        D = C[:,k]
        max_valueD = np.max(D)
        print(max_valueD)
        coefficentd = w2/max_valueD

        n = len(C[:,1])

        y = np.linspace(0 , n, n, endpoint=False)
        plt.figure(figsize=(12, 5), dpi = 300)
        plt.title("Gray Image")

        #cv2.imwrite(str(count) + '.png', frameGray)     # save frame as JPEG file

        #plt.savefig(str(count) + '.png',transparent=True )
        plt.subplot(2, 2, 1)
        plt.title("Gray Image")
        plt.imshow(frameGray, cmap= 'gray')
        plt.plot(D, y)
        #plt.plot(D*coefficentd, y) bị lỗi operands could not be broadcast together with shapes (1920,) (2,)
        plt.axvline(x = k, color = 'r', linestyle = '--')
        plt.savefig('fig' + str(count) + '.png') # save each frame and plot plot on it

        #set fixed window position : https://stackoverflow.com/questions/7449585/how-do-you-set-the-absolute-position-of-figure-windows-with-matplotlib
        mngr = plt.get_current_fig_manager()
        #mngr.window.setGeometry(50,100,640, 800)
        ##window.setGeometry(900, 200, 500, 800)

        #plt.show()
        success, frame = vidcap.read()
        count += 1

vidcap.release()

#câu lệnh dưới hiện tại mới áp dụng cho macos
os.system('ffmpeg -r 30 -f image2 -s 1920x1080 -i fig%d.png -vcodec libx264 -crf 25  -pix_fmt yuv420p output2.mp4')

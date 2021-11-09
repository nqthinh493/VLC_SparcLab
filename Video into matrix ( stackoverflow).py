#https://stackoverflow.com/questions/42163058/how-to-turn-a-video-into-numpy-array
import cv2
import numpy as np
import sys

cap = cv2.VideoCapture('shuttle 1-2000, 500hz, 80cm.mp4')
frameCount = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
frameWidth = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frameHeight = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

buf = np.empty((frameCount, frameHeight, frameWidth, 3), np.dtype('uint8'))

fc = 0
ret = True

print(frameCount)
# transform every frame to matrix
fc = 0
while (fc < frameCount  and ret):
    np.set_printoptions(threshold=sys.maxsize)
    ret, buf[fc] = cap.read()
    gray = cv2.cvtColor(buf[fc], cv2.COLOR_BGR2GRAY)

    binary_image = cv2.threshold(gray, 15 , 255, cv2.THRESH_BINARY)[1]
    file=open('graytomatrix.txt',"a")
    file.write(f'{gray}\n')

    fc += 1
file.close()

cap.release()

#print specific frame
cv2.namedWindow('frame 1 ')
cv2.imshow('frame 1 ', buf[1])
n=cv2.imread("buf[1]")
print(n)

cv2.namedWindow('frame 2 ')
cv2.imshow('frame 2 ', buf[2])
n=cv2.imread("buf[2]")
print(n)

cv2.namedWindow('frame 3 ')
cv2.imshow('frame 3 ', buf[3])
n=cv2.imread("buf[3]")
print(n)
cv2.waitKey(0)
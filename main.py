
import numpy as np
import cv2
import time


cap = cv2.VideoCapture('../VLC_SparcLab/data/video/ss4000.mp4')


while cap.isOpened():
    
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (21, 21), 0)

    width = int(cap.get(3))
    height = int(cap.get(4))
    image = np.zeros(gray.shape, np.uint8)
    smaller_frame = cv2.resize(gray, (0, 0), fx = 0.5, fy = 0.5)
    
    image[:height//2, :width//2] = smaller_frame

    image[:height//2, width//2:] = smaller_frame


    
        
    cv2.imshow('inter frame', image)
    if cv2.waitKey(30) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()
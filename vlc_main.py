#Author: Nguyễn Quang Thịnh
import numpy as np
import cv2
import matplotlib.pyplot as plt
import os
from matplotlib.image import imread
directory ='data'
classes =['data-img']
os.path.abspath(os.getcwd())

def column(matrix, i):
    return [row[i] for row in matrix]


for i in classes:
    path = os.path.join(directory,i)
    
    for img in os.listdir(path):
        img_array = cv2.imread(os.path.join(path, img), cv2.IMREAD_GRAYSCALE)
        thresh = 10  #0: black 255: white
        img_org = cv2.imread(os.path.join(path, img),)
        img_binary = cv2.threshold(img_array, thresh, 255, cv2.THRESH_BINARY)[1]
        
        R, G, B = img_org[:,:,0], img_org[:,:,1], img_org[:,:,2]
        imgGray = 0.2989 * R + 0.5870 * G + 0.1140 * B

        
    
        average_line_ox = np.average(img_binary, axis = 1) 
        m = len(average_line_ox)
        x = np.linspace(0, m, m, endpoint=False)

        
        plt.show()
        # Plot 1
        plt.figure(figsize=(15, 3))
        plt.subplot(1, 3, 1)
        plt.imshow(img_org)

        # Plot 2
        plt.subplot(1, 3, 2)
        plt.imshow(imgGray, cmap= 'gray')
        # Plot 3
        plt.subplot(1, 3, 3)
        
        plt.plot(x, average_line_ox)
        
#         plt.plot(x, imgGray[1])
#         for i in range(len(imgGray[1])):
#             plt.plot(x, imgGray[i])
#             plt.show()
        
#         y = np.linspace(0, len(column(imgGray,1)), len(column(imgGray,1)), endpoint=False)

#         for i in range(column(imgGray, 1)):
#             A = column(imgGray, i)
#             plt.plot(A, y)
#             plt.show()
        plt.show()
    break
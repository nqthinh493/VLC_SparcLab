#Author: Nguyễn Quang Thịnh
import numpy as np
import cv2
import matplotlib.pyplot as plt
import os
from matplotlib.image import imread
from scipy.signal import find_peaks
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

        
        #average pr
        average_line_ox = np.average(img_binary, axis = 0) 
        m = len(average_line_ox)
        x = np.linspace(0, m, m, endpoint=False)

        average_line_oy = np.average(img_binary, axis = 1) 
        n = len(average_line_oy)
        y = np.linspace(0, n, n, endpoint=False)
        
        h , w = imgGray.shape



        
        A = np.array(imgGray)
        A[:,1]
        n = len(A[:,1])
        y = np.linspace(0 , n, n, endpoint=False)

        k = int(input())
        B = A[:,k]
    
        
        max_value = np.max(B)
        print(max_value)
        coefficent = w/max_value
        
        # Plot 1
        plt.figure(figsize=(20, 11))
        plt.subplot(2, 2, 1)
        plt.title("Origin Image")
        plt.imshow(img_org)
        plt.axvline(x = k, color = 'r', linestyle = '--')
        plt.subplot(2, 2, 2)
        plt.title("Gray Image")
 
        plt.imshow(imgGray, cmap= 'gray')
        plt.plot(B, y)
        plt.plot(B*coefficent, y)
        plt.subplot(2, 2, 3)
        plt.title("Histogram average of column")
        plt.plot(average_line_oy, y)
        
        plt.subplot(2, 2, 4)
        plt.title("Histogram at column " + str(k))
        # plt.plot(B, y)
        x = B
        peaks, _ = find_peaks(x, height=0)
        plt.plot(y, B)
        plt.plot(peaks, x[peaks],  "x")
        plt.show()
           
            
        plt.show()
    break

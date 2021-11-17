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

def medfilt(x, k):
    """Apply a length-k median filter to a 1D array x.
    Boundaries are extended by repeating endpoints.
    """
    import numpy as np

    assert k % 2 == 1, "Median filter length must be odd."
    assert x.ndim == 1, "Input must be one-dimensional."
    
    k2 = (k - 1) // 2
    y = np.zeros ((len (x), k), dtype=x.dtype)
    y[:,k2] = x
    for i in range (k2):
        j = k2 - i
        y[j:,i] = x[:-j]
        y[:j,i] = x[0]
        y[:-j,-(i+1)] = x[j:]
        y[-j:,-(i+1)] = x[-1]
    return np.median (y, axis=1)

def meanfilt(x, k):
    """Apply a length-k mean filter to a 1D array x.
    Boundaries are extended by repeating endpoints.
    """
    
    import numpy as np

    assert k % 2 == 1, "Median filter length must be odd."
    assert x.ndim == 1, "Input must be one-dimensional."
    
    k2 = (k - 1) // 2
    y = np.zeros((len(x), k), dtype=x.dtype)
    y[:,k2] = x
    for i in range(k2):
        j = k2 - i
        y[j:,i] = x[:-j]
        y[:j,i] = x[0]
        y[:-j,-(i+1)] = x[j:]
        y[-j:,-(i+1)] = x[-1]
    return np.mean(y, axis=1)

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
        # plt.subplot(2, 2, 1)
        # plt.title("Origin Image")
        # plt.imshow(img_org)
        # plt.axvline(x = k, color = 'r', linestyle = '--')
        plt.subplot(2, 2, 1)
        plt.title("Gray Image")
        plt.axvline(x = k, color = 'r', linestyle = '--')
        plt.imshow(imgGray, cmap= 'gray')
        plt.subplot(2, 2, 2)

        plt.title("Histogram at column " + str(k))
        plt.plot(B, y)
        plt.plot(B*coefficent, y)
        plt.subplot(2, 2, 3)
        plt.title("apply median filter")
        plt.plot(medfilt(B,3), y)
        plt.subplot(2, 2, 4)
        plt.title("apply mean filter")
        # plt.plot(meanfilt(medfilt(B,3),5), y)
        filterB = meanfilt(medfilt(B,3),5)
        x = filterB
        peaks, _ = find_peaks(x, height=0, distance=10)
        plt.plot(filterB, y)
        plt.plot(x[peaks], peaks, "x")

        #local minimum
        x_cv = x* (-1)
        
        peaks_cv, _ = find_peaks(x_cv, height=-40, distance=10)
        plt.plot(x[peaks_cv], peaks_cv, "x")
        print(peaks_cv)
        plt.show()  

    break

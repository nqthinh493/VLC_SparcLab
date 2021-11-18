#Author: Nguyễn Quang Thịnh
from matplotlib.colors import Colormap
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

def Distance_Of_Adjacent_LocalExtrema(array):
    DistanceArr = []
    for i in range(len(array)):
        
        if i != 0:
            Distance = array[i] - array[i-1]
            DistanceArr.append(Distance)
    return DistanceArr

k = int(input())

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

        
        B = A[:,k]
    
        
        max_value = np.max(B)
        print(max_value)
        coefficent = w/max_value
        
        # Plot 1
        plt.figure(1, figsize=(20, 11))
        plt.subplot(2, 2, 1)
        plt.title("Gray Image")
        plt.xlabel("Row Matrix") 
        plt.ylabel("Colunm Matrix")
        plt.axvline(x = k, color = 'y', linestyle = '--')
        plt.imshow(imgGray, cmap= 'gray')


        plt.subplot(2, 2, 2)
        plt.title("Histogram at column Matrix " + str(k))
        plt.xlabel("Gray Value") 
        plt.ylabel("Colunm Matrix " + str(k))
        plt.plot(B, y)
 


        plt.subplot(2, 2, 3)
        plt.title("Median filtered & Mean filtered")
        plt.xlabel("Gray Value") 
        plt.ylabel("Colunm Matrix " + str(k))
        filterB = meanfilt(medfilt(B,3),7)
        plt.plot(filterB, y)


        plt.subplot(2, 2, 4)
        plt.title("Local extrema")
        plt.xlabel("Gray Value") 
        plt.ylabel("Colunm Matrix " + str(k))
        # plt.plot(meanfilt(medfilt(B,3),5), y)
        
        x = filterB
        peaks, _ = find_peaks(x, height=0, distance=10)
        plt.plot(filterB, y)
        plt.plot(x[peaks], peaks, "o", label="Local Extrema - Max")

        #local minimum
        x_cv = x* (-1)  #convert 
        peaks_cv, _ = find_peaks(x_cv, height=-40, distance=10)
        plt.plot(x[peaks_cv], peaks_cv, "o", label="Local Extrema - Min")
        print(peaks)
        print(Distance_Of_Adjacent_LocalExtrema(peaks))
        print(peaks_cv)
        print(Distance_Of_Adjacent_LocalExtrema(peaks_cv))
        plt.legend()



        plt.figure(2)

        plt.plot(Distance_Of_Adjacent_LocalExtrema(peaks), linestyle='dashed', label="Distance of Adjacent Local Extrema - Max")
        plt.plot(Distance_Of_Adjacent_LocalExtrema(peaks_cv), linestyle='dashed', label="Distance of Adjecent Local Extrema - Min")
        plt.ylim(0, 100)
        plt.legend()

        plt.show()

        


    break

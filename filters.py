import numpy as np
import matplotlib.pyplot as plt
from skimage import io
from skimage.color import rgb2gray
from scipy import signal
import math

def boxFilter(n):
    img_path = 'lena.png'
    img = io.imread(img_path)
    img = rgb2gray(img)
    
    img = np.pad(img, pad_width = int(n/2), mode='constant', constant_values = 0)
    img_out = img.copy()
    
    height = img.shape[0]
    width = img.shape[1]

    for i in np.arange(0, height):
        for j in np.arange(0, width):        
            sum = 0
            for k in np.arange(-(int(n/2)), int(n/2)):
                for l in np.arange(-(int(n/2)), int(n/2)):
                    a = img.item(i+k, j+l)
                    sum = sum + a
            b = int(sum / (n * n))
            img_out.itemset((i,j), b)
    
    fig1 = plt.figure(figsize = (7,7))
    plt.imshow(img, cmap='gray')
    
boxFilter(3)
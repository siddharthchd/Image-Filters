import numpy as np
import matplotlib.pyplot as plt
from skimage import io
from skimage.color import rgb2gray
from scipy import signal
import math

# Read the image and be sure it is grayscale
im_path = 'Image-Filters/lena.png'
im = io.imread(im_path)
im = rgb2gray(im)

# Ensure the image is a float in the range [0-1]
im = ((im - np.min(im)) * (1/(np.max(im) - np.min(im)) *1.0)).astype('float')

# Show the image
fig1 = plt.figure(figsize = (7,7))
plt.imshow(im, cmap='gray')
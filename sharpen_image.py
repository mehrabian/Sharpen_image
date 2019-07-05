import matplotlib.pyplot as plt
import matplotlib
import numpy as np
matplotlib.use('Agg')
from PIL import Image
import os

bins=256
# Load the image into an array: image
image= plt.imread('gray.jpeg')

def get_image_dimensions(imagefile):
    """
    Helper function that returns the image dimentions

    :param: imagefile str (path to image)
    :return dict (of the form: {width:<int>, height=<int>, size_bytes=<size_bytes>)
    """
    # Inline import for PIL because it is not a common library
    with Image.open(imagefile) as img:
        # Calculate the width and hight of an image
        width, height = img.size

    # calculat ethe size in bytes
    size_bytes = os.path.getsize(imagefile)

    return dict(width=width, height=height, size_bytes=size_bytes)

print( get_image_dimensions('gray.jpeg'))
plt.imshow(image,cmap='gray')
#plt.grid('off')
plt.savefig('image.jpg')
# Flatten the image into 1 dimension: pixels
pixels = image.flatten()
#==================================================
plt.subplot(2,1,1)
plt.title('Original image')
plt.axis('off')
plt.imshow(image,cmap='gray')

plt.subplot(2,1,2)
# Display a histogram of the pixels in the bottom subplot
pdf = plt.hist(pixels, bins=bins, range=(0,256), density=True, color='red', alpha=0.4)
#plt.grid('off')
# Use plt.twinx() to overlay the CDF in the bottom subplot
plt.twinx()
# Display a cumulative histogram of the pixels
cdf,bins,patches = plt.hist(pixels, bins=bins, range=(0,256), cumulative=True, density=True, color='blue', alpha=0.4)
# Specify x-axis range, hide axes, add title and display plot
plt.xlim((0,256))
#plt.grid(False)
plt.title('PDF & CDF (original image)')
plt.savefig('hist.jpg',cmap='gray')
plt.clf()
# Generate a cumulative histogram
new_pixels = np.interp(pixels, bins[:-1], cdf*255)
# Reshape new_pixels as a 2-D array: new_image
new_image = new_pixels.reshape(image.shape)

# Display the new image with 'gray' color map
plt.subplot(2,1,1)
plt.title('Equalized image')
plt.axis('off')
plt.imshow(new_image,cmap='gray')

# Generate a histogram of the new pixels
plt.subplot(2,1,2)
pdf = plt.hist(new_pixels, bins=bins, range=(0,256), density=True,color='red', alpha=0.4)
#plt.grid('off')

# Use plt.twinx() to overlay the CDF in the bottom subplot
plt.twinx()
plt.xlim((0,256))
#plt.grid('off')

# Add title
plt.title('PDF & CDF (equalized image)')

# Generate a cumulative histogram of the new pixels
cdf = plt.hist(new_pixels, bins=bins, range=(0,256),cumulative=True, density=True,color='blue', alpha=0.4)
plt.savefig('hist_new.jpg',cmap='gray')
plt.clf()

plt.imshow(new_image,cmap='gray')
#plt.grid('off')
plt.savefig('image_new.jpg')

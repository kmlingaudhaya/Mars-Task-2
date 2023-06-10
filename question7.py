import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import numpy as np

image_path = 'C:/Users/leeche28/Downloads/Passport photo.jpg'

# RGB(3 streams) matrix representation of the image
labrat = mpimg.imread(image_path)

# My chosen brightness level
brightnessLevel = 160 / 3

# Get the dimensions of the image
height, width, _ = labrat.shape

# plt.imshow(labrat)
# plt.show()

# Initialize a list to store the type of each pixel
pixel_types = []
# Initializing a list to store the brightness of each pixels
brightness_level = []

modified_labrat = np.copy(labrat)

# Iterate over each pixel and compare with the threshold
for i in range(height):
    for j in range(width):
        r, g, b = labrat[i, j]
        if (0.21 * r + 0.72 * g + 0.07 * b) / 3 > brightnessLevel:
            modified_labrat[i, j] = [0, 0, 0]
        else:
            modified_labrat[i, j] = [255, 255, 255]

# Displaying the modified image
plt.imshow(modified_labrat)
plt.show()

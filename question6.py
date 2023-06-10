import matplotlib.image as mpimg

image_path = 'C:/Users/leeche28/Downloads/Passport photo.jpg'

# RGB(3 streams) matrix representation of the image
labrat = mpimg.imread(image_path)

# Define the threshold (RGB values)
threshold = (160, 160, 160)

# Get the dimensions of the image
height, width, _ = labrat.shape

# Initialize a list to store the type of each pixel
pixel_types = []

# Iterate over each pixel and compare with the threshold
for i in range(height):
    for j in range(width):
        r, g, b = labrat[i, j]
        if r > threshold[0] and g > threshold[1] and b > threshold[2]:
            pixel_types.append('typeA')
        else:
            pixel_types.append('typeB')

# Calculate the percentage of typeA and typeB pixels
total_pixels = height * width
typeA_percentage = (pixel_types.count('typeA') / total_pixels) * 100
typeB_percentage = (pixel_types.count('typeB') / total_pixels) * 100

# Print the percentage of typeA and typeB pixels
print("Percentage of typeA pixels:", round(typeA_percentage, 2))
print("Percentage of typeB pixels:", round(typeB_percentage, 2))



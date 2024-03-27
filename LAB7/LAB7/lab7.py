import cv2
import numpy

# Read the image
img = cv2.imread('photo-1627325071486-0b1e3083294a.jpg')

if img is None:
    print("Error: Image not found or could not be read.")
    exit()

# Split the image into BGR channels
blue, green, red = cv2.split(img)

# Display the channels
cv2.imshow('Blue Channel', blue)
cv2.imshow('Green Channel', green)
cv2.imshow('Red Channel', red)

# Set the green channel to zero
green = numpy.zeros_like(green)

# Merge the channels back
modified_image = cv2.merge((blue, green, red))

# Display the modified image
cv2.imshow('Modified Image', modified_image)

# Wait for a key press and close all windows
cv2.waitKey(0)
cv2.destroyAllWindows()

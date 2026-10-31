import numpy as np

img = np.array([[10, 20, 30, 40],
                [50, 60, 70, 80],
                [90, 100, 110, 120],
                [130, 140, 150, 160]])

print("Original Image:")
print(img)

print("\nReshaped Image:")
print(img.reshape(2, 8))

print("\nSliced Region:")
print(img[0:2, 0:2])

print("\nBrightness Adjusted:")
print(img + 20)

print("\nTransformed Image:")
matrix = np.array([[1, 0, 1, 0],
                   [0, 1, 0, 1],
                   [1, 0, 1, 0],
                   [0, 1, 0, 1]])
print(np.dot(img, matrix))

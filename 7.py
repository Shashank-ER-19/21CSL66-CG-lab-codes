import cv2
import numpy as np

# Load the image (replace "image.jpg" with your image path)
image_path = "image.jpg"
img = cv2.imread(image_path)

# Check if the image was successfully loaded
if img is None:
    print("unable to load image at",image_path)
    exit()

# Get the height and width of the image
height, width,_ = img.shape

# Split the image into four quadrants
up_left = img[0:height//2, 0:width//2]
up_right = img[0:height//2, width//2:width]
down_left = img[height//2:height, 0:width//2]
down_right = img[height//2:height, width//2:width]

# Create a blank canvas to display the quadrants
canvas = np.zeros((height, width, 3), dtype=np.uint8)

# Place the quadrants on the canvas
canvas[0:height//2, 0:width//2] = up_left
canvas[0:height//2, width//2:width] = up_right
canvas[height//2:height, 0:width//2] = down_left
canvas[height//2:height, width//2:width] = down_right

# Display the canvas with quadrants
cv2.imshow("Image Quadrants", canvas)
cv2.imshow("1", up_left)
cv2.imshow("2", up_right)
cv2.imshow("3", down_left)
cv2.imshow("4", down_right)

# Wait for a key press and close all OpenCV windows
cv2.waitKey(0)
cv2.destroyAllWindows()


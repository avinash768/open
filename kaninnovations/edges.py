import cv2
import numpy as np
import urllib.request

# Load the image from the URL
url = "https://cdn.pixabay.com/photo/2014/05/05/18/45/rubik-cube-337700_1280.jpg"
req = urllib.request.urlopen(url)
arr = np.asarray(bytearray(req.read()), dtype=np.uint8)
image = cv2.imdecode(arr, -1)

# Convert the image to the BGR color space
bgr_image = cv2.cvtColor(image, cv2.COLOR_RGBA2BGR)

# Define the lower and upper bounds for the blue color in BGR format
lower_blue = np.array([100, 0, 0])
upper_blue = np.array([255, 100, 100])

# Create a mask to isolate blue pixels
blue_mask = cv2.inRange(bgr_image, lower_blue, upper_blue)

# Apply edge detection to the blue region
edges = cv2.Canny(blue_mask, threshold1=30, threshold2=100)

# Display the original image
cv2.imshow("Original Image", bgr_image)

# Display the detected edges
cv2.imshow("Detected Edges", edges)

# Wait for a key press and close the windows
cv2.waitKey(0)
cv2.destroyAllWindows()

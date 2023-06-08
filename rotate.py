# Import module
from PIL import Image

# Load image
im = Image.open("images/img2.jpeg")

# Rotate image by degrees
im = im.rotate(45)

# Show image
im.show()

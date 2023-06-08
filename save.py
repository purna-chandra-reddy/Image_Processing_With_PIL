# Import module
from PIL import Image

# Load image from disk (change the path)
im = Image.open("images/img2.jpeg")

# Show image
im.show()

# Save image as bitmap
im.save("images/newImg2.png")

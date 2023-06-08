# Import PIL
from PIL import Image, ImageOps

# create image
originalImg = Image.open("images/img2.jpeg")

# flip vertically
flippedImage = ImageOps.flip(originalImg)

# show image
flippedImage.show()

 

# Import PIL
from PIL import Image, ImageOps

# create image
originalImg = Image.open("images/img2.jpeg")

# flip horizontally
mirrorImage = ImageOps.mirror(originalImg)

# show image
mirrorImage.show()

 

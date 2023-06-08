# Import PIL
from PIL import Image, ImageOps

# create image
originalImg = Image.open("images/img2.jpeg")

# invert image
invertImage = ImageOps.invert(originalImg)

# show image
invertImage.show()

 

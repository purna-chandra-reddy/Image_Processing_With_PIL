# Import PIL
from PIL import Image, ImageOps

# create image
originalImg = Image.open("images/img2.jpeg")

# turn image into gray scale
grayImage = ImageOps.grayscale(originalImg)

# show image
grayImage.show()

 

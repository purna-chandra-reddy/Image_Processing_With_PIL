# import PIL
from PIL import Image, ImageFilter

# load image
image = Image.open("images/Img1.jpg")

# apply effect using filter (kernel)
blurImage = image.filter(ImageFilter.GaussianBlur(15))

# display image
blurImage.show()


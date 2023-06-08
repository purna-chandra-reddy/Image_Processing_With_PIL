from PIL import Image, ImageFilter

# load image
image = Image.open("images/img2.jpeg")

# apply effect
newImage = image.filter(ImageFilter.SHARPEN)

# display image
newImage.show()


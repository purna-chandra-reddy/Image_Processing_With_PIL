from PIL import Image, ImageFilter

# load image
image = Image.open("images/img2.jpeg")

# apply effect
newImage = image.filter(ImageFilter.EMBOSS)

# display image
newImage.show()


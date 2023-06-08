from PIL import Image, ImageFilter

# load image
image = Image.open("images/img2.jpeg")

# apply effect
blurImage = image.filter(ImageFilter.GaussianBlur(5))

# display image
blurImage.show()


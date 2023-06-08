from PIL import Image, ImageFilter

# load image
image = Image.open("images/img2.jpeg")

# apply effect using contour kernel
newImage = image.filter(ImageFilter.CONTOUR)

# display image
newImage.show()


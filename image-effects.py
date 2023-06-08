from PIL import Image, ImageFilter

# load image
image = Image.open("images/img2.jpeg")

# apply effect
blurImage0 = image.filter(ImageFilter.GaussianBlur(15))
blurImage1 = image.filter(ImageFilter.EDGE_ENHANCE)
blurImage2 = image.filter(ImageFilter.EMBOSS)
blurImage3 = image.filter(ImageFilter.CONTOUR)
blurImage4 = image.filter(ImageFilter.SHARPEN)
blurImage4.show()


# display image
image.show()

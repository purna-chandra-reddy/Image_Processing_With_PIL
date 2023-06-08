from PIL import Image

# load image
image = Image.open("images/Img1.jpg")
img2 = Image.open("images/img2.jpeg")
image.show()

# crop
box = (100,188,547,591)
croppedImg = image.crop(box)
croppedImg.show()

# paste
image.paste(croppedImg, (447, 400))
image.paste(img2, (0, 0))
image.paste(croppedImg, (0, 400))
image.show()
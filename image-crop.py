from PIL import Image

# load image
image = Image.open("images/img2.jpeg")
#image.show()

# crop
box = (100,5,547,450)
croppedImg = image.crop(box)
croppedImg.show()


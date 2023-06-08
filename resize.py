# # Import module
# from PIL import Image
#
# # Load image from disk
# im = Image.open("images/img2.jpeg")
#
# # Resize image
# im1 = im.resize(800,800)
#
# # Show image
# im1.show()


# Importing Image class from PIL module
from PIL import Image

# Opens a image in RGB mode
im = Image.open(r"images/img2.jpeg")

# Size of the image in pixels (size of original image)
# (This is not mandatory)
width, height = im.size

# Setting the points for cropped image
left = 4
top = height / 5
right = 154
bottom = 3 * height / 5

# Cropped image of above dimension
# (It will not change original image)
im1 = im.crop((left, top, right, bottom))
newsize = (900, 900)
im1 = im1.resize(newsize)
# Shows the image in image viewer
im1.show()

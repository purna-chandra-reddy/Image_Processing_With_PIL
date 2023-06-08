# Load PIL
from PIL import Image, ImageFont, ImageDraw  
      
# Load image and create image object  
image = Image.open('images/img2.jpeg')

# Draw object on image
draw = ImageDraw.Draw(image)  

# Load font (Check Path on your computer)
font = ImageFont.truetype(r'/Users/purnareddy/Downloads/downloads_chrome/python/pers_projects/Playwright-Jest-Test-Automation-Framework-master/node_modules/playwright/lib/web/traceViewer/40e1017745522c215602cd4956e7f6f4.ttf', 20)

# Text to write on image
text = 'YS JAGAN FOLLOWER'
  
# Add text to image
draw.text((5, 5), text, font = font, align ="left")

# Show image
image.show()

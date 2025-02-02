from PIL import Image, ImageDraw, ImageFont
import numpy as np
import matplotlib.pyplot as plt

font_path = "alagard.ttf"
font_size = 32
font = ImageFont.truetype(font_path, font_size)

# Text to render
text = "abcdefg"

# Create a blank image large enough to fit the text
img = Image.new('L', (font_size * len(text), font_size), color=255) # 'L' is for 8-bit pixels, white background
draw = ImageDraw.Draw(img)

# Draw text onto image
draw.text((0, 0), text, font=font, fill=0) # Black text

# Convert image to numpy array for pixel grid processing
pixel_data = np.array(img)

# Plot the pixelated text
plt.figure(figsize=(len(text), 1.5))
plt.imshow(pixel_data, cmap='gray_r')
plt.axis('off')
plt.show()
         
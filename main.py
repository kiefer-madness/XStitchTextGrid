from PIL import Image, ImageDraw, ImageFont
import numpy as np
import matplotlib.pyplot as plt

# Dictionary to hold each font's best font_size for pixel grid
font_sizes = {
    "alagard": 16,
}

font_name = "alagard"
font_path = f"fonts/{font_name}.ttf"
font_size = font_sizes[font_name]
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

# Get image dimensions
height, width = pixel_data.shape

# Plot the pixelated text with a grid overlay
fig, ax = plt.subplots(figsize=(width / 10, height / 10))
ax.imshow(pixel_data, cmap='gray')

# Draw gridlines
ax.set_xticks(np.arange(-0.5, width, 1), minor=True)
ax.set_yticks(np.arange(-0.5, height, 1), minor=True)
ax.grid(which='minor', color='gray', linestyle='-', linewidth=0.5)

# Show pixel coordinates for counting
ax.set_xticks(np.arange(0, width, 1))
ax.set_yticks(np.arange(0, height, 1))
ax.set_xticklabels(np.arange(0, width, 1), fontsize=8)
ax.set_yticklabels(np.arange(0, height, 1), fontsize=8)

plt.show()
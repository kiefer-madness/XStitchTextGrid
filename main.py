from PIL import Image, ImageDraw, ImageFont
import numpy as np
import matplotlib.pyplot as plt

# Dictionary to hold each font's best font_size for pixel grid
font_sizes = {
    "addstandard.ttf": 9,
    "alagard.ttf": 16,
    "alkhemikal.ttf": 16,
    "birchleaf.ttf": 16,
    "cavalhatriz.ttf": 16,
    "cooper.ttf": 16,
    "cursive.ttf": 17,
    "daydream.ttf": 10.5,
    "digicastle.ttf": 18,
    "digitaldisco.ttf": 16,
    "enchantedsword.ttf": 16,
    "finalfantasy.ttf": 8,
    "fipps.otf": 8,
    "gothic.ttf": 16,
    "gothic2.ttf": 16,
    "grapesoda.ttf": 16,
    "icepixel.ttf": 20,
    "kiwisoda.ttf": 16,
    "kuchibue.ttf": 16,
    "mario64.ttf": 12,
    "microserif.ttf": 10,
    "minecraft.ttf": 8,
    #"mleitod.ttf": 14,
    "nokia.ttf": 8,
    "notepen.ttf": 16,
    "pixelcowboy.otf": 8,
    "pixeledenglish.ttf": 16,
    "pixellove.ttf": 8,
    #"pixelout.ttf": 28,
    "pixelpoiiz.ttf": 10,
    "primusscript.ttf": 10,
    "runescape.ttf": 16,
    "typecast.ttf": 16,
    "typecast-bold.ttf": 16,
    "typecast-italic.ttf": 16,
    "veniceclassic.ttf": 19,
    "verminvibes.ttf": 16,
    "windows_command_prompt.ttf": 16,
}

font_name = "typecast-italic.ttf"
font_path = f"fonts/{font_name}"
font_size = font_sizes[font_name]
font = ImageFont.truetype(font_path, font_size)
font_line_spacing = 50

# Text to render
text = """hey lil mama"""

# Canvas size
img_width = 100
img_height = 100

# Create a blank image large enough to fit the text
img = Image.new('RGBA', (img_width, img_height), color=(255, 255, 255, 255))  # White background with alpha
draw = ImageDraw.Draw(img)

# Get image dimensions
width, height = img.size

# Find the center pixel
center_x, center_y = width // 2, height // 2

# Draw transparent red crosshairs
red_transparent = (255, 0, 0, 128)  # Red with 50% transparency

# Draw vertical and horizontal lines using pixel-perfect positions
for y in range(height):
    img.putpixel((center_x, y), red_transparent)
for x in range(width):
    img.putpixel((x, center_y), red_transparent)

# Split text into lines
lines = text.split("\n")

# Get text size for each line, determine total height
line_heights = [font.getbbox(line)[3] - font.getbbox(line)[1] for line in lines]
total_text_height = sum(line_heights) + (len(lines) - 1) * font_line_spacing

# Get y offset to center vertically
y_start = (img_height - total_text_height) // 2

# Track the min/max x positions for labeling
min_x = img_width
max_x = 0

# Now draw text
for i, line in enumerate(lines):
    bbox = font.getbbox(line)
    text_width = bbox[2] - bbox[0]

    x_offset = (img_width - text_width) // 2
    y_offset = y_start + sum(line_heights[:i]) + i * font_line_spacing

    draw.text((x_offset, y_offset), line, font=font, fill=(0, 0, 0, 255))  # Black text on top

    # Track the min/max x positions for labeling
    min_x = min(min_x, x_offset)
    max_x = max(max_x, x_offset + text_width)

# Convert to numpy array for pixel grid processing
pixel_data = np.array(img)

# Plot the image with grid overlay
fig, ax = plt.subplots(figsize=(width / 10, height / 10))
ax.imshow(pixel_data)

# Draw gridlines
ax.set_xticks(np.arange(-0.5, width, 1), minor=True)
ax.set_yticks(np.arange(-0.5, height, 1), minor=True)
ax.grid(which='minor', color='gray', linestyle='-', linewidth=0.5)

# Limit tick labels only to where the text begins
xticks = np.arange(min_x, max_x, 1)
yticks = np.arange(y_start, y_start + total_text_height, 1)

# Show pixel coordinates for counting
ax.set_xticks(xticks)
ax.set_yticks(yticks)
ax.set_xticklabels(xticks, fontsize=8)
ax.set_yticklabels(yticks, fontsize=8)

plt.show()

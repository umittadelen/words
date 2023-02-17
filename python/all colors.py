from PIL import Image

# Size of the image
width, height = 40960, 40960

# Create a new transparent image
img = Image.new("RGBA", (width, height), (0, 0, 0, 0))

# Iterate through all possible RGBA color tones
for r in range(256):
  for g in range(256):
    for b in range(256):
      for a in range(256):
        # Set the pixel color with the given transparency
        print(f"r:{r} g:{g} b:{b} a:{a}")
        img.putpixel((r, g), (r, g, b, int(255 * (a / 100))))

# Save the image to the desktop
img.save("../rgba_colors.png")
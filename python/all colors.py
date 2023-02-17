from PIL import Image

# Size of the image
width, height = 40960, 40960

# Create a new transparent image
img = Image.new("RGBA", (width, height), (0, 0, 0, 0))

# Iterate through all possible RGBA color tones and alpha values
for x in range(width):
  for y in range(height):
    for r in range(256):
      for g in range(256):
        for b in range(256):
          for a in range(256):
            # Set the pixel color with the given transparency
            print(f"x:{x} y:{y} r:{r} g:{g} b:{b} a:{a}")
            img.putpixel((x, y), (r, g, b, a))

# Save the image to the desktop
img.save("../rgba_colors.png")

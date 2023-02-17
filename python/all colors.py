from PIL import Image

a,r,g,b,x,y = 0,0,0,0,0,0
# Size of the image
width, height = 65536, 65536

# Create a new transparent image
img = Image.new("RGBA", (width, height), (0, 0, 0, 0))

# Iterate through all possible RGBA color tones and alpha values
for a in range(256):
  for r in range(256):
    for g in range(256):
      for b in range(256):
        # Set the pixel color with the given transparency
        x += 1
        if x >= height:
          x = 0
          y += 1
          if y > width:
            y = width
        print(f"x:{x}\ty:{y}\tr:{r}\tg:{g}\tb:{b}\ta:{a}")
        img.putpixel((x, y), (r, g, b, a))

# Save the image to the desktop
img.save("D:/all colors/rgba_colors.png")

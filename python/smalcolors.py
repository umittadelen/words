from PIL import Image

r,g,b,x,y = 0,0,0,0,0
# Size of the image
width, height = 1001, 1001

# Create a new transparent image
img = Image.new("RGB", (width, height), (0, 0, 0))

# Iterate through all possible RGBA color tones and alpha values
for r in range(100):
    for g in range(100):
        for b in range(100):
        # Set the pixel color with the given transparency
            x += 1
            if x >= height:
                x = 0
                y += 1
                if y > width:
                    y = width
            print(f"x:{x}\ty:{y}\tr:{r}\tg:{g}\tb:{b}")
            img.putpixel((x, y), (r, g, b))

# Save the image to the desktop
img.save("D:/all colors/rgba_colors.png")
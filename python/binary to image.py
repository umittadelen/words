# ↓↓ IMPORTING PACKAGES AND CHECKING PIP AND PIL PACKAGE ↓↓

import os,math,importlib.util

try:
  from PIL import Image
except:
  err = [1,"pillow"]
else:
  err = [0,""]

if err[0] == 1:
  if importlib.util.find_spec("pip") is None:
    os.system("py -m ensurepip --upgrade")
  os.system(f"pip install {err[1]}")

# ↓↓ MAIN CODE ↓↓ #

def message_to_image(message):
  # Split the message into a list of characters
  message_chars = list(message)

  # Convert the characters to binary strings and append a period to each
  binary_chars = []
  for char in message_chars:
    binary_char = format(ord(char), 'b') + '.'
    binary_chars.append(binary_char)

  # Join the binary characters into a single string
  binary_string = ''.join(binary_chars)

  # Convert the binary digits and periods to integers
  pixels = [int(x) if x != '.' else 255 for x in binary_string]
  # Determine the size of the image
  width = int(math.sqrt(len(pixels)))
  height = int(math.ceil(len(pixels) / width))

  # Create an image with a white background
  image = Image.new('RGB', (width, height), (0,255,0))
  a = 0
  for i in pixels:
    if i == 1:
      pixels[a] = (0,0,0)
    if i == 0:
      pixels[a] = (255,255,255)
    if i == 255:
      pixels[a] = (255,0,0)
    a += 1
  # Set the pixel values
  image.putdata(pixels)
  return image

def image_to_message(image_file):
  # Open the image
  try:
    image = Image.open(image_file)
    dots = list(image.getdata())
    readded_bin_list = []
    temp = ""
    result = []
    text_result = []
    output = ""
    for i in dots:
      if i == (0, 0, 0):
        readded_bin_list.append(1)
      if i == (255, 255, 255):
        readded_bin_list.append(0)
      if i == (255, 0, 0):
        readded_bin_list.append(" ")
    for x in readded_bin_list:
        if x == " ":
            result.append(temp)
            temp = ""
        else:
          temp += str(x)
    result.append(temp)
    del result[-1]
    text_result = [chr(int(s, 2)) for s in result]
    output = ''.join(text_result)
    return output
    
  except:
    print("image not found")
    return ""
  
loop = 1
while True:
  # Test the encoder
  os.system("cls")
  answer = input("\033[1m \033[1;31;40mencode, decode or exit > \033[0;0m\033[1;34;40m")
  print("\033[0;0m")

  if answer == "encode":
    message = input("\033[1m \033[1;33;40menter text> \033[0;0m\033[1;36;40m")
    print("\033[0;0m")
    image = message_to_image(message)
    image.save(f'C:/Users/{os.getlogin( )}/Desktop/binary_image.png')
    image.show()

  elif answer == "decode":
    print("\033[92m" + image_to_message(f'C:/Users/{os.getlogin( )}/Desktop/binary_image.png') + "\033[0;0m\n")

  elif answer == "exit":
    os._exit(0)

  else:
    print("\033[1m \033[1;32;40myou can enter (encode, decode, exit)\033[0;0m\n")

  input("\033[1m \033[1;33;40mpress ENTER to return to the main menu\033[0;0m")
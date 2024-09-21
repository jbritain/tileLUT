source_image = "sourceImage.png"
target_image = "targetImage.bin"

channels = 2 # 1 means you only get the first channel i.e the R. 4 would get you RGBA

from PIL import Image

source = Image.open(source_image).convert()
tile_size = min(source.size)
horizontal = source.size[0] > source.size[1] # whether the tiles are vertical or horizontal

# maps an xyz coordinate to xy in the image and gets the value at that position
def get_source_colour(x, y, z):
  if horizontal:
    return source.getpixel((x + z * tile_size, y))

  return source.getpixel((x, y + tile_size * z))

byte_data = [] # list of bytes to write

# read bytes from image
for z in range(tile_size):
  for y in range(tile_size):
    for x in range(tile_size):
      colour = get_source_colour(x, y, z)

      for c in colour[0:channels]:
        byte_data.append(c)

# write bytes to LUT
with open(target_image, "wb+") as target:
  target.write(bytes(byte_data))
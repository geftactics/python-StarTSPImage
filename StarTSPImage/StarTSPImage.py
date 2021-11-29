import PIL.ImageOps
from PIL import Image


def buildRaster(img, cut=True):

  bytes_per_line = 72

  # Convert image to greyscale and resize to max width
  basewidth = bytes_per_line * 8
  wpercent = (basewidth / float(img.width))
  hsize = int((float(img.height) * float(wpercent)))
  img = PIL.ImageOps.invert(img.convert('RGB'))
  img = img.convert(mode='1', dither=Image.FLOYDSTEINBERG).resize((basewidth, hsize))

  # PIL mode 1 image (1-bit pixels, black and white, one pixel per byte)
  bytesarray = bytes(img.tobytes())

  # Start our raster image
  buf = []
  buf.extend([0x1b, ord('*'), ord('r'), ord('A')])                  # Enter raster mode
  buf.extend([0x1b, ord('*'), ord('r'), ord('P'), ord('0'), 0x00])  # continuous mode

  # Handle cuts
  if not cut:
      buf.extend([0x1b, ord('*'), ord('r'), ord('E'), ord('1'), 0x00]) # Raster EOT no-cut

  # Loop over bytes array, adding a transfer data command for each line
  # followed by the amount of bytes that make up a line
  byte = 0
  for line in range(img.height):
    line_bytes = [ord('b'), bytes_per_line, 0] # Transfer of raster data
    for b in range(bytes_per_line):
      line_bytes.append(bytesarray[byte])
      byte += 1
    buf.extend(line_bytes)

  buf.extend([0x1b, ord('*'), ord('r'), ord('B')]) # Quit raster mode

  return bytearray(buf)


def imageToRaster(img, cut=True):
  return buildRaster(img, cut)


def imageFileToRaster(image_path, cut=True):
  img = Image.open(image_path)
  return buildRaster(img, cut)

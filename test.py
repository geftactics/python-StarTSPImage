import StarTSPImage
from PIL import Image, ImageDraw

image = Image.new('RGB', (500, 500), color='White')
draw = ImageDraw.Draw(image)
draw.ellipse((0, 0, 500, 500), fill='Black')
draw.ellipse((10, 10, 490, 490), fill='White')

raster = StarTSPImage.imageToRaster(image, cut=True)

printer = open('/dev/usb/lp0', "wb")
printer.write(raster)
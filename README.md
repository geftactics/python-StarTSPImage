# python-StarTSP100

The Star TSP100 / TSP143 printers do not support Star line mode commands natively, these are usually provided by a driver performing some kind of emulation. As such, it's not possible to simply send text to the appropriate `/dev` point, because these printers only support Star graphic mode.

You can find the graphic mode commands here: http://www.starasia.com/Download/Manual/star_graphic_cm_en.pdf

This project will take an image file (Any format that Pythons Pillow library can open), resize it to the appropriate width for the printer, and then create a binary output of the raster commands, which can be send directly to the device.

To get started simply: `python3 StarTSP100.py > /dev/usb/lp0` (Replacing with the appropriate dev path)

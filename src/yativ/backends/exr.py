import sys

import OpenEXR
import numpy
import Imath

from yativ.colorspaces import srgb


def supported(path):
    return OpenEXR.isOpenExrFile(path)


def getPixels(path):
    image = OpenEXR.InputFile(path)
    header = image.header()
    pt = Imath.PixelType(Imath.PixelType.FLOAT)
    dw = header['dataWindow']
    x, y = (dw.max.x - dw.min.x + 1, dw.max.y - dw.min.y + 1)

    im = numpy.zeros((x,y,3))
    im[:,:,0] = numpy.frombuffer(image.channel('R', pt), dtype=numpy.float32).reshape((x,y))
    im[:,:,1] = numpy.frombuffer(image.channel('G', pt), dtype=numpy.float32).reshape((x,y))
    im[:,:,2] = numpy.frombuffer(image.channel('B', pt), dtype=numpy.float32).reshape((x,y))

    im = numpy.clip(im, 0, 1)
    return srgb.to(im), x, y

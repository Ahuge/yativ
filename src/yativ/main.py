import os
import sys
# TODO: use argparse
import argparse

import numpy

from yativ import exceptions, terminal_utils, backends

def extension_loader(path):
    ext = os.path.splitext(path)[-1]
    plugin = __import__("yativ.backends%s" % ext, globals(), locals(), ["supported", "getPixels"])
    if plugin.supported(path):
        return plugin.getPixels(path)
    else:
        for filename in os.listdir(os.path.join(os.path.dirname(__file__), "backends")):
            ext = os.path.splitext(filename)[-1]
            plugin = __import__("yativ.backends%s" % ext, globals(), locals(), ["supported", "getPixels"])
            if plugin.supported(path):
                return plugin.getPixels(path)
    return exceptions.UnknownImagePathError("Unable to load backend for %s" % path)


def display_image(path):
    try:
        matrix, x, y = extension_loader(path)
    except exceptions.UnknownImagePathError as err:
        import traceback
        traceback.print_exc()
        sys.exit(1)
    
    red = matrix[:,:,0]
    green = matrix[:,:,1]
    blue = matrix[:,:,2]

    for xindex in range(x):
        for yindex in range(y):
            rpix = red[xindex, yindex]
            gpix = green[xindex, yindex]
            bpix = blue[xindex, yindex]
            number = terminal_utils.rgbTupleToANSIColor(rpix, gpix, bpix)

            sys.stdout.write(u"\u001b[48;5;{num}m  \u001b[0m".format(num=number))
        sys.stdout.write(u"\n")

if __name__ == "__main__":
    path = sys.argv[1]
    display_image(path)

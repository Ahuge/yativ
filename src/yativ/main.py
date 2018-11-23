import os
import sys
# TODO: use argparse
import argparse

import numpy

from yativ import exceptions, terminal_utils, backends, scale

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

def display_image(path, size=32):
    try:
        matrix, x, y = extension_loader(path)
    except exceptions.UnknownImagePathError as err:
        import traceback
        traceback.print_exc()
        sys.exit(1)

    factor = 1

    if size:
        factor = x/float(size)
        x = size
        y = int(y / factor)

    # print("Factor: %s" % factor)
    red = scale.scale(matrix[:,:,0], factor)
    green = scale.scale(matrix[:,:,1], factor)
    blue = scale.scale(matrix[:,:,2], factor)
    # print(red.shape)

    for xindex in range(x):
        for yindex in range(int(y)):
            rpix = red[xindex, yindex]
            gpix = green[xindex, yindex]
            bpix = blue[xindex, yindex]
            ansi = terminal_utils.ansi_code(rpix, gpix, bpix)
            sys.stdout.write(ansi + u"  \033[0m")
            # sys.stdout.write(u"\u001b[48;5;{num}m  \u001b[0m".format(num=number))
        sys.stdout.write(u"\n")


def write_image(path, output="/var/tmp/imageout.txt"):
    o_out = sys.stdout
    import cStringIO
    virtualout = cStringIO.StringIO()
    sys.stdout = virtualout

    display_image(path)
    sys.stdout = o_out
    virtualout.seek(0)
    with open(output, "wb") as fh:
        fh.write(virtualout.read())
    return virtualout


if __name__ == "__main__":
    path = sys.argv[1]
    display_image(path)

import sys
# TODO: use argparse
import argparse

import numpy
import terminal_utils


if __name__ == "__main__":
    path = sys.argv[1]
    matrix, x, y = getPixelsSRGB(path)
    
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

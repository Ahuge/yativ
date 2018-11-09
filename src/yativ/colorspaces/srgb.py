import numpy

def to(val):
    return val * 12.92 if val <= 0.0031308 else 1.055 * val**(1.0/2.4) - 0.055

to = numpy.vectorize(toSRGB)

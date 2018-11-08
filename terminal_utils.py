import hexColorSupport

def color256():
    # TODO: test
    return True

def colorTrue():
    # TODO: test
    return False

def rgbTupleToANSIColor(r, g, b):
    if colorTrue():
        raise NotImplementedError("Ack!")
    elif color256():
        hex_r = int(rpix * 256)
        hex_g = int(gpix * 256)
        hex_b = int(bpix * 256)
        hex_color = "%02x%02x%02x" % (hex_r, hex_g, hex_b)
        number, hexc = hexColorSupport.rgb2short(hex_color)
    else:
        raise EnvironmentError("Terminal supports no colors?")
    return number

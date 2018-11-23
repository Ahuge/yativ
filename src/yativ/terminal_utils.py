import hexColorSupport

def color256():
    # TODO: test
    return True

def colorTrue():
    # TODO: test
    return False
    # return True


def ansi_code(r, g, b):
    hex_r = int(rpix * 256)
    hex_g = int(gpix * 256)
    hex_b = int(bpix * 256)
    if colorTrue():
        return u"\u001b[48;2;%s;%s;%s" % (hex_r, hex_g, hex_b)
    elif color256():
        hex_color = "%02x%02x%02x" % (hex_r, hex_g, hex_b)
        number, hexc = hexColorSupport.rgb2short(hex_color)
        return u"\u001b[48;5;{num}m  \u001b[0m".format(num=number)


def rgbTupleToANSIColor(r, g, b):
    if colorTrue():
        return "%s;%s;%s" % (int(r*256), int(g*256), int(b*256))
        raise NotImplementedError("Ack!")
    elif color256():
        hex_r = int(r * 256)
        hex_g = int(g * 256)
        hex_b = int(b * 256)
        hex_color = "%02x%02x%02x" % (hex_r, hex_g, hex_b)
        number, hexc = hexColorSupport.rgb2short(hex_color)
    else:
        raise EnvironmentError("Terminal supports no colors?")
    return number

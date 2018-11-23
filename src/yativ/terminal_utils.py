import hexColorSupport

def color256():
    # TODO: test
    return True

def colorTrue():
    # TODO: test
    return False
    # return True


def ansi_code(r, g, b):
    hr = int(r*256)
    hg = int(r*256)
    hb = int(b*256)
    if colorTrue():
        return u"\x1b[48;2;%s;%s;%s" % (hr, hg, hb)
    elif color256():
        hex_color = "%02x%02x%02x" % (hr, hg, hb)
        number, hexc = hexColorSupport.rgb2short(hex_color)
        return u"\x1b[48;5;%sm" % number


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

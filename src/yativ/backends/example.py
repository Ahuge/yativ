def supported(path):
    """Takes a path, returns a bool of if this plugin supports it."""
    return False


def getPixels(path):
    """Takes a path, returns a tuple:
            np 3d array: pixels for RGB
            int: x width
            int: y height
    """

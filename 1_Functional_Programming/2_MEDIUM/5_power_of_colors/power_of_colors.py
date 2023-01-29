import random

random.seed(3)


def random_hex_colors():
    return "#" + str(hex(random.randint(0, 16777215)))[2:]


def random_rgb_colors():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)


def convert_colors(color):
    if isinstance(color, tuple):
        for channel in color:
            if 0 <= channel <= 255:
                return "#" + "".join([hex(channel)[2:].zfill(2) for channel in color])
            return "Incorrect input value."
    elif isinstance(color, str) and len(color) == 7 and color.startswith("#"):
        return (int(color[1:3], 16), int(color[3:5], 16), int(color[5:], 16))
    return "Incorrect input value."

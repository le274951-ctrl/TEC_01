def hex_color(color):
    if len(color) != 7:
        return False

    if color[0] != "#":
        return False

    if not all(c in "0123456789ABCDEFabcdef" for c in color[1:]):
        return False

    return True


color = input("Enter hex color: ")
print(hex_color(color))
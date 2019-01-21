def xo(str):
    if str.count("x") == str.count("o"):
        return True
    else:
        return False

print(xo("xoxoxo"))
print(xo("oxooxo"))
print(xo("oxo"))
print(xo("xxxooo"))
print(xo("xoxooxxo"))
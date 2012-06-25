def build_palette(filename):
    """
        legacy function to build a palette object from an image like
        this one: http://alexander-jenkins.co.uk/blog/?p=9
    """
    from PIL import Image
    img = Image.open(filename)
    x_offset, y_offset = 6, 6
    tile_width, tile_height = 28, 22

    palette = {}
    for tile_y in xrange(16):
        for tile_x in xrange(16):
            x, y = tile_x * tile_width + x_offset, tile_y * tile_height + y_offset
            palette[tile_y * 16 + tile_x] = img.getpixel((x, y))

    return palette

# but in most cases, this should be enough
AOE1_PALETTE = {0: (0, 0, 0),
 1: (128, 0, 0),
 2: (0, 128, 0),
 3: (128, 128, 0),
 4: (0, 0, 128),
 5: (128, 0, 128),
 6: (0, 128, 128),
 7: (192, 192, 192),
 8: (192, 220, 192),
 9: (166, 202, 240),
 10: (163, 0, 255),
 11: (195, 0, 255),
 12: (227, 0, 255),
 13: (255, 0, 243),
 14: (255, 0, 210),
 15: (255, 0, 178),
 16: (227, 247, 255),
 17: (187, 215, 235),
 18: (147, 187, 215),
 19: (115, 155, 199),
 20: (87, 123, 179),
 21: (63, 95, 159),
 22: (39, 63, 143),
 23: (23, 39, 123),
 24: (7, 15, 103),
 25: (0, 0, 87),
 26: (255, 255, 243),
 27: (255, 255, 119),
 28: (255, 255, 79),
 29: (255, 255, 39),
 30: (254, 254, 0),
 31: (199, 199, 0),
 32: (255, 239, 239),
 33: (255, 191, 191),
 34: (255, 143, 143),
 35: (255, 95, 95),
 36: (255, 47, 47),
 37: (227, 11, 0),
 38: (199, 23, 0),
 39: (143, 31, 0),
 40: (111, 11, 7),
 41: (83, 11, 0),
 42: (171, 171, 0),
 43: (147, 147, 0),
 44: (119, 119, 0),
 45: (91, 91, 0),
 46: (63, 63, 0),
 47: (35, 35, 0),
 48: (255, 255, 199),
 49: (255, 255, 159),
 50: (255, 255, 0),
 51: (227, 227, 0),
 52: (223, 207, 15),
 53: (195, 163, 27),
 54: (163, 115, 23),
 55: (135, 103, 39),
 56: (107, 75, 39),
 57: (79, 55, 35),
 58: (11, 11, 0),
 59: (243, 255, 243),
 60: (211, 255, 191),
 61: (207, 255, 143),
 62: (155, 255, 95),
 63: (87, 255, 47),
 64: (243, 219, 187),
 65: (231, 195, 115),
 66: (207, 163, 67),
 67: (183, 139, 43),
 68: (163, 115, 79),
 69: (139, 91, 55),
 70: (115, 71, 39),
 71: (95, 51, 27),
 72: (63, 55, 35),
 73: (35, 35, 31),
 74: (0, 255, 0),
 75: (0, 231, 23),
 76: (0, 211, 39),
 77: (0, 187, 55),
 78: (0, 167, 67),
 79: (0, 143, 71),
 80: (255, 219, 179),
 81: (255, 195, 111),
 82: (251, 159, 31),
 83: (247, 139, 23),
 84: (243, 119, 15),
 85: (239, 99, 7),
 86: (207, 67, 0),
 87: (159, 51, 0),
 88: (135, 43, 0),
 89: (111, 35, 0),
 90: (0, 123, 75),
 91: (0, 103, 99),
 92: (0, 55, 83),
 93: (0, 19, 63),
 94: (0, 0, 43),
 95: (255, 247, 235),
 96: (175, 207, 147),
 97: (155, 183, 111),
 98: (139, 159, 79),
 99: (127, 139, 55),
 100: (99, 123, 47),
 101: (75, 107, 43),
 102: (55, 95, 39),
 103: (27, 67, 27),
 104: (19, 51, 19),
 105: (11, 27, 11),
 106: (247, 235, 215),
 107: (239, 219, 195),
 108: (231, 207, 175),
 109: (223, 195, 159),
 110: (215, 183, 143),
 111: (211, 171, 127),
 112: (254, 254, 254),
 113: (235, 235, 235),
 114: (219, 219, 219),
 115: (199, 199, 199),
 116: (179, 179, 179),
 117: (143, 143, 143),
 118: (107, 107, 107),
 119: (71, 71, 71),
 120: (55, 55, 55),
 121: (35, 35, 35),
 122: (187, 143, 99),
 123: (78, 55, 35),
 124: (47, 47, 35),
 125: (255, 251, 247),
 126: (235, 227, 219),
 127: (219, 207, 195),
 128: (235, 255, 239),
 129: (159, 231, 187),
 130: (95, 211, 159),
 131: (43, 191, 147),
 132: (0, 171, 147),
 133: (0, 131, 123),
 134: (0, 111, 107),
 135: (0, 79, 79),
 136: (0, 63, 67),
 137: (0, 35, 39),
 138: (199, 183, 175),
 139: (183, 163, 151),
 140: (163, 143, 131),
 141: (147, 123, 111),
 142: (127, 103, 95),
 143: (111, 87, 79),
 144: (107, 79, 71),
 145: (103, 75, 63),
 146: (99, 71, 59),
 147: (95, 67, 55),
 148: (91, 63, 47),
 149: (87, 59, 43),
 150: (83, 59, 39),
 151: (255, 1, 1),
 152: (171, 31, 0),
 153: (115, 35, 0),
 154: (99, 23, 0),
 155: (67, 7, 0),
 156: (51, 0, 0),
 157: (35, 0, 0),
 158: (243, 243, 255),
 159: (219, 219, 243),
 160: (199, 199, 231),
 161: (179, 183, 223),
 162: (159, 167, 211),
 163: (143, 151, 203),
 164: (127, 131, 183),
 165: (115, 119, 167),
 166: (99, 103, 151),
 167: (87, 87, 135),
 168: (75, 75, 119),
 169: (51, 51, 99),
 170: (31, 31, 83),
 171: (15, 15, 63),
 172: (7, 7, 47),
 173: (0, 0, 31),
 174: (255, 235, 215),
 175: (255, 203, 143),
 176: (255, 183, 75),
 177: (255, 179, 43),
 178: (235, 79, 0),
 179: (183, 59, 0),
 180: (203, 231, 187),
 181: (39, 79, 31),
 182: (15, 39, 15),
 183: (163, 163, 163),
 184: (127, 127, 127),
 185: (91, 91, 91),
 186: (15, 15, 15),
 187: (1, 1, 1),
 188: (255, 239, 219),
 189: (247, 223, 199),
 190: (239, 207, 179),
 191: (231, 187, 163),
 192: (223, 171, 147),
 193: (215, 151, 131),
 194: (207, 135, 115),
 195: (199, 115, 99),
 196: (191, 99, 87),
 197: (171, 71, 63),
 198: (151, 47, 39),
 199: (131, 27, 23),
 200: (95, 0, 0),
 201: (251, 247, 243),
 202: (247, 231, 215),
 203: (239, 207, 163),
 204: (235, 199, 139),
 205: (231, 191, 95),
 206: (139, 95, 11),
 207: (119, 75, 0),
 208: (255, 0, 247),
 209: (255, 0, 227),
 210: (255, 0, 211),
 211: (255, 0, 195),
 212: (255, 0, 179),
 213: (255, 0, 163),
 214: (255, 0, 147),
 215: (255, 0, 131),
 216: (255, 0, 115),
 217: (255, 0, 95),
 218: (255, 0, 79),
 219: (255, 0, 63),
 220: (255, 0, 47),
 221: (255, 0, 31),
 222: (255, 0, 15),
 223: (255, 0, 0),
 224: (251, 251, 251),
 225: (247, 243, 235),
 226: (247, 239, 227),
 227: (243, 235, 215),
 228: (243, 231, 207),
 229: (243, 227, 195),
 230: (243, 219, 183),
 231: (247, 215, 175),
 232: (247, 207, 163),
 233: (251, 199, 151),
 234: (255, 191, 143),
 235: (227, 171, 127),
 236: (203, 151, 111),
 237: (175, 131, 95),
 238: (151, 111, 79),
 239: (127, 95, 67),
 240: (167, 131, 35),
 241: (0, 151, 135),
 242: (0, 95, 95),
 243: (0, 47, 51),
 244: (2, 2, 2),
 245: (253, 253, 253),
 246: (255, 251, 240),
 247: (160, 160, 164),
 248: (39, 63, 144),
 249: (63, 95, 159),
 250: (87, 123, 180),
 251: (63, 95, 160),
 252: (39, 63, 145),
 253: (23, 39, 123),
 254: (23, 39, 124),
 255: (255, 255, 255)}


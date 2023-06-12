import random
import trmnl_colors as clr
color_map = {
    0: clr.greyD, 1: clr.greyB, 2: clr.greyL, 3: clr.greyI, 4: clr.greyU, 5: clr.greyS,
    6: clr.redD, 7: clr.redB, 8: clr.redL, 9: clr.redI, 10: clr.redU, 11: clr.redS,
    12: clr.greenD, 13: clr.greenB, 14: clr.greenL, 15: clr.greenI, 16: clr.greenU, 17: clr.greenS,
    18: clr.yellowD, 19: clr.yellowB, 20: clr.yellowL, 21: clr.yellowI, 22: clr.yellowU, 23: clr.yellowS,
    24: clr.blueD, 25: clr.blueB, 26: clr.blueL, 27: clr.blueI, 28: clr.blueU, 29: clr.blueS,
    30: clr.magentaD, 31: clr.magentaB, 32: clr.magentaL, 33: clr.magentaI, 34: clr.magentaU, 35: clr.magentaS,
    36: clr.cyanD, 37: clr.cyanB, 38: clr.cyanL, 39: clr.cyanI, 40: clr.cyanU, 41: clr.cyanS,
    42: clr.greyD, 43: clr.greyB, 44: clr.greyL, 45: clr.greyI, 46: clr.greyU, 47: clr.greyS,
    48: clr.blackbg, 49: clr.redbg, 50: clr.greenbg, 51: clr.yellowbg, 52: clr.bluebg,
    53: clr.magentabg, 54: clr.cyanbg, 55: clr.whitebg, 56: clr.greybg
}

nums = list(color_map.keys())

# color_map[random.choice(bg_disabled_keys)]()
# print(color_map[random.choice(bg_disabled_keys)])
# clr.reset()
# Extract the method names as strings
method_names = [str(value.__name__) for value in color_map.values()]

# Sort the method names based on the desired order
sorted_method_names = sorted(
    method_names,
    key=lambda name: (
        name.endswith("bg"),
        name.endswith('D'),
        name.endswith('B'),
        name.endswith('L'),
        name.endswith('I'),
        name.endswith('U'),
        name.endswith('S')
    )
)

# Create a new dictionary with the sorted method names
sorted_color_map = {
    index: getattr(clr, name) for index, name in enumerate(sorted_method_names)
}
# print(sorted_color_map)
num2 = list(sorted_color_map.keys())
underline_disabled_keys = num2[0:11]+ num2[16:]

print(underline_disabled_keys)
import colorgram

# colorgram related variables and fns
colors_from_image = colorgram.extract('imagewa.jpg', 30)
list_of_rgbcolor_tuples = []

for i in range(30):
    color = colors_from_image[i].rgb
    r = color.r
    g = color.g
    b = color.b
    rgb_tuple = (r, g, b)
    list_of_rgbcolor_tuples.append(rgb_tuple)
print("Print and copy-paste all colors in a variable\n\n", list_of_rgbcolor_tuples)


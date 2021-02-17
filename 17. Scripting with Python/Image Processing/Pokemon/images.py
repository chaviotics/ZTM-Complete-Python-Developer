from PIL import Image, ImageFilter
# https://pillow.readthedocs.io/en/stable/ -> Read the documentation

# We can process multiple images at once

img = Image.open(r'.\Pokedex\pikachu.jpg')
filtered_img = img.filter(ImageFilter.GaussianBlur(3))

filtered_img.save("blur.png", 'png')

# filtered_img.show()

grey_img = img.convert('L')
grey_img.save("grey_img.png", 'png')

# grey_img.show()


# print(img)
# print(img.format)
# print(img.mode)
# print(img.size)

# print(dir(img)) # can be checked in the documentation

# for i in dir(img):
#     print(i)

# print(dir(ImageFilter))
from PIL import Image, ImageFilter

img = Image.open(r'17. Scripting with Python\Image Processing\astro.jpg')
# print(img.size)
# resize_img = img.resize((400,200))

img.thumbnail((400,400)) # keeps the aspect ratio
# resize_img.show()
img.show()

# resize_img.save('thumbnail.jpg')

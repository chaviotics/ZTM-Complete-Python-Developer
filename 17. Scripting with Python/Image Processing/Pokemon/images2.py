from PIL import Image, ImageFilter

img = Image.open(r'.\Pokedex\pikachu.jpg')
filtered_img = img.filter(ImageFilter.GaussianBlur(3))

filtered_img.save("blur.png", 'png') 

crook = filtered_img.rotate(0)
# crook.save("crook.png", 'png')

resize = img.resize((200,200))
# resize.save("SmallPikachu.png", 'png')

box = (100, 100, 400, 400)
region = img.crop(box)
region.save("facePikachu.png", "png")


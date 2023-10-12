from PIL import Image

mac = Image.open('Atmecs image.jpg')
print(type(mac))
mac.show()
print(mac.size)
print(mac.format_description)

# Cropping Images
width, height = mac.size

left = 5
top = height / 4
right = 164
bottom = 3 * height / 4

mac.crop((left, top, right, bottom))
mac.show()

pencils = Image.open("Pencils.jpg")
pencils.show()
print(pencils.size)

width, height = pencils.size

# Setting the points for cropped image
left = 5
top = height / 4
right = 164
bottom = 3 * height / 4
pencil = pencils.crop((left, top, right, bottom))
pencil.show()
pencils.paste(im=pencil, box=(0, 0))
pencils.show()
pencils.resize((3000, 5000))
pencils.show()
pencils.rotate(90)
pencils.show()
red = Image.open("Pencils.jpg")
red.putalpha(112)
red.show()
red.paste(im=pencil, box=(0, 0), mask= pencil)
red.show()

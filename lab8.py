'''from PIL import Image

img = Image.open("march.jpg")
img_cropped = img.crop((0, 100, 700, 320))
img_cropped.save("crop_march.jpg")


from PIL import Image
n = {1: "march.jpg", 2: "HNY.jpg", 3: "HB.jpg"}
print("1-8 марта", "2-новый год", "3-день рождения")
ans = int(input("Введите номер праздника из списка: "))
filename = n[ans]
with Image.open(filename) as img:
    img.load()
    img.show()'''


from PIL import Image, ImageDraw, ImageFont


name = input("Введите имя именинника: ")
filename = "HB.jpg"
with Image.open(filename) as img:
    img.load()
font = ImageFont.truetype("arial.ttf", 20)
draw_text = ImageDraw.Draw(img)
draw_text.text(
    (img.width // 2 - 100,15),
    name + ", поздравляю!",
    font=font,
    fill=("#000000")
)
img.show()
img.save(name + "nameHB.jpg")









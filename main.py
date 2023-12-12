from PIL import Image, ImageDraw, ImageFont
print('Добро пожаловать в генератор мемов')
text_type = int(input('Введите 1, если нужен только нижний текст, и 2, если и верхний , нижний: '))
top_text = ''
bottom_text = ''
if text_type == 1:
  bottom_text = input('Введите нижний текст: ')
elif text_type == 2:
  top_text = input('Введите верхний текст: ')
  bottom_text = input('Введите нижний текст: ')
else:
  print('Введен неправильный режим')
  quit()
print(top_text, bottom_text)
memes = ['Кот в ресторане.png', 'Кот в очках', 'Кот на пляже']
print('Выберите картинку: ')
for i in range(len(memes)):
    print(i, memes[i])
user_input = int(input('Введите номер картинки: '))
image = Image.open(memes[user_input])
width, height = image.size

draw = ImageDraw.Draw(image)

font = Image.truetype('arial.ttf', size=100)

text = draw.textbbox((0, 0), top_text, font)

text_bottom = draw.textbbox((0, 0), bottom_text, font)

draw.text(((width - text[2]) / 2, 10), top_text, font=font, fill='black')
y_bottom = height - text_bottom[3] - 5
draw.text(((width - text_bottom[2]) / 2, y_bottom), bottom_text, font=font, fill='black')

image.save("new_meme5.jpg")
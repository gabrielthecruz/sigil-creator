from PIL import Image, ImageDraw
import string
import math

LETTER_BOX = 101


def make_alphabet_table(columns, alphabet):
    center_box = math.ceil(LETTER_BOX / 2)
    alphabet_table = {}

    for index, letter in enumerate(alphabet):
        x = (index % columns) * LETTER_BOX + center_box
        y = math.floor(index / columns) * LETTER_BOX + center_box
        alphabet_table[letter] = (x, y)

    return alphabet_table


def draw_sigil(text, columns=4, alphabet=string.ascii_lowercase):
    img_height = LETTER_BOX * math.ceil(len(alphabet) / columns)
    img_width = LETTER_BOX * columns
    image = Image.new('RGB', (img_width, img_height), 'white')
    draw = ImageDraw.Draw(image)

    position_table = make_alphabet_table(columns, alphabet)
    text = text.lower().replace(' ', '')
    coords = [position_table[c] for c in dict.fromkeys(text).keys()]
    draw.line(coords, fill='black')
    image.save('Sigil_{}.png'.format(text))


if __name__ == '__main__':
    draw_sigil('example')

#!/usr/bin/env python3

import datetime
import json
import os
import random
import textwrap

from PIL import Image, ImageFont, ImageDraw


def get_random_words(lines):
    count = 0
    words = {}
    while 1:
        random_number = random.randint(0, len(lines) - 1)
        word = lines[random_number].split("-")[0].replace(" ", "")
        meaning = lines[random_number].split("-")[1].replace("\n", "")
        if word in open('seen-words.txt').read():
            continue
        words[word] = meaning
        count += 1
        if count == 10 or len(lines) - len(open('seen-words.txt').readlines()) < 10:
            break
    return words


def update_words(lines):
    today_words = {'words': get_random_words(lines)}
    today_words['last_updated'] = datetime.datetime.today().strftime("%Y-%m-%d")
    today_words['last_word'] = None
    with open('today-words.txt', 'w') as f1:
        f1.write(json.dumps(today_words))


def main():
    lines = open('vocab-list.txt').readlines()

    if os.stat("today-words.txt").st_size == 0:
        # For an empty file
        update_words(lines)

    if (json.loads(open('today-words.txt').read())).get('last_updated') != datetime.datetime.today().strftime("%Y-%m-%d"):
        # Update the set of words everyday
        update_words(lines)
    
    today_words = json.loads(open('today-words.txt').read())
    words = set(today_words.get('words').keys()) - {today_words.get('last_word')}
    current_word = random.sample(words, 1)[0]
    current_meaning = today_words['words'].get(current_word)
            
    # Editing the background image
    img = Image.open('sample.jpg')
    draw = ImageDraw.Draw(img)
    W, H = img.size  # Gets the width and height of our image

    font1 = ImageFont.truetype("RobotoCondensed-Bold.ttf", 96)  # Font for displaying the "WORD"
    w, h = draw.textsize(current_word)  # Size of the word
    draw.text(((W - w) / 2 - 150, (H - h) / 2 - 200), current_word, (255, 255, 255), font=font1)

    font2 = ImageFont.truetype("Aaargh.ttf", 80)
    current_meaning = textwrap.wrap(current_meaning, width=35)
    padding = 0
    for line in current_meaning:
        w, h = draw.textsize(str(line))
        draw.text(((W - w) / 2 - 600, (H - h) / 2 + padding), str(line), (255, 255, 255), font=font2)
        padding += 100
    img.save('wallpaper.jpg')

    today_words['last_word'] = current_word
    with open('today-words.txt', 'w') as f1:
        f1.write(json.dumps(today_words))


if __name__ == "__main__": main()

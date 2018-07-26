#!/usr/bin/env python3

import datetime
import json
import os
import random
import textwrap

from PIL import Image, ImageFont, ImageDraw


def prepare_empty_files(lines):
    if os.stat("seen-words.txt").st_size == 0:
        with open("seen-words.txt", 'w') as file:
            file.write(json.dumps({"words": []}))

    if os.stat("today-words.txt").st_size == 0:
        # For an empty file
        update_words(lines)


def get_random_words(lines):
    count = 0
    words = {}
    seen_words = json.loads(open('seen-words.txt').read()).get('words')
    while 1:
        random_number = random.randint(0, len(lines) - 1)
        word = lines[random_number].split("-")[0].replace(" ", "")
        word = word.lstrip()
        meaning = lines[random_number].split("-")[1].replace("\n", "")
        if word in seen_words:
            continue
        words[word] = meaning.lstrip()
        count += 1
        if count == 10 or len(lines) - len(seen_words) < 10:
            break
    return words


def move_words_to_seen():
    words = json.loads(open('today-words.txt').read()).get('words')
    words = list(words.keys())
    seen_words = json.loads(open('seen-words.txt').read())
    seen_words['words'] = seen_words.get('words') + words
    with open('seen-words.txt', 'w') as file:
        file.write(json.dumps(seen_words))


def update_words(lines):
    if not os.stat("today-words.txt").st_size == 0:
        move_words_to_seen()
    today_words = {'words': get_random_words(lines)}
    today_words['last_updated'] = datetime.datetime.today().strftime("%Y-%m-%d")
    today_words['last_word'] = None
    with open('today-words.txt', 'w') as f1:
        f1.write(json.dumps(today_words))


def edit_wallpaper(current_word, current_meaning):
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


def single_word_meaning():
    lines = open('vocab-list.txt').readlines()

    # Check if files are empty (today's words and seen words)
    prepare_empty_files(lines)

    if (json.loads(open('today-words.txt').read())).get('last_updated') != datetime.datetime.today().strftime(
            "%Y-%m-%d"):
        # Update the set of words everyday
        update_words(lines)

    today_words = json.loads(open('today-words.txt').read())
    words = set(today_words.get('words').keys()) - {today_words.get('last_word')}
    current_word = random.sample(words, 1)[0]
    current_meaning = today_words['words'].get(current_word)

    edit_wallpaper(current_word, current_meaning)

    # Update today's words
    today_words['last_word'] = current_word
    with open('today-words.txt', 'w') as f1:
        f1.write(json.dumps(today_words))


def show_word_family():
    with open('json_words_families.txt', 'r') as file:
        word_json = json.loads(file.read())
        meaning = random.choice(list(word_json.keys()))
        words = ", ".join(word_json[meaning])
        edit_wallpaper(meaning, words)


def main():
    x = random.randint(0,1)
    single_word_meaning()
    # show_word_family()
    # if x == 0:
    #     single_word_meaning()
    # else:
    #     show_word_family()

    


if __name__ == "__main__": main()

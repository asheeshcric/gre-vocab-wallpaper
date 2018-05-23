from PIL import Image, ImageFont, ImageDraw
import random
import os


def get_random_words(lines):
	count = 0
	words = {}
	while 1:
		random_number = random.randint(0, len(lines)-1)
		word = lines[random_number].split("-")[0].replace(" ", "")
		meaning = lines[random_number].split("-")[1].replace("\n", "")
		if word in open('seen-words.txt').read():
			continue
		words[word] = meaning
		count += 1
		if count == 10 or len(lines) - len(open('seen-words.txt').readlines()) < 10:
			break
	print(words)
	return words

def main():
	lines = open('vocab-list.txt').readlines()

	if os.stat("today-words.txt").st_size == 0:
		today_words = get_random_words(lines)
		print(today_words)
		with open('today-words.txt', 'a') as f1:
			for word in today_words:
				f1.write(word + ' - ' + today_words[word])
				f1.write('\n')

	today_lines = open('today-words.txt').readlines()
	random_number = random.randint(0, len(today_lines)-1)

	current_line = today_lines[random_number]
	current_word = current_line.split("-")[0].replace(" ", "")
	current_meaning = current_line.split("-")[1].replace("\n", "")

	img = Image.open('sample.jpg')

	draw = ImageDraw.Draw(img)
	# font = ImageFont.truetype(<font-file>, <font-size>)
	font1 = ImageFont.truetype("RobotoCondensed-Bold.ttf", 96)
	# draw.text((x, y),"Sample Text",(r,g,b))
	draw.text((800, 300),current_word,(255,255,255),font=font1)

	font2 = ImageFont.truetype("Aaargh.ttf", 80)
	# draw.text((x, y),"Sample Text",(r,g,b))
	draw.text((400, 500),current_meaning,(255,255,255),font=font2)
	img.save('wallpaper.jpg')



if __name__ == "__main__": main()
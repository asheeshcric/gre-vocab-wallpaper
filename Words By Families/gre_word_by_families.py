import csv
import json

# import csv
# >>> with open('eggs.csv', newline='') as csvfile:
# ...     spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
# ...     for row in spamreader:
# ...         print(', '.join(row))
# Spam, Spam, Spam, Spam, Spam, Baked Beans
# Spam, Lovely Spam, Wonderful Spam

def save_words_json():
	with open('gre_words.txt', 'r') as file:
		lines = file.readlines()
		# print(lines)
		word_json = {}
		for line in lines:
			word, meaning = line.split(",")
			word = word.strip()
			meaning = meaning.strip().replace('\n', '')
			if word_json.get(meaning, None):
				word_json[meaning].append(word)
			else:
				word_json[meaning] = [word]

		print(word_json)
		with open('json_words.txt', 'w') as new_file:
			new_file.write(json.dumps(word_json))


if __name__ == '__main__':
	save_words_json()
def count_common_words(filename, word):
	"""Count the approximate number of words in a file."""
	try:
		with open(filename, encoding='utf-8') as f:
			contents = f.read()
	except FileNotFoundError:
		pass 
	else:
		word_count = contents.lower().count(word)
		print(f"The '{word}' appears in {filename} about {word_count} times")

filename = 'pg66735.txt'
count_common_words(filename, 'the')

import json

numbers = ['3', '5', '6', '8', '10']

filename = 'numbers.json'
with open(filename ,'w') as f:
	json.dump(numbers, f)

filename = 'numbers.json'
with open(filename) as f:
	numbers = json.load(f)

print(numbers)


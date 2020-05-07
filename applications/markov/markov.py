import random

# Read in all the words in one go
# TODO: analyze which words can follow other words
glossary = {}

def build_glossary():
	with open("input.txt") as f:
		all_words = f.read()

		words = all_words.split(" ")

		for index in range(0, len(words) - 1):
			current = words[index]
			next = words[index + 1]

			if current in glossary:
				glossary[current].append(next)
			else:
				glossary[current] = []
				glossary[current].append(next)
			
	return glossary

build_glossary()
# TODO: construct 5 random sentences

start = [word for word in glossary.keys() if word.istitle()]

for i in range(5):
	first_word = random.choice(start)
	word = first_word
	result = word
	while word:
		if word[-1] in ['.', '?', '!']:
			break
		else:
			word = random.choice(glossary[word])
			result += " " + word
	print(result)
	print('\n')

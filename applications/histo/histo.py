# Implement me.
with open("robin.txt") as f:
	the_input = f.read()
	clean = the_input.lower().split("\n")
	cleaning_string = " ".join(clean)
	clean_string = ""
	for char in cleaning_string:
		if char not in ['"', ':', ';', ',', '.', '-', '+', '=' '/', '\\', '|', '[', ']', '{', '}', '(', ')', '*', '^', '&']:
			clean_string += char
	
	histo = {}
	clean_array = clean_string.split(" ")
	for word in clean_array:
		if word == '':
			continue
		if word not in histo:
			histo[word] = "#"
		if word in histo:
			histo[word] += "#"

	items = list(histo.items())

	def get_big(item):
		return (item[1], item[0])

	items.sort(key=get_big, reverse=True)
	biggest_word = 0
	for word, _ in items:
		if len(word) > biggest_word:
			biggest_word = len(word)

	for item in items:
		space = " " * (biggest_word - len(item[0]))
		print(f'{item[0]}' + "  " +space+f'{item[1]}')
# show word count for each word,
# output -- ordered by the number of words, then by the word
# hash marks should be left justified two spaces after the longest word
# case should be in lowercase
# split the strings into words on any whitespace
# ignore special characters


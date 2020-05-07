def word_count(s):

	cache = {}

	def remove_extra(s):
		result = ""
		for char in s:
			if char not in '":;,.-+=/\\|[]{}()*^&':
				if char in ['\t', '\r', '\n']:
					result += " "
				else:
					result += char
		return result


	def counter(s, c):
		array = s.lower().split(" ")
		for word in array:
			if word == "":
				continue
			elif word not in c:
				c[word] = 1
			else:
				c[word] += 1
		return c

	no_extra = remove_extra(s)
	return counter(no_extra, cache)

if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))
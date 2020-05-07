def no_dups(s):
	# Implement me.
	result = ""
	if s == "":
		return s
	for word in s.split(" "):
		if word not in result:
			result += word + " "
	return result[:-1]
	# return result


if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))
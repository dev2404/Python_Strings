def reverse(string):
	s = string.split(' ')
	s = [word for word in s if word != '']
	s2 = s[::-1]
	
	return " ".join(s2)
	

print(reverse("the sky is blue"))

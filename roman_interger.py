def roman_to_integer(string):
	hash = {'I':1,'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
	count = 0
	for i in range(0, len(string)-1):
		if hash[string[i]] < hash[string[i+1]]:
			count -= hash[string[i]]
		else:
			count += hash[string[i]]
	return count + hash[string[-1]]		


x = (input("enter the roman number: "))
print(roman_to_integer(x))	
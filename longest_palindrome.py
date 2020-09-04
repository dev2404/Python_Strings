def longest_palindrome(string):
	m=""
	for i in range(len(string)):
		for j in range(len(string)-1,i, -1):
			if len(m) >= j-i:
				break
			elif string[i:j] == string[i:j][::-1]:
				m = string[i:j]
				break
	return m			



print(longest_palindrome("cbbddd"))

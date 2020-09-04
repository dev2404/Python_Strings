class Solution:
    def myAtoi(self, str: str) -> int:
        str = str.strip()
        match = re.match('[+-]{0,1}[0-9]+', str)
        if match is None:
            return 0
        else:
            num = int(str[match.start():match.end()])
            if num <= -2 ** 31: 
                return -2 ** 31
            elif num > 2**31 -1:
                return 2**31 -1
    return num
	  
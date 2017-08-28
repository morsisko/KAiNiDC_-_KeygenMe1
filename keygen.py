def sumString(string):
	sum = 0
	for char in string:
		sum += ord(char)
		
	return sum

def changeToString(secretValue, maxLen, fromRight=True):
	string = ""
	while secretValue:
		rest = secretValue % 0x10
		secretValue = int(secretValue/0x10)
		
		toChar = rest + 0x30
		
		if toChar >= 0x3A:
			toChar += 0x7
			
		string += chr(toChar)
	
	reversedString = string[::-1]
	if fromRight:
		return reversedString[:maxLen]
	else:
		return reversedString[-maxLen:]
	
def divHelper(name, key):
	sum = len(name) * ord(name[:1])
	sum *= sumString(name)
	sum *= key
	
	return int(round(sum/ord(name[:1]), 0))
	
def multiple(name):
	sum = len(name) * 0x17A
	sum *= sumString(name)
	
	return sum
	
def add(name):
	sum = len(name) * 0x2DD
	sum += sumString(name)
	
	return sum
	
def div(name):
	return divHelper(name, 0x20E)
	
def xor(name):
	sum = divHelper(name, 0x6C)
	sum ^= sumString(name)
	sum ^= 0xABCDEF
	
	return sum
	
string = "gucio"
print(changeToString(multiple(string), 4),
changeToString(add(string), 3),
changeToString(div(string), 6),
changeToString(xor(string), 4, False),
sep="-")

		
def encrypt(text, key):
	encryptedString = ""
	y = 0
	for i in range(0, len(text)):
		letter = text[i]
		encryptedString += chr(ord(letter) + key[y])
		y += 1
		if y >= len(key):
			y = 0

	return encryptedString


def encryptFile(fileName, destFileName, key):
	with open(fileName, 'r') as f:
		content = f.read()

	encryptedText = encrypt(content, key)

	with open(destFileName, 'w') as f:
		f.write(encryptedText)


key = (3, 5, 9)
fileName = 'nomefile.txt'
encryptFile('nomefile.txt', encrypt(fileName, key), key)

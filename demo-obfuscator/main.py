import os 
import base64



def main():

	reqFile = str(input("Please input name file for obfuscation "))

	theDir = os.listdir()
	for i in theDir:
		if reqFile == i:
			print("Founded: " + reqFile)

	mainStr = ""
	with open(reqFile, 'r') as file:
		stringsArray = []
		for line in file.readlines():
			string = line.strip()
			data = base64.b64encode(string.encode())
			sttr = str(data)
			sttr = sttr[2:]
			stringsArray.append(sttr)

		for strings in stringsArray:
			mainStr += strings

	with open(reqFile, 'w') as file2:
		file2.write(mainStr)	
	print(mainStr)


if __name__ == '__main__':
	main()
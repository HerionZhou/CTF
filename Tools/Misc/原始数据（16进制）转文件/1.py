with open('hexdata.txt', 'r') as f:
	with open('1.exe', 'wb') as f1:
		lines = f.readlines()
		for line in lines:
			line = line.strip()
			f1.write(bytes.fromhex(line))

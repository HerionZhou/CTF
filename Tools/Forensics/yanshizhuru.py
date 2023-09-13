import urllib.parse
with open('log','r') as file:
	ans = ""
	req = file.readlines()
	req = req[361:1842]
	for i in range(len(req)):
		if "[01/Mar/2022" in req[i]:
			if abs(int(req[i-1].split('[01/Mar/2022')[1][7:9]) - int(req[i].split('[01/Mar/2022')[1][7:9]))<3:
				tmp = req[i-1].split('=binary(\'')[1][0:3]
				if '\')' in tmp:
					ans += tmp[0]
				else:
					ans += tmp

	print(urllib.parse.unquote(ans))
import requests



URL="https://finger-warmup.chals.damctf.xyz/"
link="7tb1cnl5mp2xfn4pm0ep4h"
for i in range(1,500):
	request = requests.get(URL+link)
	start = request.text.find('<a href="')+9
	end = request.text.find('">click here', start)
	link=request.text[start:end]
	print(request.text)





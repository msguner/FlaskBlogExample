## Python - Flask Blog Example

**- Installed modules :**
 - Flask
 - PyMySQL
 - Flask-WTF
 - passlib
 - requests
 
**- Database name :** flask_blog

**- Create users table sql query :**
```sql
CREATE TABLE users (
	id int(11) unsigned NOT NULL AUTO_INCREMENT,
	name text,
	username text,
	email text,
	password text,
	PRIMARY KEY (id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
```
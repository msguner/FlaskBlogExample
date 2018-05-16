* Database name : flask_blog

* Create users table sql code : 

CREATE TABLE `users` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `name` text,
  `username` text,
  `email` text,
  `password` text,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
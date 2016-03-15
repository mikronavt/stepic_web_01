#!/usr/bin/env bash
sudo /etc/init.d/mysql restart
mysql -uroot -e "create database my_py_db;"
mysql -uroot -e "create user web_py identified by 'test123';"
mysql -uroot -e "grant all on my_py_db.* to web_py;"
#mysql --user web_py --password=test123 my_py_db

mysql -uroot -e "create database my_py_db"
mysql -uroot -e "create user web_py identified by 'test123'"
mysql -uroot -e "grant all on my_py_db.* to web_py"

sudo /etc/init.d/mysql start
mysql -uroot -e "CREATE DATABASE askdb;"
mysql -uroot -e "CREATE USER 'django@localhost' IDENTIFIED BY 'pass';"
mysql -uroot -e "GRANT ALL ON askdb.* TO 'django@localhost';"
mysql -uroot -e "FLUSH PRIVILEGES;"
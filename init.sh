#! usr/bin/bash
sudo ln -s /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/test.conf
sudo rm /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart
sudo ln -s /home/box/web/etc/hello.conf /etc/gunicorn.d/hello.conf
sudo ln -s /home/box/web/etc/django.conf /etc/gunicorn.d/django.conf
sudo /etc/init.d/gunicorn restart
sudo /etc/init.d/mysql restart
mysql -uroot -e "CREATE USER 'dj'@'localhost' IDENTIFIED BY '';"
mysql -uroot -e "GRANT ALL ON *.* TO 'dj'@'localhost';"
mysqladmin -uroot create django
python ask/manage.py syncdb
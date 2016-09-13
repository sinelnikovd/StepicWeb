mysql -uroot -e "CREATE USER 'dj'@'localhost' IDENTIFIED BY '';"
mysql -uroot -e "GRANT ALL ON *.* TO 'dj'@'localhost';"
mysqladmin -uroot create django
sudo pip install django-autofixture
python ask/manage.py syncdb
python ask/manage.py createsuperuser
python manage.py loadtestdata qa.Question:50
python manage.py loadtestdata qa.Answer:500
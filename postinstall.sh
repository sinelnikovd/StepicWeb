#mysql -uroot -e "CREATE USER 'dj'@'localhost' IDENTIFIED BY '';"
#mysql -uroot -e "GRANT ALL ON *.* TO 'dj'@'localhost';"
#mysqladmin -uroot create django
sudo pip install django-autofixture
python ask/manage.py syncdb
python ask/manage.py createsuperuser
python ask/manage.py loadtestdata qa.Question:50
python ask/manage.py loadtestdata qa.Answer:500

curl -X POST "http://127.0.0.1/ask/" --data "title=value1&text=value2"
#mysql -uroot -e "CREATE USER 'dj'@'localhost' IDENTIFIED BY '';"
#mysql -uroot -e "GRANT ALL ON *.* TO 'dj'@'localhost';"
#mysqladmin -uroot create django

git clone https://github.com/sinelnikovd/StepicWeb.git web

sudo pip install django-autofixture
python ask/manage.py syncdb
python ask/manage.py createsuperuser
python ask/manage.py loadtestdata qa.Question:50
python ask/manage.py loadtestdata qa.Answer:500

gunicorn -b 127.0.0.1:8000 --access-logfile '/home/box/web/ac.log' --error-logfile '/home/box/web/ac.log' ask.wsgi:application

curl -X POST "http://127.0.0.1/ask/" --data "title=value1&text=value2"
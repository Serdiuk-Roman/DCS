
# Django Celery Scrapy

create env

activate

pip install -r requirements.txt

python manage.py migrate

python manage.py runserver

celery -A dj_sc worker -l info

cd tutorial/

scrapy crawl porter_scrap



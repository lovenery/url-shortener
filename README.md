# URL Shortener

- Python 3.6.1
- Django 1.11.2
- SQLite 3

## Install

```
# Environment
git clone git@github.com:lovenery/url-shortener.git
cd url-shortener
virtualenv venv
. venv/bin/activate
pip install -r requirements.txt

# Development
cd src
cp .env.example .env
vim .env
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```
rm iron/login/migrations/0*.py
rm iron/core/migrations/0*.py
rm iron/fin/migrations/0*.py
rm db.sqlite3
python manage.py makemigrations
python manage.py migrate
echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('admin', '', '1234')" | python manage.py shell
# python manage.py loadata

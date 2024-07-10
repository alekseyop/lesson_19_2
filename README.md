# lesson_19_2
всё в develop

для вывода в json использовал для windows

chcp 65001

python manage.py dumpdata catalog --output=catalog/catalog_data.json --indent 4

Чтобы запустить команду загрузки данных, используйте команду в терминале:
python manage.py load_data

Для запуска приложения: python.exe manage.py runserver
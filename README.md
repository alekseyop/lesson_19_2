# lesson_19_2
�� � develop

��� ������ � json ����������� ��� windows

chcp 65001

python manage.py dumpdata catalog --output=catalog/catalog_data.json --indent 4

����� ��������� ������� �������� ������, ����������� ������� � ���������:
python manage.py load_data

��� ������� ����������: python.exe manage.py runserver
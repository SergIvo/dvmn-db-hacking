# Взлом электронного дневника

## О проекте

Данный модуль создан для корректировки информации в базе данных приложения "Электронный дневник", работающего на фреймворке Django (пример такого приложения можно скачать [здесь](https://github.com/devmanorg/e-diary/tree/master)). Модуль преимущественно использует инструменты [Django ORM](https://highload.today/django-orm/) и предназначен для использования в терминале Django.

Данный программный код написан в образовательных целях онлайн-курса для веб-разработчиков [dvmn.org](https://dvmn.org/)

## Запуск программы

1. Скачайте файлы с GitHub с помощью комманды `git clone`:
```
git clone https://github.com/SergIvo/dvmn-db-hacking
```
2. Скопируйте файл `hacking.py` в корневую папку приложения Django. Это должна быть та же папка, в которой находится файл `manage.py` и папка `datacenter`.
```
.
├── datacenter
├── hacking.py
├── manage.py
├── project
├── __pycache__
├── README.md
├── requirements.txt
└── schoolbase.sqlite3
```
3. Запустите терминал Django следующей командой:
```
python manage.py shell
```
Далее импортируйте весь модуль `hacking` или отдельные функции из него. Чтобы импортировать модуль, введите следующую команду:
```
import hacking
```
Модуль содержит три функции для корректировки данных в базе. Функция `fix_marks` заменяет все оценки '2' и '3' на оценки '5' для указанного ученика. Чтобы указать нужного ученика, нужно получить запись этого ученика из модели `Schoolkid`. Про модели данных в Django можно подробнее прочитать [здесь](https://django.fun/ru/docs/django/4.1/topics/db/models/). Для того, чтобы воспользоваться функцией `fix_marks`, достаточно ввести в консоли следующие команды:
```
from datacenter.models import Schoolkid
from hacking import fix_marks


target_kid = Schoolkid.objects.get(full_name="Фамилия Имя Отчество ученика, полностью, именно в таком порядке")
fix_marks(target_kid)
```
Функция `remove_chastisements` работает схожим образом. Ей также необходимо передать запись нужного ученика из модели `Schoolkid`, после чего функция удалит из базы данных все замечания, сделанные этому ученику. Пример использования:
```
from datacenter.models import Schoolkid
from hacking import remove_chastisements


target_kid = Schoolkid.objects.get(full_name="Фамилия Имя Отчество ученика, полностью, именно в таком порядке")
remove_chastisements(target_kid)
```
Про использование моделей Django ORM, получение информации из них и другие их возможности можно подробнее прочитать [здесь](https://django.fun/ru/docs/django/4.1/topics/db/queries/)

Функция `create_commendation` добавляет случайную похвалу указанному ученику за последний урок по указанному предмету. ФИО ученика и название предмета должны быть указаны полностью, через запятую. Пример использования:
```
from hacking import remove_chastisements


create_commendation("Фамилия Имя Отчество ученика", "Название предмета")
```

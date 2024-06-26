# Пульт охраны банка

Это внутренний репозиторий для сотрудников банка «Сияние». Если вы попали в
этот репозиторий случайно, то вы не сможете его запустить, т.к. у вас нет
доступа к БД, но можете свободно использовать код вёрстки или посмотреть как
реализованы запросы к БД.

Пульт охраны - это сайт, который можно подключить к удалённой базе данных с
визитами и карточками пропуска сотрудников нашего банка.

### Как установить
Python3 должен быть уже установлен. Затем используйте (или , есть конфликт с Python2) для установки зависимостей:`pip` `pip3`

```
pip install -r requirements.txt
```
В папке проекта создайте файл .env. Заполните переменные HOST , PORT , NAME , USER , PASSWORD. В настройке
ALLONED_HOSTS укажите через запятую, какие хосты смогут обслуживать этот сайт. Настройте DEBUG-режим под
себя - True или False.

Выглядеть должно примерно так:

```
PASSWORD_DB = 'osim5'
ENGINE_DB = 'django.db.backends.postgresql_psycopg2'
HOST_DB = 'checkpoint.devman.org'
PORT_DB = '5434'
NAME_DB = 'checkpoint'
USER_DB ='guard'
SECRET_KEY = 'REPLACE_ME'
DEBUG = True
```

### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).
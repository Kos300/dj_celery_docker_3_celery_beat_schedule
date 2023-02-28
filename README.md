## Django, Celery, Celery beat, Docker, Redis

1) Приложение ставит задачу на загрузку файла в очередь каждый раз при обновлении страницы. Задачи последовательно выполняются, загружая файлы в указанную папку.
2) С помощью Celery beat создано расписание выполнения задач: периодических и однократных. Данные расписания хранятся в базе данных sqlite3. Задачи могут устанавливаться через админ панель или через терминал контейнера. 
   

Для реализации в docker-compose описаны четыре контейнера: 
- для приложения
- для Celery beat
- для "worker"-a
- для Redis

## Зависимости

requirements.txt

amqp==5.1.1 
asgiref==3.6.0
async-timeout==4.0.2
billiard==3.6.4.0
celery==5.2.7
certifi==2022.12.7
charset-normalizer==3.0.1
click==8.1.3
click-didyoumean==0.3.0
click-plugins==1.1.1
click-repl==0.2.0
colorama==0.4.6
Django==4.1.7
idna==3.4
kombu==5.2.4
prompt-toolkit==3.0.36
pytz==2022.7.1
redis==4.5.1
requests==2.28.2
six==1.16.0
sqlparse==0.4.3
tzdata==2022.7
urllib3==1.26.14
vine==5.0.0
wcwidth==0.2.6

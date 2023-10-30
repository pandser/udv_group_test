## Скрипт сбора сведений с коммутатора

Запуск через Docker-контейнер:

```
sudo docker build -t <имя образа> .
```

```
sudo docker run -v <путь к текущему каталогу>/report/:/app/report <имя образа> python3 main.py
```
Результат выгружается в файл report.txt в папке report

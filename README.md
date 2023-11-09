## Скрипт сбора сведений с коммутатора

Запуск скрипта

```
./run.sh
```

Пример  файла .env
```
SWITCH="{
    'device_type': 'cisco_ios_telnet',
    'host': '192.168.1.1',
    'username': 'admin',
    'password': 'admin'
    }"
```

Результат выгружается в файл report.txt в папке report

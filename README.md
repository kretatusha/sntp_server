# sntp_server
Запуск сервера

python server.py

Запуск клиента

python client.py

Как работает

Получаем пакет от правдивый NTP-сервер

Изменяем 40-47 байт, содержащий информацию о времени на N секунд

Пробрасываем пакет клиенту

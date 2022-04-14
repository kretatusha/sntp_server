import socket
import time

from ntplib import NTPStats

stats = NTPStats()

sock = socket.socket()
sock.connect(('localhost', 123))
sock.send(str('HLO').encode())

data = sock.recv(1024)
sock.close()

print('Полученные данные: {}'.format(data))
stats.from_data(data)
print('Время полученное пользователем: {}'.format(time.ctime(stats.tx_time)))
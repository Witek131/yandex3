'''Аудиорегистратор формирует записи в формате стерео с частотой дискретизации 44 кГц и разрешением 16 бит без сжатия.
Длительность каждой записи составляет 1 минуту. Аудиофайлы сохраняются в памяти устройства, группируются в пакеты по 32 штуки,
затем передаются в центр обработки информации со скоростью передачи данных 1 802 240 бит/с.
Сколько секунд потребуется для передачи одного пакета?
В ответе укажите целую часть числа.'''
s=(44000*16*60)*32*2
print(s//1_802_240)

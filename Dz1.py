#первое задание

duration = int(input('Введите время в секундах: '))

sec, min, hours, days = (((duration % 86400) % 3600) % 60), (((duration % 86400) % 3600) // 60), ((duration % 86400) // 3600), duration // 86400


print ('{}  дней, {} часов, {} минут, {} секунд.'.format(days, hours, min, sec))

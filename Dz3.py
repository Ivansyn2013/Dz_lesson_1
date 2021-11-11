# третье задание

n = int(input('Введите число процентов:'))
if n % 10 == 1:
    word = 'процент.'
elif n % 10 >= 2 and n % 10 <=4 :
    word = 'процента.'
elif n % 10 >= 5 and n % 10 <= 9 :
    word = 'процентов.'
else: word = 'процентов.'

print(n,'%', word)
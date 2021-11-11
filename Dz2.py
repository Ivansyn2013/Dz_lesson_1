# второе задание

nkubs = []
kubs = range(1,1001)
sum_result = 0
#вычисляем кубы нечетный
for i in kubs:
   # print(i)
    if kubs[i-1]%2 != 0:
        nkubs.append((kubs[i-1] ** 3))
print('Кубы нечетных чисел:', nkubs)
    #сумма чисел кубов
for i, item in enumerate(nkubs):
    sum_len = 0
    ost = nkubs[i]
    temp_sum = 0
    while ost > 9 :

        temp_sum = ost % 10 + temp_sum
        ost = ost // 10

            # вычесляем сумму делленных на 7
    else:
        temp_sum = temp_sum + ost
        if temp_sum % 7 == 0:

            sum_result = sum_result + temp_sum

print('Сумма знаков чисел делящихся на 7 =', sum_result)

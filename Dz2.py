# второе задание

nkubs = []
result_list = []
result_list17 = []
nkubs17 = []
kubs = range(1,1001)
sum_result = 0
sum_result17 = 0
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
            result_list.append(nkubs[i])
            sum_result = sum_result + temp_sum


print('Суммма чисел делящихся по сумме знаков на 7:', sum(result_list))


for i, item in enumerate(nkubs):
    nkubs17.append(nkubs[i] + 17)

for i, item in enumerate(nkubs17):
    sum_len17 = 0
    ost17 = nkubs17[i]
    temp_sum17 = 0
    while ost17 > 9 :

        temp_sum17 = ost17 % 10 + temp_sum17
        ost17 = ost17 // 10

            # вычесляем сумму делленных на 7
    else:
        temp_sum17 = temp_sum17 + ost17
        if temp_sum17 % 7 == 0:
            result_list17.append(nkubs17[i])
            sum_result17 = sum_result17 + temp_sum17
print('Суммма чисел делящихся по сумме знаков на 7 + 17 :', sum(result_list17))

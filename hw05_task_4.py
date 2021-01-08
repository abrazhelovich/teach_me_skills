# Для заданного числа N составьте программу
# вычисления суммы S=1+1/2+1/3+1/4+...+1/N, где N –
# натуральное число.

digit = int(input('Need number: '))
sum = 1

for number in range(2, digit + 1):
    sum += 1 / number

print('Summa:' + str(sum))

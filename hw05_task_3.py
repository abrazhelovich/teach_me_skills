# Дано число. Найти сумму и произведение его цифр.

number = list(input('Enter the number: '))

sum = 0
mult = 1

for i in number:
    sum += int(i)
    mult *= int(i)

print('Summa: ' + str(sum))
print('Multiplication: ' + str(mult))

'''Введите число. Если это число делиться на 1000 без
остатка, то выведите на экран "millennium".'''

number = 0

try:
    number = int(input('Please enter a number: '))
    split =  number % 1000
    if split == 0:
        print('millennium')
except:
    print('Please enter a number not a string.')

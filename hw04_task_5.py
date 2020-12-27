'''Создать строку равную всем элементам введенной
строки с четными индексами. (считая, что индексация
начинается с 0, поэтому символы выводятся начиная
с первого, индексы 0,2,4,6....).'''

input_str = input('Please enter enything: ')
new_str = input_str[::2]

if len(input_str) == 0:
    print('Please enter enything!!!')
else:
    print('Your new string looks as follows: ' + str(new_str))

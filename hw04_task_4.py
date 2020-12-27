'''Создать строку равную введенной строке без
последних двух символов.'''

input_str = input('Please enter enything: ')
new_str = input_str[:-2]

if len(input_str) == 0:
    input_str
    print('Please enter enything!!!')
else:
    print('Your new string looks as follows: ' + str(new_str))

# Написать программу, в которой вводятся два операнда
# Х и Y и знак операции sign (+, –, /, *). Вычислить
# результат Z в зависимости от знака. Предусмотреть
# реакции на возможный неверный знак операции, а
# также на ввод Y=0 при делении. Организовать
# возможность многократных вычислений без
# перезагрузки программа (т.е. построить бесконечный
# цикл). В качестве символа прекращения вычислений
# принять ‘0’ (т.е. sign='0').

while True:
    op_x = input('Please typing operand X: ')
    op_y = input('Please typing operand Y: ')
    sign = input('Please typing sign as well (+, –, /, *). "0" - Exit from program: ')

    if op_y == 0:
        print('ERROR: division by zero. Please change operand Y.')
    elif sign == '+':
        plus = op_x + op_y
        print(plus)
    elif sign == '-':
        minus = op_x - op_y
        print(minus)
    elif sign == '/':
        division = op_x / op_y
        print(division)
    elif sign == '*':
        multi = op_x * op_y
        print(multi)
    elif sign == '0':
        print('Exit from program')
        break
    else:
        print('Not correct sign')

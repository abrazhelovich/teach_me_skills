# Для каждого натурального числа в промежутке от m до
# n вывести все делители, кроме единицы и самого
# числа. m и n вводятся с клавиатуры.
# Пример:m =100, n = 105
# 100: 2 4 5 10 20 25 50
# 101:
# 102: 2 3 6 17 34 51
# 103:
# 104: 2 4 8 13 26 52
# 105: 3 5 7 15 21 35

num_m = int(input('m: '))
num_n = int(input('n: '))

div = []
join_div = ' '.join(div)

for i in range(num_m, num_n + 1):
    div = []
    for k in range(2, num_n):
        if i / k == 1:
            continue
        if i % k == 0:
            div.append(k)
    print(f'{i}:', ' '.join(str(e) for e in div))

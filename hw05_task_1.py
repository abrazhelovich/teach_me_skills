# Написать генератор песенки «TEN green bottles
# hanging on the wall».
# В песенке вместо цифр должны быть именно слова,
# обозначающие цифры, т.е. TEN, NINE, EIGHT, etc.
# Песенка состоит из серии куплетов вот таких:
#
# <количество> green bottles hanging on the wall,
# <количество> green bottles hanging on the wall,
# And if one green bottle should accidentally fall,
# There‛ll be...
# <пустая строка>
# <количество - 1> green bottles hanging on the wall…
#
# И так до тех пор, пока не закончатся бутылки. Когда
# они закончились, то песенка должна закончится
# фразой: NO green bottles hanging on the wall!


dic = {1: 'ONE', 2: 'TWO', 3: 'THREE', 4: 'FOUR', 5: 'FIVE', 6: 'SIX', 7: 'SEVEN',
       8: 'EIGHT', 9: 'NINE', 10: 'TEN'}


str_one = 'green bottles hanging on the wall,'
str_two = 'green bottles hanging on the wall,'
str_three = 'And if one green bottle should accidentally fall,'
str_four = 'There‛ll be...'

len_dic = len(dic)

i = 0
while i < len_dic:
    print(f'{dic[len_dic - i]} {str_one}')
    print(f'{dic[len_dic - i]} {str_two}')
    print(str_three)
    if str_three.startswith('And'):
        print(str_four, end='\n\n')
        i += 1

print('NO green bottles hanging on the wall!')

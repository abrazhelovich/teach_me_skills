# 1. Написать модуль, содержащий 12 функций по
# переводу:
# Примечание: функция принимает на вход число и возвращает
# конвертированное число
# 1.1.Дюймы в сантиметры
# 1.2.Сантиметры в дюймы
# 1.3.Мили в километры
# 1.4.Километры в мили
# 1.5.Фунты в килограммы
# 1.6.Килограммы в фунты
# 1.7.Унции в граммы
# 1.8.Граммы в унции
# 1.9.Галлон в литры
# 1.10.Литры в галлоны
# 1.11.Пинты в литры
# 1.12.Литры в пинты

def print_res(res: float) -> float:
    """The function just print result"""

    print(res, end='\n\n')

def inchToSant(inch: float, div: float = 2.54) -> float:
    """The function transform Inch to Sant"""

    return inch * div

def santToInch(sant: float, div: float = 2.54) -> float:
    """The function transform Sant to Inch"""

    return sant / div

def milToKm(mil: float, div: float = 1.609344) -> float:
    """The function transform Miles to Kilometers"""

    return mil * div

def kmToMil(km: float, div: float = 1.609344) -> float:
    """The function transform Kilometers to Miles"""

    return km / div

def funtToKg(funt: float, div: float = 0.4535923745) -> float:
    """The function transform Pounds to Kilograms"""

    return funt * div

def kgToFunt(kg: float, div: float = 0.4535923745) -> float:
    """The function transform Kilograms to Pounds"""

    return kg / div

def uncToGr(unc: float, div: float = 28.349523125) -> float:
    """The function transform Ounces to Grams"""

    return unc * div

def grToUnc(gr: float, div: float = 28.349523125) -> float:
    """The function transform Grams to Ounces"""

    return gr / div

def galToLitr(gal: float, div: float = 3.78541) -> float:
    """The function transform Halons to Litres"""

    return gal * div

def litrToGal(litr: float, div: float = 3.78541) -> float:
    """The function transform Litres to Halons"""

    return litr / div

def pintaToLitr(pinta: float, div: float = 0.56826240812) -> float:
    """The function transform Pints to Litres"""

    return pinta * div

def litrToPinta(litr: float, div: float = 0.56826240812) -> float:
    """The function transform Litres to Pints"""

    return litr / div

def main():
    while True:
        val = int(input('''1.Дюймы в сантиметры
2.Сантиметры в дюймы
3.Мили в километры
4.Километры в мили
5.Фунты в килограммы
6.Килограммы в фунты
7.Унции в граммы
8.Граммы в унции
9.Галлон в литры
10.Литры в галлоны
11.Пинты в литры
12.Литры в пинты
0.Выход из программы

Сделайте выбор: '''))

        if val == 0:
            break

        text = float(input('Введите численное значение: '))
        if val == 1:
            result = inchToSant(text)
            pr_result = print_res(result)
        elif val == 2:
            result = santToInch(text)
            pr_result = print_res(result)
        elif val == 3:
            result = milToKm(text)
            pr_result = print_res(result)
        elif val == 4:
            result = kmToMil(text)
            pr_result = print_res(result)
        elif val == 5:
            result = funtToKg(text)
            pr_result = print_res(result)
        elif val == 6:
            result = kgToFunt(text)
            pr_result = print_res(result)
        elif val == 7:
            result = uncToGr(text)
            pr_result = print_res(result)
        elif val == 8:
            result = grToUnc(text)
            pr_result = print_res(result)
        elif val == 9:
            result = galToLitr(text)
            pr_result = print_res(result)
        elif val == 10:
            result = litrToGal(text)
            pr_result = print_res(result)
        elif val == 11:
            result = pintaToLitr(text)
            pr_result = print_res(result)
        elif val == 12:
            result = litrToPinta(text)
            pr_result = print_res(result)

if __name__ == '__main__':
    main()

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

def inchToSant(inch):
    convert = inch * 2.54
    return convert

def santToInch(sant):
    convert = sant / 2.54
    return convert

def milToKm(mil):
    convert = mil * 1.609344
    return convert

def kmToMil(km):
    convert = km / 1.609344
    return convert

def funtToKg(funt):
    convert = funt * 0.4535923745
    return convert

def kgToFunt(kg):
    convert = kg / 0.4535923745
    return convert

def uncToGr(unc):
    convert = unc * 28.349523125
    return convert

def grToUnc(gr):
    convert = gr / 28.349523125
    return convert

def galToLitr(gal):
    convert = gal * 3,78541
    return convert

def litrToGal(litr):
    convert = litr / 3,78541
    return convert

def pintaToLitr(pinta):
    convert = pinta * 0.56826240812
    return convert

def litrToPinta(litr):
    convert = litr * 0.56826240812
    return convert

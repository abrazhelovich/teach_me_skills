# Даны три слова. Выяснить, является ли хоть одно из
# них палиндромом ("перевертышем"), т. е. таким,
# которое читается одинаково слева направо и справа
# налево. (Определить функцию, позволяющую
# распознавать слова палиндромы.)

def is_palindrom(text):
    result = [word for word in text if word == word[::-1]]
    if len(result) != 0:
        return f"Palindrom exist, it is: {', '.join(result)}"
    else:
        return f'Palindrom not exist'

def main():
    print('Typing 3 words:', end='\n\n')
    words = [input() for i in range(3)]
    print(is_palindrom(words))

if __name__ == '__main__':
    main()

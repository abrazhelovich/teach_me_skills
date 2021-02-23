# Даны три слова. Выяснить, является ли хоть одно из
# них палиндромом ("перевертышем"), т. е. таким,
# которое читается одинаково слева направо и справа
# налево. (Определить функцию, позволяющую
# распознавать слова палиндромы.)

def palindrom(word):
    if word == word[::-1]:
        return f'Palindrom'
    return f'Not palindrom'


def main():
    print('Typing 3 words:', end='\n\n')
    words = [input() for i in range(3)]
    for word in words:
        print(f'{word} - {palindrom(word)}')


if __name__ == '__main__':
    main()

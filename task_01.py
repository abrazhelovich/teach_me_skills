# 1. Создать сайт, содержащий 3 страницы: главную,
# страницу со списком пользователей, детальную
# страницу пользователя.
# 2. При переходе на главную страницу должна
# отобразится страница с приветственной надписью для
# пользователя.
# 3. При переходе на страницу со списком пользователей -
# должна отобразится страница, где перечислены
# пользователи в виде ссылок. При клике на любую из
# них должен осуществиться переход на детальную
# страницу пользователя.
# 4. При переходе на детальную страницу пользователя
# должна открыться страница с приветствием
# пользователя по его имени и текущее время с
# указанием утро это, день, вечер или ночь(6 - 12 утро,
# 12 - 16 день, 16 - 0 вечер, 0 - 6 ночь), например:
# Привет, Жора! Сейчас 23:00:32. Приятного вечера!

from flask import Flask, render_template, make_response
from datetime import datetime

app = Flask(__name__)
app.debug = True


def day_time():
    now = datetime.now().strftime('%H:%M:%S')
    return now


def compare_date():
    now = datetime.now().strftime('%H:%M:%S')
    if now < '12:00:00':
        return 'Good morning!!!'
    if now > '16:00:00':
        return 'Have a nice evening!!!'
    return 'Have a nice day!!!'


@app.route('/')
def root():
    return render_template('index.html')


@app.route('/users/')
def users():
    return render_template('user_list.html')


@app.route('/users/<string:name>/')
def user(name):
    day = day_time()
    greeting = compare_date()
    print(day)
    user_prof = name
    tpl_dict = {'name': user_prof, 'day': day, 'greeting': greeting}
    return render_template('user_profile.html', **tpl_dict)


if __name__ == '__main__':
    app.run()
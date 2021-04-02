from flask import Flask, render_template, make_response
from datetime import datetime

app = Flask(__name__)
app.debug = True

users = {'user1': 'Petia', 'user2': 'Sasha', 'user3': 'Ivan'}

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
    return render_template('menu.html')


@app.route('/welcome/')
def welcome():
    return render_template('index.html')


l_users = ['Petia', 'Sasha', 'Ivan', 'Dima', 'Vlad', 'Kostia']


@app.route('/users/')
def users():

    tpl_dict = {'l_users': l_users}
    return render_template('user_list.html', **tpl_dict)


@app.route('/users/<string:name>/')
def user(name):
    day = day_time()
    greeting = compare_date()
    print(day)
    user_prof = name
    tpl_dict = {'name': user_prof, 'day': day, 'greeting': greeting, 'l_users': l_users}
    return render_template('user_profile.html', **tpl_dict)


if __name__ == '__main__':
    app.run()
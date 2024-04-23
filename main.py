import random
import sqlite3
from flask import Flask, url_for, request, render_template
import datetime

app = Flask(__name__)
NAME = []
count = 1


class User():
    def __init__(self):
        self.clas = ''
        self.name = ''
        self.res = []
        self.time_start = datetime.datetime.today() - datetime.timedelta(minutes=-40)


class Decision():
    def __init__(self):
        self.result = []


class Counter():
    def __init__(self):
        self.counter = 1


my_counter = Counter()
my_results = Decision()
my_user = User()


@app.route('/', methods=['POST', 'GET'])
def start_page():
    if request.method == 'GET':
        return render_template('home_page.html')
    elif request.method == 'POST':
        name = request.form

        if 'surname' in name:
            print(*name.getlist('surname'), *name.getlist('name'), *name.getlist('clas'),
                  *name.getlist('var'))
            my_user.clas = str(name.getlist('clas'))
            my_user.name = f"{str(name.getlist('surname')[0])} {str(name.getlist('name')[0])}"
        # print('Данные пользователя', name)

        # база данных
        # DB = sqlite3.connect('DB/test_web.db')
        # SQL = DB.cursor()
        # al = SQL.execute(f"SELECT * FROM task WHERE number == {my_counter.counter}").fetchall()
        # print(my_counter.counter)
        # img = ''
        # if my_counter.counter <= 3:
        #     img = str(random.choice(al[1]))

        # без базы данных
        al = ['/static/img/1280.gif', '/static/img/1267.gif', '/static/img/1276.gif', '/static/img/1270.gif']
        img = random.choice(al)
        # del al[al.index(img)]
        name = request.form
        if 'decision' in name:
            print(img, *name.getlist('decision'))
            my_user.res.append([img, str(name.getlist('decision')[0])])
        if my_counter.counter == 4:
            res_json()
            return 'КОНЕЦ РАБОТЫ!'
        return tasks(my_counter, img)


@app.route('/tasks', methods=['POST', 'GET'])
def tasks(my_counter, img):
    my_counter.counter += 1
    # res = request.form
    # print('результат', res.getlist('decision'))
    return render_template('tasks_page.html', img=img)


@app.route('/admin_page', methods=['POST', 'GET'])
def admin_page():
    return render_template('admin_page.html')


def res_json():
    print(my_user.clas)
    print(my_user.name)
    print(my_user.res)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')

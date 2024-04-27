import random
import sqlite3
from flask import Flask, url_for, request, render_template
import datetime
from flask import send_file

app = Flask(__name__)
NAME = []
count = 1


class User():
    def __init__(self):
        self.clas = ''
        self.name = ''
        self.res_task = []
        self.res_des = []
        self.result = []


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

        DB = sqlite3.connect('DB/test_web.db')
        SQL = DB.cursor()
        al = SQL.execute(f"SELECT * FROM task WHERE number == {my_counter.counter}").fetchall()
        img = ''
        if my_counter.counter <= 3:
            list_img = [i[1] for i in al]
            img = str(random.choice(list_img))

        # без базы данных
        # al = ['/static/img/1280.gif', '/static/img/1267.gif', '/static/img/1276.gif', '/static/img/1270.gif']
        # img = random.choice(al)
        # del al[al.index(img)]
        name = request.form
        if 'surname' in name:
            my_user.clas = str(name.getlist('clas'))
            my_user.name = f"{str(name.getlist('surname')[0])} {str(name.getlist('name')[0])}"
            my_user.res_task.append(img)

        elif 'decision' in name:
            if img != '':
                my_user.res_task.append(img)
            my_user.res_des.append(str(name.getlist('decision')[0]))
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
    # if request.method == ['GET']:
    #     return 'UJNJDJ'
    # elif request.method == ['POST']:
    #     print(2)
    #     return render_template('admin_page.html')
    return render_template('admin_page.html')


@app.route('/download_file')
def download_file():
    return send_file('table.xlsx')


@app.route('/login', methods=['GET', 'POST'])
def login():
    return 'ЛОГИН'


@app.route('/register', methods=['GET', 'POST'])
def reqister():
    return 'РЕГИСТРАЦИЯ'


def res_json():
    print(my_user.clas)
    print(my_user.name)
    for i in range(3):
        my_user.result.append([my_user.res_task[i], my_user.res_des[i]])
    print(my_user.result)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')

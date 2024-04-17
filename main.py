import random
import sqlite3
from flask import Flask, url_for, request, render_template

app = Flask(__name__)
NAME = []
count = 1


class Decision():
    def __init__(self):
        self.result = []


class Counter():
    def __init__(self):
        self.counter = 0


my_counter = Counter()
my_results = Decision()

@app.route('/', methods=['POST', 'GET'])
def start_page():
    if request.method == 'GET':
        return render_template('home_page.html')
    elif request.method == 'POST':
        name = request.form
        my_results.result.append(name)
        print('Данные пользователя', name)

        if my_counter.counter == 3:
            return 'КОНЕЦ ЗДЕСЬ'
        return tasks(my_counter)


@app.route('/tasks', methods=['POST', 'GET'])
def tasks(my_counter):
    # база данных
    # DB = sqlite3.connect('DB/test_web.db')
    # SQL = DB.cursor()
    # al = SQL.execute(f"SELECT * FROM task WHERE number == {count}").fetchall()
    # img = str(random.choice(al[1])

    al = ['/static/img/1280.gif', '/static/img/1267.gif', '/static/img/1276.gif']
    img = random.choice(al)
    # del al[al.index(img)]
    my_counter.counter += 1
    res = request.form
    print('результат', res.getlist('decision'))
    return render_template('tasks_page.html', img=img)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')

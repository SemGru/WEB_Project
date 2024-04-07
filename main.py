import random

from flask import Flask, url_for, request, render_template

app = Flask(__name__)
NAME = []


@app.route('/', methods=['POST', 'GET'])
@app.route('/start', methods=['POST', 'GET'])
def astronaut_selection():
    if request.method == 'GET':
        # required
        # return render_template('start.html')
        return f'''<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">
                    <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                    <title>Проверочная работа</title>
                  </head>
                  <body>
                    <h1 align="center">Проверочная работа</h1>
                    <h3 align="center">по информатике</h3>
                    <div>
                        <form class="login_form" method="post">

                            <input type="text" class="form-control" id="surname" aria-describedby="surnamelHelp" placeholder="Введите фамилию" name="surname" >
                            <input type="text" class="form-control" id="name" aria-describedby="nameHelp" placeholder="Введите имя" name="name" >
                            <input type="text" class="form-control" id="class" aria-describedby="classHelp" placeholder="Введите класс в формате 9 А" name="class" >
                            <br>
                            <input type="text" class="form-control" id="var" aria-describedby="classHelp" placeholder="Введите вариант работы" name="var">
                            <br>
                             <button type="submit" class="btn btn-primary" Centered button >Начать</button>
                        </form>
                    </div>
                  </body>
                </html>'''
    if request.method == 'POST':
        NAME = request.form
        print(NAME)
        return tasks()


@app.route('/tasks', methods=['POST', 'GET'])
def tasks():
    # if request.method == 'GET':
    # прикручитить получание названия файло виз БД
    img = random.choice(['/static/img/1280.gif', '/static/img/1267.gif'])
    # удаление названия файла чтобы избежать повтора
    return f'''<!doctype html>
                    <html lang="en">
                        <head>
                        <meta charset="utf-8">
                        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                        <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">
                        <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                        <title>Проверочная работа</title>
                        </head>
                        <body>
                        <form class="work_form" method="post">
                        <img class="displayed" src="{img}">
                        <div class="form-group">
                                        <label for="about">Решение:</label>
                                        <textarea class="form-control" id="about" rows="5" name="decision"></textarea>
                        </div>
                        <button type="submit" class="btn btn-primary" Centered button >Отправить</button>
                        </form>
                        <body>
                    </html>'''
    # if request.method == 'POST':
    #     print(NAME)
    #     print(request.form)
    #     tasks()


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')

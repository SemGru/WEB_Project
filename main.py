import random

from flask import Flask, url_for, request

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
@app.route('/astronaut_selection', methods=['POST', 'GET'])
def astronaut_selection():
    if request.method == 'GET':
        return f'''<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">
                    <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                    <title>Отбор астронавтов</title>
                  </head>
                  <body>
                    <h1 align="center">Анкета претендента</h1>
                    <h3 align="center">на участие в миссии</h3>
                    <div>
                        <form class="login_form" method="post">
                            <input type="text" class="form-control" id="surname" aria-describedby="surnamelHelp" placeholder="Введите фамилию" name="surname">
                            <input type="text" class="form-control" id="name" aria-describedby="nameHelp" placeholder="Введите имя" name="name">
                            <input type="text" class="form-control" id="class" aria-describedby="classHelp" placeholder="Введите класс" class="class">
                            <br>
                            <button type="submit" class="btn btn-primary">Начать</button>
                        </form>
                    </div>
                  </body>
                </html>'''
    if request.method == 'POST':
        print(request.form)
        img = random.choice(['/static/img/Background_3.jpg', '/static/img/maars.jpg'])
        return f'''<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">
                    <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                    <title>Отбор астронавтов</title>
                  </head>
                  <body>
                  <img src="{img}">
                  <div class="form-group">
                                <label for="about">Решение:</label>
                                <textarea class="form-control" id="about" rows="3" name="about"></textarea>
                  </div>
                  <button type="submit" class="btn btn-primary">Отправить</button>
                  <body>
                </html>'''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')

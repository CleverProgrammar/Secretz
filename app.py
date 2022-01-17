from json import (load, dump)
from flask import Flask, render_template, request

from hashlib import sha256

app = Flask(__name__)
SECRETS_DATABASE = load(open('secrets.json'))


@app.route("/", methods=['GET', 'POST'])
def create():
    if request.method == "POST":
        title = request.form['id']
        password = request.form['password']
        secret = request.form['secret']

        SECRETS_DATABASE[title] = {
            'password': sha256(password.encode()).hexdigest(),
            'secret': secret
        }
        dump(SECRETS_DATABASE, open('secrets.json', "w"))
        print(SECRETS_DATABASE)

    return render_template('index.html')


@app.route("/view", methods=["GET","POST"])
def view():
    if request.method == 'POST':
        Id = request.form['id']
        password = sha256(request.form['password'].encode()).hexdigest()
        if SECRETS_DATABASE[Id]['password'] == password or SECRETS_DATABASE[Id]['password'] == 0:
            secret = SECRETS_DATABASE[Id]['secret']
            print(secret)

        return render_template('view.html', id=Id, secret=secret)
    return render_template('view.html', id="None", secret="None")


if __name__ == '__main__':
    app.run()

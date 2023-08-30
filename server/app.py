#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string>')
def print_string(string):
    # return f'<h1>Profile for {username}</h1>'
    print(f'{string}')
    return f'{string}'


@app.route("/count/<n>")
def count(n):
    n = int(n)
    output = ""

    for i in range(n):
        output += str(i) + "\n"
    return output


@app.route("/math/<num1>/<operation>/<num2>")
def math(num1, operation, num2):
    num1 = int(num1)
    num2 = int(num2)

    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "div":
        result = num1 / num2
    elif operation == "%":
        result = num1 % num2
    return str(result)



if __name__ == '__main__':
    app.run(port=5555, debug=True)

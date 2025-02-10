from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def index():  # put application's code here
    return render_template("index.html")

@app.route('/calculate', methods=['POST', 'GET'])

def calculate():
    num1 = int(request.form.get("num1"))
    num2 = int(request.form.get("num2"))
    operation = request.form.get("operation")
    result = 0
    if operation == "divide":
        if num2 == 0:
            result = "Error"
        else:
            result = num1 / num2
    elif operation == "multiply":
        result = num1 * num2
    elif operation == "add":
        result = num1 + num2
    elif operation == "subtract":
        result = num1 - num2

    return render_template("index.html", result=result)
if __name__ == '__main__':
    app.run()

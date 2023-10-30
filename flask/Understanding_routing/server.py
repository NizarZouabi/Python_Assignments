from flask import Flask
app = Flask(__name__)
@app.route('/')
def Hello_World():
    return 'Hello World!'
@app.route('/dojo')
def dojo():
    return "Dojo!"
@app.route('/say/flask')
def greet_first():
    return "Hi Flask!"
@app.route('/say/michael')
def greet_second():
    return "Hi Michael!"
@app.route('/say/john')
def greet_third():
    return "Hi John!"
@app.route('/repeat/<int:num>/<string:input>')
def repeat_input(num, input):
    return f'{input * num}'
@app.route('/<path:invalid_route>')
def error_message(invalid_route):
    return f"Sorry! No response, \"{invalid_route}\" is not valid, Try again."
if __name__ =="__main__":
    app.run(debug=True)
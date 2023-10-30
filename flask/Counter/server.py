from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)

app.secret_key = '786578'


@app.route('/')
def default():
    session['count'] += 1
    return render_template('index.html', count=session.get('count'))


@app.route('/increment')
def add():
    session['count'] += 1
    return redirect('/')


@app.route('/destroy_session')
def clear():
    session['count'] = 0
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)

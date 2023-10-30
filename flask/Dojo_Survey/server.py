from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)

app.secret_key = '547564'


@app.route('/')
def default():
    return render_template('main.html')


@app.route('/form', methods=['POST'])
def form():
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['comment'] = request.form['comment']
    return redirect('/result')


@app.route('/result', methods=['GET'])
def show():
    return render_template('info.html', name=session.get('name'), location=session.get('location'), language=session.get('language'), comment=session.get('comment'))

if __name__=='__main__':
    app.run(debug=True)
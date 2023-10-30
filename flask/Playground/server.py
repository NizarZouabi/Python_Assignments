from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def default():
    return render_template("index.html")

@app.route('/play')
def index():
    return render_template("index.html", x=3, color='blue')

@app.route('/play/<int:num>')
def repeat(num):
    return render_template("index.html", x=num, color='blue')

@app.route('/play/<int:num>/<color>')
def change_color(num, color):
    return render_template("index.html", x=num, color=color)
if __name__=="__main__":
    app.run(debug=True)
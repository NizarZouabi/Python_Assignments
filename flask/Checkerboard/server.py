from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def default():
    return render_template("index.html", col=0, row=0, color=0, subcolor=0)


@app.route('/<int:c>')
def white(c):
    return render_template("index.html", col=c, row=1, color="black", subcolor=0)


@app.route('/<int:c>/<int:r>')
def black(c, r):
    return render_template("index.html", col=c, row=r, color="black", subcolor="white")


@app.route('/<int:c>/<int:r>/<color>')
def colors(c, r, color):
    return render_template("index.html", col=c, row=r, color=color, subcolor='white')


@app.route('/<int:c>/<int:r>/<color>/<subcolor>')
def subcolor(c, r, color, subcolor):
    return render_template("index.html", col=c, row=r, color=color, subcolor=subcolor)


if __name__ == "__main__":
    app.run(debug=True)

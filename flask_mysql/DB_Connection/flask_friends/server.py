from flask import Flask, render_template, request, redirect
from friend import Friend
app = Flask(__name__)


@app.route("/show")
def show():
    # call the get all classmethod to get all friends
    friends = Friend.get_all()
    print(friends)
    return render_template("show.html", all_friends=friends)

@app.route("/")
def index():
    return render_template("friends.html")


@app.route('/create_friend', methods=["POST"])
def create_friend():
    # First we make a data dictionary from our request.form coming from our template.
    # The keys in data need to line up exactly with the variables in our query string.
    data = {
    "fname": request.form["fname"],
    "lname": request.form["lname"],
    "occ": request.form["occ"]
    }
# We pass the data dictionary into the save method from the Friend class.
    Friend.save(data)
# Don't forget to redirect after saving to the database.
    return redirect('/show')


if __name__ == "__main__":
    app.run(debug=True)
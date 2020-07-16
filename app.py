from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)


# @app.route('/')
# def home():
#     return render_template("index.html", content="Testing")


@app.route("/login", methods=['POST', 'GET'])
def login():
    if request.method == "POST":
        user = request.form['nm']
        password = request.form["password"]
        if user == "o@gmail.com" and password == "123":
            return redirect(url_for("user", usr=user))
        else:
            return render_template("login.html")
    else:
        return render_template("login.html")

@app.route("/<usr>")
def user(usr):
    # return f"<h1>{usr}</h1>"
    return render_template("employer.html")

@app.route("/post_a_job_employer")
def post_a_job():
    return render_template("post_a_job_employer.html")

@app.route("/my_posts_employer")
def my_posts():
    return render_template("my_posts_employer.html")


@app.route("/edit_profile_employer")
def edit_profile():
    return render_template("edit_profile_employer.html")

@app.route("/profit_employer")
def profit():
    return render_template("profit_employer.html")




if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, redirect, url_for, render_template, request
import json
app = Flask(__name__)


# @app.route('/')
# def home():
#     return render_template("index.html", content="Testing")

with open('countries.json') as json_file:
    data = json.load(json_file)

countries = data.keys()

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

@app.route("/post_a_job_employer", methods=['GET', 'POST'])
def post_a_job():
    if request.method == "POST":
        job_title = request.form['job_title']
        country = request.form["country"]
        city = request.form["city"]
        state = request.form["state"]
        industry = request.form["industry"]
        department = request.form["department"]
        if request.form['submit'] == 'submitt':
            return render_template("my_posts_employer.html")
        elif request.form['submit'] == 'interview':
            return render_template("add_interview_questions.html")
    else:
        # Toast eklenecek
        return render_template("post_a_job_employer.html", countries=countries)

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

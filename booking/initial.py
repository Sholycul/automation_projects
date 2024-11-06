from flask import Flask, render_template
from datetime import datetime
from random import randint
import requests

gender_url = "https://api.genderize.io"

agify_url = "https://api.agify.io"

nationalize_url = "https://api.nationalize.io/"


app = Flask(__name__)


@app.route("/")
def home():
    year = str(datetime.now()).split("-")[0]
    random_num = randint(1, 10)
    return render_template("index.html", curr_year=year, num=random_num)


@app.route("/guess/<name>")
def some_guess(name):
    actual_name = name.title()
    param = {
        "name": name,
    }
    gender_data = requests.get(gender_url, params=param).json()
    gender_value = gender_data["gender"].title()

    age_data = requests.get(agify_url, params=param).json()
    age_value = age_data["age"]

    nationality_data = requests.get(nationalize_url, params=param).json()
    country_value = nationality_data["country"][0]["country_id"].title()
    return render_template("guess.html", gender=gender_value, age=age_value, country=country_value, name=actual_name)


@app.route("/blog")
def blog_post():
    response = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()
    return render_template("blog.html", blog_posts=response)


if __name__ == "__main__":
    app.run(debug=True)


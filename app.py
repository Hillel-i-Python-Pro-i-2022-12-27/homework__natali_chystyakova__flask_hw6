from flask import Flask
from webargs import fields
from webargs.flaskparser import use_args

from application.files_example.average_value_file import average_value_from_csv
from application.files_example.create_text_file import create_txt_file
from application.files_example.generators import generate_users
from application.files_example.number_of_astronauts import number_of_astro
from application.files_example.read_text_file import read_text_file
from application.files_example.request_end_download import get_download_file
from application.files_example.request_end_download import get_requests_data

app = Flask(__name__)


@app.route("/")
def start():  # put application's code here
    return "<h1>start</h1>"


@app.route("/generate-users/")
@use_args({"amount": fields.Int(missing=10)}, location="query")
def generate_users_(args):
    amount = args["amount"]
    users = generate_users(amount=amount)  # put application's code here
    return f"<ol>{''.join(f'<li>{user.name} - {user.email}</li>' for user in users)} </ol>"


@app.route("/get-content/")
def get_content():
    create_txt_file(name_file="fake_text")
    get_content_ = read_text_file(name_file="fake_text")
    return f"<p><blockquote>{get_content_}</blockquote></p>"


@app.route("/space/")
def space():  # put application's code here
    get_requests_data(url="http://api.open-notify.org/astros.json")
    astro_ = number_of_astro(name_file="output")
    return f"<span>{astro_}</span>"


@app.route("/mean/")
def mean():
    url = "https://drive.google.com/uc?export=download&id=1yM0a4CSf0iuAGOGEljdb7qcWyz82RBxl"
    get_download_file(url)
    mean = average_value_from_csv(name_file="output")
    return f"<p><span>{mean}</span></p>"
    # put application's code here


if __name__ == "__main__":
    app.run()

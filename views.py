from flask import Blueprint

views = Blueprint("views")
@views.route("/")
def home():
    return "this is the home page"
from flask import Blueprint, render_template, jsonify, redirect, url_for

views = Blueprint(__name__,"views")


@views.route("/")
def home():
    return render_template("index.html", name="Henry")

@views.route("/profile")
def profile():
    args = request.args
    name = args.get('name')
    return render_template("index.html", name=name)
@views.route("/json")
def get_json():
    return jsonify({'name':'henry','coolness':10})

@views.route('data')
def get_data():
    data = request.json
    return jsonify({'name':'tim', 'coolness':10})
@views.route("/go-to-home")
def go_to_home():
    return redirect(url_for("views.get_json"))
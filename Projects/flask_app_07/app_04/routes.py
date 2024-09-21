import os
import secrets
from PIL import Image
from flask import render_template, url_for, flash, redirect, request
from app_04 import app, db, bcrypt
from app_04.forms import RegistrationForm, LoginForm, UpdateAccountForm
from app_04.models import User, Post
from flask_login import login_user, current_user, logout_user, login_required


# Define a route for the root URL ('/') using the '@app.route' decorator
# This means when a user visits the base URL of the application,
# the 'hello_world' function will be executed
@app.route("/")
def hello_world():
    # Define a function named 'hello_world' that returns the string "Hello, World!"
    return "Hello, World!"


@app.route("/about")
def about():
    return "about me"


@app.route("/blog")
def blog():
    posts = [
        {
            "title": "Blog Post 1",
            "content": "This is the content of blog post 1",
            "author": "Rashid",
            "date_posted": "April 20, 2021",
        },
        {
            "title": "Blog Post 2",
            "content": "This is the content of blog post 2",
            "author": "Rashid",
            "date_posted": "April 21, 2021",
        },
    ]
    return render_template("blog.html", author="Rashid", posts=posts)


@app.route("/blog/<string:blog_id>")
def blog_post(blog_id):
    return f"Blog post with ID: {blog_id}"


@app.route("/register", methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for("blog"))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode(
            "utf-8"
        )
        user = User(
            username=form.username.data, email=form.email.data, password=hashed_password
        )
        db.session.add(user)
        db.session.commit()
        flash(f"Your account is created succesfully, you can login now", "success")
        return redirect(url_for("login"))
    return render_template("register.html", title="Register", form=form)


@app.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("blog"))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get("next")
            return redirect(next_page) if next_page else redirect(url_for("blog"))

        else:
            flash("Login Unsuccessful. Please check username and password", "danger")
    return render_template("login.html", title="Login", form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("blog"))


def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(app.root_path, "static/profile_pics", picture_fn)
    output_size = (125, 125)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)
    return picture_fn


@app.route("/account", methods=["GET", "POST"])
@login_required
def account():
    form = UpdateAccountForm()
    if form.validate_on_submit():
        if form.picture.data:
            picture_file = save_picture(form.picture.data)
            current_user.image_file = picture_file
        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash("Your account has been updated", "success")
        return redirect(url_for("account"))
    elif request.method == "GET":
        form.username.data = current_user.username
        form.email.data = current_user.email
    image_file = url_for("static", filename="profile_pics/" + current_user.image_file)
    return render_template(
        "account.html", title="Account", image_file=image_file, form=form
    )

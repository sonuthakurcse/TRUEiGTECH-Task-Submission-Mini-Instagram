from flask import Blueprint, render_template, redirect, request
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, current_user
from app.extensions import db, login_manager
from app.models.user import User

auth_ka_bp = Blueprint("auth", __name__)

@login_manager.user_loader
def load_banda(user_id):
    return User.query.get(int(user_id))


@auth_ka_bp.route("/login", methods=["GET", "POST"])
def login_page():

    if current_user.is_authenticated:
        return redirect("/feed")

    if request.method == "POST":
        email_wala = request.form["email"]
        pass_wala = request.form["password"]

        banda = User.query.filter_by(email=email_wala).first()

        if banda and check_password_hash(banda.password, pass_wala):
            login_user(banda)
            return redirect("/feed")

    return render_template("login.html")


@auth_ka_bp.route("/signup", methods=["GET", "POST"])
def signup_page():

    if request.method == "POST":
        naya_user = User(
            name=request.form["name"],
            email=request.form["email"],
            password=generate_password_hash(request.form["password"])
        )
        db.session.add(naya_user)
        db.session.commit()
        return redirect("/login")

    return render_template("signup.html")


@auth_ka_bp.route("/logout")
def logout_page():
    logout_user()
    return redirect("/login")

from flask import Blueprint, render_template, redirect, url_for
from flask_login import login_required, current_user
from app.models.post import Post

page_wala_bp = Blueprint("pages", __name__)

@page_wala_bp.route("/")
def ghar_page():
    return redirect(url_for("auth.login_page"))


@page_wala_bp.route("/feed")
@login_required
def feed_page():
    sab_posts = Post.query.order_by(Post.created_at.desc()).all()
    return render_template("feed.html", posts=sab_posts)


@page_wala_bp.route("/create")
@login_required
def create_page():
    return render_template("create_post.html")


@page_wala_bp.route("/profile")
@login_required
def profile_page():
    return render_template("profile.html", user=current_user)

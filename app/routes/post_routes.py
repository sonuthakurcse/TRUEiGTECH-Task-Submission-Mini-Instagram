from flask import Blueprint, request, redirect, current_app
from flask_login import login_required, current_user
from werkzeug.utils import secure_filename
from app.extensions import db
from app.models.post import Post
from app.models.comment import Comment
import os

post_wala_bp = Blueprint("post", __name__)

@post_wala_bp.route("/post/create", methods=["POST"])
@login_required
def post_banana():

    image_file = request.files["image"]
    caption_text = request.form["caption"]

    naam_safe = secure_filename(image_file.filename)
    image_file.save(os.path.join(current_app.config["UPLOAD_FOLDER"], naam_safe))

    naya_post = Post(
        image_url=naam_safe,
        caption=caption_text,
        author=current_user
    )

    db.session.add(naya_post)
    db.session.commit()

    return redirect("/feed")


@post_wala_bp.route("/post/like/<int:post_id>")
@login_required
def like_karna(post_id):

    post_mila = Post.query.get_or_404(post_id)

    if current_user in post_mila.liked_by:
        post_mila.liked_by.remove(current_user)
    else:
        post_mila.liked_by.append(current_user)

    db.session.commit()
    return redirect("/feed")


@post_wala_bp.route("/post/comment/<int:post_id>", methods=["POST"])
@login_required
def comment_karna(post_id):

    comment_text = request.form["comment"]

    naya_comment = Comment(
        text=comment_text,
        user_id=current_user.id,
        post_id=post_id
    )

    db.session.add(naya_comment)
    db.session.commit()

    return redirect("/feed")

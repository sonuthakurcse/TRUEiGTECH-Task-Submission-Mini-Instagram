from flask import Blueprint
from flask_login import login_required, current_user
from app.extensions import db
from app.models.user import User

user_wala_bp = Blueprint("user", __name__)

@user_wala_bp.route("/follow/<int:user_id>")
@login_required
def follow_karna(user_id):

    samne_wala = User.query.get_or_404(user_id)

    if samne_wala != current_user and samne_wala not in current_user.following:
        current_user.following.append(samne_wala)
        db.session.commit()

    return "Followed bhai"

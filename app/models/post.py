from app.extensions import db
from datetime import datetime

likes = db.Table(
    "likes",
    db.Column("user_id", db.Integer, db.ForeignKey("user.id")),
    db.Column("post_id", db.Integer, db.ForeignKey("post.id"))
)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    image_url = db.Column(db.String(300))
    caption = db.Column(db.String(300))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))

    liked_by = db.relationship(
        "User",
        secondary=likes,
        backref="liked_posts"
    )

from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for, flash, abort
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

# --- Config ---
app.config["SECRET_KEY"] = "change-me-in-production"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///blog.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

# --- Model ---
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(180), nullable=False)
    content = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __repr__(self):
        return f"<Post {self.id} - {self.title!r}>"

# --- CLI helper (create the DB file) ---
@app.cli.command("init-db")
def init_db():
    """Initialize the database."""
    db.create_all()
    print("Initialized the database at blog.db")

# --- Routes ---
@app.route("/")
def home():
    # Step 5: Display all posts (latest first)
    posts = Post.query.order_by(Post.created_at.desc()).all()
    return render_template("index.html", posts=posts)

@app.route("/post/<int:post_id>")
def post_detail(post_id):
    # Step 6: Display a single post
    post = Post.query.get_or_404(post_id)
    return render_template("post_detail.html", post=post)

@app.route("/create", methods=["GET", "POST"])
def create():
    # Step 7: Create a post
    if request.method == "POST":
        title = request.form.get("title", "").strip()
        content = request.form.get("content", "").strip()
        if not title or not content:
            flash("Title and content are required.", "error")
            return render_template("form.html", mode="create", post=None)

        post = Post(title=title, content=content)
        db.session.add(post)
        db.session.commit()
        flash("Post created!", "success")
        return redirect(url_for("post_detail", post_id=post.id))
    return render_template("form.html", mode="create", post=None)

@app.route("/edit/<int:post_id>", methods=["GET", "POST"])
def edit(post_id):
    # Step 7: Edit a post
    post = Post.query.get_or_404(post_id)
    if request.method == "POST":
        title = request.form.get("title", "").strip()
        content = request.form.get("content", "").strip()
        if not title or not content:
            flash("Title and content are required.", "error")
            return render_template("form.html", mode="edit", post=post)

        post.title = title
        post.content = content
        db.session.commit()
        flash("Post updated!", "success")
        return redirect(url_for("post_detail", post_id=post.id))
    return render_template("form.html", mode="edit", post=post)

@app.route("/delete/<int:post_id>", methods=["POST"])
def delete(post_id):
    # Step 7: Delete a post
    post = Post.query.get_or_404(post_id)
    db.session.delete(post)
    db.session.commit()
    flash("Post deleted.", "success")
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5050, debug=True)

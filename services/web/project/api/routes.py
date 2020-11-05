from flask import Blueprint, jsonify, request
from flask_login import login_required

from project import db
from project.model import Post

api = Blueprint('api', __name__, url_prefix='/api')


@api.route('/posts/<int:count>', methods=['GET'])
@login_required
def get_posts(count):
    if count:
        posts = Post.query.order_by(Post.id.desc()).limit(10)
    else:
        posts = Post.query.all()
    posts = [{
        'id': post.id,
        'title': post.title,
        'description': post.description
    } for post in posts]
    return jsonify(success=True, posts=posts)


@api.route('/post/new', methods=['POST'])
def create_post():
    title = request.form['title']
    description = request.form['description']
    body = request.form['body']

    new_post = Post(
        title=title,
        description=description,
        body=body
    )
    db.session.add(new_post)
    db.session.commit()

    return jsonify(success=True)


@api.route('/post/<int:i_id>', methods=['GET', 'DELETE'])
def post(i_id):
    if request.method == 'GET':
        post_data = Post.query.filter_by(id=i_id).first()
        return jsonify(
            success=True,
            title=post_data.title,
            body=post_data.body
        )
    elif request.method == 'DELETE':
        post_to_delete = Post.query.filter_by(id=i_id).first()
        db.session.delete(post_to_delete)
        db.session.commit()
        return jsonify(success=True)

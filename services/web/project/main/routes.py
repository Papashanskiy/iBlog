from flask import Blueprint, render_template, jsonify, abort, request, current_app
from flask_login import login_required
from project.model import User, Post
from project import db, bcrypt

main = Blueprint('main', __name__)


@main.errorhandler(400)
def custom400(error):
    response = jsonify({'message': error.description})


@main.route('/')
@main.route('/index')
@login_required
def index():
    return render_template('main/index.html')


@main.route("/api/protect/create_db", methods=['GET'])
def create_db():
    db.drop_all()
    db.create_all()
    db.session.commit()
    return jsonify(success=True)


@main.route("/api/protect/create_admin_user")
def create_admin_user():
    admin = User(
        username='admin',
        email=current_app.config['ADMINS'][0],
        password=bcrypt.generate_password_hash(current_app.config['ADMINS_PWD'][0]),
        role='Admin'
    )
    db.session.add(admin)
    db.session.commit()
    return jsonify(success=True)


@main.route('/post/new', methods=['GET'])
@login_required
def create_post():
    return render_template('main/create_post.html')


@main.route('/post/<int:i_id>', methods=['GET'])
@login_required
def post(i_id):
    return render_template('main/post.html', id=i_id)

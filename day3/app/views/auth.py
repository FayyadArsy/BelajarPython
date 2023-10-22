from flask_restx import Namespace, Resource, fields
from flask import request
from flask
from http import HTTPStatus
from utils import db
from ..models.users import Users
from ..logs.log import logger

auth_ns = Namespace('auth', 'Namespace for auth')

auth_model = auth_ns.model(
    'Users', {
        'id': fields.Integer(description = "ini adalah user id"),
        'username': fields.String(description = "ini adalah username"),
        'password': fields.String(description = "ini adalah password"),
    }
)

@auth_ns.route('/signup')
class Signup(Resource):
    @auth_ns.doc(
        description = "Sign up for user"
    )
@auth_ns.route('/signin')
class Signin(Resource):
    @auth_ns.expect(auth_model)
    @auth_ns.doc(
        description = 'Sign in for user'
    )
    def post(self):
        """An sign in for new accoung"""
        data = request.get_json()

        try:
            user = User.query.filter_by(username = data.get('username')).first()
            check_password = check_password_hash(user.password, data.get('password'))
            logger.info(f"check_password: {check_password}")
            return [], HTTPStatus.OK
        except Exception as e:
            print("Error get:", e)
            return [], HTTPStatus.BAD_REQUEST

@auth_ns.route('/refresh')
class Refresh(Resource):
    @jwt_required(refresh=True)
    def post(self):
        """Refresh JWT Token"""
        try:
            username = get_jwt_identity()
            access_token = create_access_token(identity = username)
            esponse = {'access_token' : access_token}, HTTPStatus.OK
        except Exception as e:
            print("Error refresh :", e)
            return [], HTTPStatus.BAD_REQUEST
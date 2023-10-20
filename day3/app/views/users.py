from flask_restx import Namespace, Resource, fields
from flask import request
from ..utils import db
from ..models.users import Users
from http import HTTPStatus
from ..logs.log import logger

users_ns = Namespace('users', 'Namespace for users')
users_model = users_ns.model(
    'Users', {
        'id': fields.Integer(description = "Ini adalah user id"),
        'username': fields.String(description = "Ini adalah user name"),
        'password': fields.String(description = "Ini adalah user password"),
    }
)

@users_ns.route('/')
class UserGetPost(Resource):
    @users_ns.marshal_list_with(users_model)
    @users_ns.doc(
        description = "Get all users"
    )
    def get(self):
        """Get All Data Users"""
        try:
        # return {"Status": 200, "Data": []}
            data_users = Users.query.all()
            print("data berhasil:", data_users)
            logger.info(f"Data User: {data_users}")
            return data_users, HTTPStatus.OK
        except Exception as e:
            print("error:", e)
            return [], 400
    

    @users_ns.expect(users_model)
    @users_ns.marshal_with(users_model)
    @users_ns.doc(
        description = "Create new user."
    )
    def post(self):
        """Create new user data."""
        try:
            new_user = request.get_json()
            print(f"data: {new_user}")
        
            new_input_user = Users(
                username = new_user.get('username'),
                password = new_user.get('password')
            )
            
            db.session.add(new_input_user)
            db.session.commit()
            logger.info(f"Input User: {new_user}")
            return [], HTTPStatus.OK
        except Exception as e:
            print("Error post: ", e)
            return [], HTTPStatus.BAD_REQUEST

    
@users_ns.route('/<int:user_id>')
class UserGetPutDelete(Resource):
    @users_ns.marshal_list_with(users_model)
    @users_ns.doc(
        description = "Get users by id",
        params = {
            "user_id" : "An Id a given user frm metod get by id"
        }
    )
    def get(self, user_id):
        """Get All Data Users"""
        try:
        # return {"Status": 200, "Data": []}
            data_by_id = Users.query.get_or_404(user_id)
            print("data berhasil:", data_by_id)

            return data_by_id, HTTPStatus.OK
        except Exception as e:
            print("error:", e)
            return [], 400
            
    @users_ns.expect(users_model)
    @users_ns.marshal_with(users_model)
    @users_ns.doc(
        description = "Update certain user's data",
        params = {
            "user_id" : "ID of user used to update data"
        }
    )
    def put(self, user_id):
        """update User"""
        try:
            user_to_update = Users.query.get_or_404(user_id)

            data = users_ns.payload

            user_to_update.username = data['username']
            user_to_update.password = data['password']

            db.session.commit()

            return [], HTTPStatus.OK
        except Exception as e:
            print("Error update by uid", e)
            return [], HTTPStatus.BAD_REQUEST
    
    @users_ns.marshal_list_with(users_model)
    @users_ns.doc(
        description = "Delete by id",
        param = {
            "user_id" : "And id to delete"
        }
    )
    def delete (self, user_id):
        """Delete"""
        try:
            user_to_delete = Users.query.get.get_or_404(user_id)

            db.session.delete(user_to_delete)
            db.session.commit()
            return [], HTTPStatus.OK
        
        except Exception as e:
            print("error delete by id", e)
            return [], HTTPStatus.BAD_REQUEST
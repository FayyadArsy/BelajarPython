from flask_restx import Namespace, Resource, fields
users_ns = Namespace('users', 'Namespace for users')
users_model = users_ns.model(
    'Users', {
        'id': fields.Integer(description = "Ini adalah user id"),
        'isername': fields.String(description = "Ini adalah user name"),
        'password': fields.String(description = "Ini adalah user password"),
    }
)

@users_ns.route('/')
class UserGetPost(Resource):
    @users_ns.doc(
        description = "Get all users"
    )
    def get(self):
        return {"Status": 200, "Data": []}
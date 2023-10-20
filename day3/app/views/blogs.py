from flask_restx import Namespace, Resource, fields
from flask import request
from ..utils import db
from ..models.blogs import Blogs
from http import HTTPStatus

blogs_ns = Namespace('blogs', 'Namespace for blogs')
blogs_model = blogs_ns.model(
    'Blogs', {
        'id': fields.Integer(description = "Ini adalah user id"),
        'username': fields.String(description = "Ini adalah user name"),
        'password': fields.String(description = "Ini adalah user password"),
    }
)
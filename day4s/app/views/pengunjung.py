from flask_restx import Namespace, Resource, fields
from flask import request
from ..utils import db
from .models.pengunjung import Pengunjung
from http import HTTPStatus

pengunjung_ns =Namespace('pengunjung', 'Namespace for pengunjung')
pengunjung_model = users_ns.model(
    'Users', {
        'id': fields.Integer(description = "Ini adalah user id"),
        'username': fields.String(description = "Ini adalah user name"),
        'password': fields.String(description = "Ini adalah user password"),
    }
)

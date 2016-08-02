from functools import wraps
from flask import g, request, redirect, url_for
from errors import Errors

class Auth():
    @staticmethod
    def auth_required(f):
        @wraps(f)
        def auth_function(*args, **kwargs):
            if request.headers.get('auth') != 'nlp':
                return Errors.unauthorized()
            return f(*args, **kwargs)
        return auth_function

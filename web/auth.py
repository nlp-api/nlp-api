from functools import wraps
from flask import g, request, redirect, url_for
from errors import Errors
import redis

r = redis.StrictRedis(host='localhost', port=6379, db=0)

class Auth():
    @staticmethod
    def auth_required(f):
        @wraps(f)
        def auth_function(*args, **kwargs):
            user = r.get(request.headers.get('auth'))
            print(user)
            if user == None:
                return Errors.unauthorized()
            return f(*args, **kwargs)
        return auth_function

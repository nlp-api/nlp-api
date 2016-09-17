from functools import wraps
from flask import g, request, redirect, url_for
from errors import Errors
import redis

# Default redis connection - break out into config
r = redis.StrictRedis(host='localhost', port=6379, db=0)

# Enable/Disable auth - break out into config
AUTH_ENABLED = False

class Auth():
    @staticmethod
    def auth_required(f):
        @wraps(f)
        def auth_function(*args, **kwargs):
            if AUTH_ENABLED == True:
                user = r.get(request.headers.get('Authorization'))
                print(user)
                if user == None:
                    return Errors.unauthorized()
            else:
                return f(*args, **kwargs)
        return auth_function

from flask import Flask, request, jsonify

class Errors():
    @staticmethod
    def not_found(error=None):
        message = {
                'status': 404,
                'message': 'Not Found: ' + request.url,
        }
        resp = jsonify(message)
        resp.status_code = 404
        return resp

    @staticmethod
    def bad_request(error=None):
        message = {
                'status': 400,
                'message': 'Could not parse json, check formatting: ' + request.url,
        }
        resp = jsonify(message)
        resp.status_code = 400
        return resp

    @staticmethod
    def unauthorized(error=None):
        message = {
                'status': 401,
                'message': 'Unauthorized, check auth token: ' + request.url,
        }
        resp = jsonify(message)
        resp.status_code = 401
        return resp

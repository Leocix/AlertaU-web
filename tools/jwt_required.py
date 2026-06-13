from functools import wraps
from flask import request, jsonify
from tools.jwt_utils import verificar_token

def jwt_token_requerido(f):
    @wraps(f)
    def envoltura(*args, **kwargs):
        token = None
        if not request.headers.get("Authorization"):
            return jsonify({'status': False, 'data': None, 'message': 'Cabecera no válida'}), 401

        try:
            token = request.headers.get("Authorization").split('Bearer ')[1]
        except IndexError:
            return jsonify({'status': False, 'data': None, 'message': 'Formato de token inválido'}), 401

        if not token:
            return jsonify({'status': False, 'data': None, 'message': 'Token requerido'}), 401

        payload = verificar_token(token)
        if not payload:
            return jsonify({'status': False, 'data': None, 'message': 'Token inválido o expirado'}), 401

        return f(*args, **kwargs)
    return envoltura

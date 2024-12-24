from flask import jsonify

def success_response(data=None, message="Request was successful", status_code=200):
    """
    Standardized success response.
    """
    response = {
        'status': 'success',
        'message': message,
        'data': data if data else {}
    }
    return jsonify(response), status_code


def error_response(message="An error occurred", status_code=400, error_details=None):
    """
    Standardized error response.
    """
    response = {
        'status': 'error',
        'message': message,
        'details': error_details if error_details else {}
    }
    return jsonify(response), status_code

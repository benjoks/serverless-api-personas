import json

def response_success(message, description):
    body = {
        "statusCode": 200,
        "message": message,
        "description": description
        }
    return {
        "isBase64Encoded": False,
        "statusCode": 200,
        "headers": {"Access-Control-Allow-Origin": "*"},
        "body": json.dumps(body)
    }

def response_success_data(message, description,data):
    body = {
        "statusCode": 200,
        "message": message,
        "description": description,
        "data":data
        }
    return {
        "isBase64Encoded": False,
        "statusCode": 200,
        "headers": {"Access-Control-Allow-Origin": "*"},
        "body": json.dumps(body)
    }

def response_bad_request(message, description):
    body = {
        "statusCode": 400,
        "message": message,
        "description": description
        }
    return {
        "isBase64Encoded": False,
        "statusCode": 400,
        "headers": {"Access-Control-Allow-Origin": "*"},
        "body": json.dumps(body)
    }

def response_not_found(message, description):
    body = {
        "statusCode": 404,
        "message": message,
        "description": description
        }
    return {
        "isBase64Encoded": False,
        "statusCode": 404,
        "headers": {"Access-Control-Allow-Origin": "*"},
        "body": json.dumps(body)
    }

def response_server_error(message, description):
    body = {
        "statusCode": 500,
        "message": message,
        "description": description
        }
    return {
        "isBase64Encoded": False,
        "statusCode": 500,
        "headers": {"Access-Control-Allow-Origin": "*"},
        "body": json.dumps(body)
    }

def response_conflict(message, description):
    body = {
        "statusCode": 409,
        "message": message,
        "description": description
        }
    return {
        "isBase64Encoded": False,
        "statusCode": 409,
        "headers": {"Access-Control-Allow-Origin": "*"},
        "body": json.dumps(body)
    }

template = {
    "swagger": "2.0",
    "info": {
        "title": "Dukka Backend Test",
        "description": "Transaction Receipt Generation endpoints",
        "contact": {
            "email": "nickifeajika@gmail.com",
            "url": "github.com/cybermind-nick"
        },
        "termsOfService": "github.com/cybermind-nick",
        "version": "1.0"
    },
    "basePath": "/user",
    "schemes": [
        "http",
        "https"
    ],
    "securityDefinitions": {
        "Bearer": {
            "type": "apiKey",
            "name": "Authorization",
            "in": "header",
            "description": '''JWT Authorization header using the Bearer
            scheme.'''
        }
    },  
}

swagger_config = {
    "headers": [

    ],
    "specs": [
        {
            "endpoint": 'apispec',
            "route": 'apispec.json',
            "rule_filter": lambda rule: True,
            "model_filter": lambda tag: True
        }
    ],
    "static_url_path": "/flasgger_static",
    "swagger_ui": True,
    "specs_route": "/"
}
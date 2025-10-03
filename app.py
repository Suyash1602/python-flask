import os

from flask import Flask, jsonify
from flask_smorest import Api
from flask_jwt_extended import JWTManager

from db import db
from blocklist import BLOCKLIST
import models

from resources.item import blp as ItemBlueprint
from resources.store import blp as StoreBlueprint
from resources.tag import blp as TagBlueprint
from resources.user import blp as UserBlueprint

def create_app(db_url=None):
    # Create and configure the Flask application
    app  = Flask(__name__)

    # General configuration
    app.config["PROPAGATE_EXCEPTIONS"] = True
    app.config["API_TITLE"] = "Stores REST API"
    app.config["API_VERSION"] = "v1"
    app.config["OPENAPI_VERSION"] = "3.0.3"
    app.config["OPENAPI_URL_PREFIX"] = "/"
    app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
    app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
    app.config["SQLALCHEMY_DATABASE_URI"] = db_url or os.getenv("DATABASE_URL","sqlite:///data.db")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)

    # Initialize Flask-Smorest API
    api = Api(app)

    # Add JWT bearer security scheme to OpenAPI/Swagger spec
    api.spec.components.security_scheme(
        "bearerAuth",
        {
            "type": "http",
            "scheme": "bearer",
            "bearerFormat": "JWT",
        },
    )
    api.spec.security = [{"bearerAuth": []}]

    # JWT configuration
    app.config["JWT_SECRET_KEY"] = "suss"
    jwt = JWTManager(app)

    # Blocklist check for revoked tokens
    @jwt.token_in_blocklist_loader
    def check_if_token_in_blocklist(jwt_header, jwt_payload):
        return jwt_payload["jti"] in BLOCKLIST
    
    # Handler for revoked tokens
    @jwt.revoked_token_loader
    def revoked_token_callback(jwt_header, jwt_payload):
        return (
            jsonify({"message": "The token has been revoked.", "error": "token_revoked"}),  
            401,
        )

    # Add custom claims to JWT (admin flag)
    @jwt.additional_claims_loader
    def add_claims_to_jwt(identity):
        if str(identity) == "1":
            return {"is_admin": True}
        return {"is_admin": False}

    # Handler for expired tokens
    @jwt.expired_token_loader
    def expired_token_callback(jwt_header, jwt_payload):
        return (
            {"message": "The token has expired.", "error": "token_expired"},
            401,
        )

    # Handler for invalid tokens
    @jwt.invalid_token_loader
    def invalid_token_callback(error):
        return (
            {"message": "Signature verification failed.", "error": "invalid_token"},
            401,
        )

    # Handler for missing tokens
    @jwt.unauthorized_loader
    def missing_token_callback(error):
        return (
            {
                "description": "Request does not contain an access token.",
                "error": "authorization_required",
            },
            401,
        )

    # Create database tables at startup
    with app.app_context():
        db.create_all()

    # Register blueprints for each resource
    api.register_blueprint(ItemBlueprint)
    api.register_blueprint(StoreBlueprint)
    api.register_blueprint(TagBlueprint)
    api.register_blueprint(UserBlueprint)

    return app

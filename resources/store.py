import uuid
from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort

from sqlalchemy.exc import SQLAlchemyError, IntegrityError  # type: ignore

from db import db
from models import StoreModel
from schemas import StoreSchema


blp = Blueprint("Stores",__name__,description="Operations on stores")

# API for single store operations (GET, DELETE)
@blp.route("/store/<string:store_id>")
class Store(MethodView):
    # Retrieve a store by its ID
    @blp.response(200,StoreSchema)
    def get(self,store_id):
        store = StoreModel.query.get_or_404(store_id)
        return store

    # Delete a store by its ID
    def delete(self,store_id):
        store = StoreModel.query.get_or_404(store_id)
        db.session.delete(store)
        db.session.commit()
        return {"message":"Store deleted."}
        
# API for store collection operations (GET all, POST new)
@blp.route("/store")
class StoreList(MethodView):
    # Retrieve all stores
    @blp.response(200,StoreSchema(many=True))
    def get(self):
        return StoreModel.query.all()
    
    # Create a new store
    @blp.arguments(StoreSchema)
    @blp.response(201,StoreSchema)
    def post(self,store_data):
        store = StoreModel(**store_data)

        try:
            db.session.add(store)
            db.session.commit()
            db.session.refresh(store) 
        except IntegrityError:
            abort(400,message="A store with that name already exists.")
        except SQLAlchemyError: # type: ignore
            abort(500,message="An error occurred while inserting the store.")

        return store
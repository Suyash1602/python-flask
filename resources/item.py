import uuid
from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError   

from db import db
from models import ItemModel
from schemas import ItemSchema,ItemUpdateSchema


blp = Blueprint("Items",__name__,description="Operations on items")

# API for single item operations (GET, DELETE, PUT)
@blp.route("/item/<string:item_id>")
class Item(MethodView):
    # Retrieve an item by its ID
    @blp.response(200,ItemSchema)
    def get(self,item_id):
        item = ItemModel.query.get_or_404(item_id)
        return item

    # Delete an item by its ID
    def delete(self,item_id):
        item = ItemModel.query.get_or_404(item_id)
        db.session.delete(item)
        db.session.commit()
        return {"message":"Item deleted."}

    # Update an item by its ID
    @blp.arguments(ItemUpdateSchema)  
    @blp.response(200,ItemSchema)
    def put(self,item_data,item_id):
        item = ItemModel.query.get(item_id)
        if item:
            item.price = item_data["price"]
            item.name = item_data["name"]
        else:
            item = ItemModel(id = item_id,**item_data)

        db.session.add(item)
        db.session.commit()
        db.session.refresh(item)

        return item


# API for item collection operations (GET all, POST new)
@blp.route("/item")
class ItemList(MethodView):
    # Retrieve all items
    @blp.response(200,ItemSchema(many=True))
    def get(self):
        return ItemModel.query.all()

    # Create a new item
    @blp.arguments(ItemSchema)
    @blp.response(201, ItemSchema)
    def post(self, item_data):
        item = ItemModel(**item_data)

        try:
            db.session.add(item)
            db.session.commit()
            db.session.refresh(item)  # <-- Add this line
        except SQLAlchemyError:
            abort(500, message="An error occurred while inserting the item.")

        return item
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from flask_jwt_extended import jwt_required,get_jwt
from sqlalchemy.exc import SQLAlchemyError   

from db import db
from models import ItemModel
from schemas import ItemSchema,ItemUpdateSchema

# Blueprint for item-related operations
blp = Blueprint("Items",__name__,description="Operations on items")

# Routes for single item operations
@blp.route("/item/<int:item_id>")
class Item(MethodView):
    # Get an item by its ID (requires JWT)
    @jwt_required()
    @blp.response(200,ItemSchema)
    def get(self,item_id):
        item = ItemModel.query.get_or_404(item_id)
        return item

    # Delete an item by its ID (admin only, requires JWT)
    @jwt_required()
    def delete(self,item_id):
        jwt = get_jwt()
        if not jwt.get("is_admin"):
            abort(401,message="Admin privilege required.")
            
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

# Routes for item collection operations
@blp.route("/item")
class ItemList(MethodView):
    # Get all items (requires JWT)
    @jwt_required()
    @blp.response(200,ItemSchema(many=True))
    def get(self):
        return ItemModel.query.all()

    # Create a new item (requires JWT)
    @jwt_required()
    @blp.arguments(ItemSchema)
    @blp.response(201, ItemSchema)
    def post(self, item_data):
        item = ItemModel(**item_data)

        try:
            db.session.add(item)
            db.session.commit()
            db.session.refresh(item)
        except SQLAlchemyError:
            abort(500, message="An error occurred while inserting the item.")

        return item
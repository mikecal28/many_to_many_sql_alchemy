import uuid
from sqlalchemy.dialects.postgresql import UUID
from db import db
import marshmallow as ma


class Orders(db.Model):
    __tablename__ = "orders"
    order_id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    product_id = db.Column(
        UUID(as_uuid=True), db.ForeignKey("products.product_id"), nullable=False
    )
    quantity = db.Column(db.String(), nullable=False)
    active = db.Column(db.Boolean(), default=True)

    def __init__(self, order_id, product_id, quantity, active):
        self.order_id = order_id
        self.product_id = product_id
        self.quantity = quantity
        self.active = active


class OrdersSchema(ma.Schema):
    class Meta:
        fields = [
            "order_id",
            "product_id",
            "quantity",
            "active",
        ]


order_schema = OrdersSchema()
orders_schema = OrdersSchema(many=True)

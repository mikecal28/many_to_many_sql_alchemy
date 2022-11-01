import uuid
from sqlalchemy.dialects.postgresql import UUID
from db import db
import marshmallow as ma


class Products(db.Model):
    __tablename__ = "products"
    product_id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = db.Column(db.String(), nullable=False)
    org_id = db.Column(
        UUID(as_uuid=True), db.ForeignKey("organizations.org_id"), nullable=False
    )
    active = db.Column(db.Boolean(), default=True)

    def __init__(self, product_id, name, org_id, active):
        self.product_id = product_id
        self.name = name
        self.org_id = org_id
        self.active = active


class ProductsSchema(ma.Schema):
    class Meta:
        fields = [
            "product_id",
            "name",
            "org_id",
            "active",
        ]


product_schema = ProductsSchema()
products_schema = ProductsSchema(many=True)

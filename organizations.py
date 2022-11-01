from email.policy import default
import uuid
from sqlalchemy.dialects.postgresql import UUID
from db import db
import marshmallow as ma


class Organizations(db.Model):
    __tablename__ = "organizations"
    org_id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = db.Column(db.String(), nullable=False)
    phone = db.Column(db.String())
    city = db.Column(db.String())
    state = db.Column(db.String())
    active = db.Column(db.Boolean(), default=True)

    # Connections:
    user = db.relationship("Users", back_populates="organization", lazy=True)
    organization_products = db.relationship(
        "Products", back_populates="organization", lazy=True
    )

    def __init__(self, name, phone, city, state, active):
        self.name = name
        self.phone = phone
        self.city = city
        self.state = state
        self.active = active


class OrganizationsSchema(ma.Schema):
    class Meta:
        fields = [
            "org_id",
            "name",
            "phone",
            "city",
            "state",
            "users",
            "organization_products",
            "active",
        ]

    users = ma.fields.Nested("UsersSchema")
    organization_products = ma.fields.Nested("ProductsSchema")


organization_schema = OrganizationsSchema()
organizations_schema = OrganizationsSchema(many=True)

import uuid
from sqlalchemy.dialects.postgresql import UUID
from db import db
import marshmallow as ma


class Transactions(db.Model):
    __tablename__ = "transactions"
    transaction_id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = db.Column(
        UUID(as_uuid=True), db.ForeignKey("users.user_id"), nullable=False
    )
    purchase_date = db.Column(db.String(), nullable=False)
    active = db.Column(db.Boolean(), default=True)

    # Connections:
    user = db.relationship("Users", back_populates="user_transactions", lazy=True)
    order = db.relationship("Orders", back_populates="transaction", secondary="" lazy=True)

    def __init__(self, transaction_id, product_id, user_id, purchase_date, active):
        self.transaction_id = transaction_id
        self.product_id = product_id
        self.user_id = user_id
        self.purchase_date = purchase_date
        self.active = active


class TransactionsSchema(ma.Schema):
    class Meta:
        fields = [
            "transaction_id",
            "user",
            "order",
            "purchase_date",
            "active",
        ]

    user = ma.fields.Nested("UsersSchema")
    order = ma.fields.Nested("OrdersSchema")


transaction_schema = TransactionsSchema()
transactions_schema = TransactionsSchema(many=True)

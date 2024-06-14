from ninja import Schema
from pydantic import Field
from datetime import datetime

class InventorySchema(Schema):
    id: int
    condition: str
    description: str
    title: str
    brand: str
    price: float
    product_type: str
    custom_label_0: str
    timestamp: str = Field(..., alias="timestamp", description="The timestamp of the inventory item")

    @classmethod
    def from_orm(cls, obj):
        return cls(
            id=obj.id,
            condition=obj.condition,
            description=obj.description,
            title=obj.title,
            brand=obj.brand,
            price=obj.price,
            product_type=obj.product_type,
            custom_label_0=obj.custom_label_0,
            timestamp=obj.timestamp.strftime('%Y-%m-%d %H:%M:%S')
        )

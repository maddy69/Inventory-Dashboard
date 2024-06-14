from datetime import date, timedelta
from typing import List, Optional
from ninja import NinjaAPI
from .models import Inventory
from .schemas import InventorySchema

api = NinjaAPI()

def apply_duration_filter(queryset, duration):
    today = date.today()
    if duration == "lastMonth":
        start_date = today.replace(day=1) - timedelta(days=1)
        end_date = start_date.replace(day=1)
    elif duration == "thisMonth":
        start_date = today.replace(day=1)
        end_date = today
    elif duration == "last3Months":
        start_date = today - timedelta(days=90)
        end_date = today
    elif duration == "last6Months":
        start_date = today - timedelta(days=180)
        end_date = today
    elif duration == "thisYear":
        start_date = today.replace(month=1, day=1)
        end_date = today
    elif duration == "lastYear":
        start_date = today.replace(year=today.year - 1, month=1, day=1)
        end_date = today.replace(year=today.year - 1, month=12, day=31)
    else:
        return queryset

    return queryset.filter(date__range=[start_date, end_date])

@api.get("/inventory/", response=List[InventorySchema])
def list_inventory(request):
    return [InventorySchema.from_orm(item) for item in Inventory.objects.all()]

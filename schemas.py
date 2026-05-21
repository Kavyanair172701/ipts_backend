from pydantic import BaseModel
from datetime import date
from decimal import Decimal


class IonCreate(BaseModel):
    ion_no: str
    ion_date: date
    department: str
    work_name: str
    vendor_name: str
    po_no: str | None = None
    po_date: date | None = None
    total_amount: Decimal
    remarks: str | None = None


class IonResponse(IonCreate):
    ion_id: int
    paid_amount: Decimal
    balance_amount: Decimal
    status: str
    status_colour: str

    class Config:
        from_attributes = True
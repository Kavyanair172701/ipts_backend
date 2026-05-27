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


class UserCreate(BaseModel):
    username: str
    password: str
    first_name: str | None = None
    last_name: str | None = None
    mobile_no: str | None = None
    email: str | None = None
    is_superuser: int = 0
    is_staff: int = 0
    is_active: int = 1


class UserLogin(BaseModel):
    username: str
    password: str
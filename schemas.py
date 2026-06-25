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

class VendorBase(BaseModel):
    vendor_name: str
    vendor_code: str | None = None
    vendor_type: str | None = None
    contact_person: str | None = None
    mobile_no: str | None = None
    alternate_no: str | None = None
    email_id: str | None = None
    address: str | None = None
    city: str | None = None
    state: str | None = None
    pincode: str | None = None
    pan_number: str | None = None
    gst_no: str | None = None
    bank_name: str |None = None
    account_number: str | None = None
    ifsc_code: str | None = None
    account_type: str | None = None
    status: str = "ACTIVE"
    remarks: str | None = None


class VendorCreate(VendorBase):
    pass


class VendorUpdate(VendorBase):
    pass


class VendorResponse(VendorBase):
    vendor_id: int

    class Config:
        from_attributes = True


class PurchaseOrderCreate(BaseModel):
    company_name: str = ""
    po_date: str = ""
    po_ref_no: str = ""

    vendor_name: str = ""
    vendor_address: str = ""

    gstin: str = ""
    kind_attention: str = ""

    proforma_invoice_no: str = ""

    project_name: str = ""

    duration_from: str = ""
    duration_to: str = ""

    amount: float = 0

    gst_percent: float = 18
    gst_amount: float = 0

    grand_total: float = 0

    amount_words: str = ""

    payment_terms: str = ""

    cheque_favour: str = ""
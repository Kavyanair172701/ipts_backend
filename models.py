from sqlalchemy import Column, Integer, String, Date,Float, DECIMAL, Text, TIMESTAMP
from sqlalchemy.sql import func
from database import Base

class VendorMaster(Base):
    __tablename__ = "vendor_master"

    vendor_id = Column(Integer, primary_key=True, index=True)
    vendor_name = Column(String(200), nullable=False)
    contact_person = Column(String(150))
    mobile_no = Column(String(20))
    email_id = Column(String(150))
    gst_no = Column(String(50))
    address = Column(Text)
    status = Column(String(20), default="ACTIVE")
    created_at = Column(TIMESTAMP, server_default=func.now())

    vendor_code = Column(String(50))
    vendor_type = Column(String(100))
    alternate_no = Column(String(20))
    city = Column(String(100))
    state = Column(String(100))
    pincode = Column(String(20))
    pan_number = Column(String(50))
    bank_name = Column(String(100))
    account_number = Column(String(50))
    ifsc_code = Column(String(50))
    account_type = Column(String(50))
    remarks = Column(Text)

class IonMaster(Base):
    __tablename__ = "ion_master"

    ion_id = Column(Integer, primary_key=True, index=True)
    ion_no = Column(String(50), unique=True, nullable=False)
    ion_date = Column(Date, nullable=False)
    department = Column(String(100))
    work_name = Column(String(200))
    vendor_name = Column(String(200))
    po_no = Column(String(100))
    po_date = Column(Date)
    total_amount = Column(DECIMAL(12, 2), default=0)
    paid_amount = Column(DECIMAL(12, 2), default=0)
    balance_amount = Column(DECIMAL(12, 2), default=0)
    status = Column(String(50), default="CREATED")
    status_colour = Column(String(20), default="WHITE")
    prepared_date = Column(Date)
    sent_to_management_date = Column(Date)
    management_signed_date = Column(Date)
    received_from_management_date = Column(Date)
    sent_to_finance_date = Column(Date)
    remarks = Column(Text)
    created_at = Column(TIMESTAMP, server_default=func.now())


class UserMaster(Base):
    __tablename__ = "user_master"

    id = Column(Integer, primary_key=True, index=True)
    password = Column(String(255), nullable=False)
    last_login = Column(TIMESTAMP, nullable=True)
    is_superuser = Column(Integer, default=0)
    username = Column(String(150), unique=True, nullable=False)
    first_name = Column(String(150))
    last_name = Column(String(150))
    mobile_no = Column(String(20))
    email = Column(String(200))
    is_staff = Column(Integer, default=0)
    is_active = Column(Integer, default=1)
    date_joined = Column(TIMESTAMP, server_default=func.now())

class RSP(Base):
    __tablename__ = "rsp"

    rsp_id = Column(Integer, primary_key=True, index=True)

    title_type = Column(String(100))
    company_name = Column(String(255))
    rsp_date = Column(String(50))

    vendor_name = Column(String(255))
    cheque_name = Column(String(255))
    project_name = Column(String(255))
    work_name = Column(String(255))

    invoice_type = Column(String(100))
    invoice_no = Column(String(100))
    invoice_date = Column(String(50))

    amount_payable = Column(Float)
    amount_words = Column(String(500))
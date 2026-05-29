from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models import VendorMaster

router = APIRouter()


@router.post("/create")
def create_vendor(
    vendor_name: str,
    vendor_code: str = None,
    vendor_type: str = None,
    contact_person: str = None,
    mobile_no: str = None,
    alternate_no: str = None,
    email_id: str = None,
    address: str = None,
    city: str = None,
    state: str = None,
    pincode: str = None,
    pan_number: str = None,
    gst_no: str = None,
    bank_name: str = None,
    account_number: str = None,
    ifsc_code: str = None,
    account_type: str = None,
    status: str = "ACTIVE",
    remarks: str = None,
    db: Session = Depends(get_db)
):
    vendor = VendorMaster(
        vendor_name=vendor_name,
        vendor_code=vendor_code,
        vendor_type=vendor_type,
        contact_person=contact_person,
        mobile_no=mobile_no,
        alternate_no=alternate_no,
        email_id=email_id,
        address=address,
        city=city,
        state=state,
        pincode=pincode,
        pan_number=pan_number,
        gst_no=gst_no,
        bank_name=bank_name,
        account_number=account_number,
        ifsc_code=ifsc_code,
        account_type=account_type,
        status=status,
        remarks=remarks
    )

    db.add(vendor)
    db.commit()
    db.refresh(vendor)
    return vendor


@router.get("/")
def get_vendors(db: Session = Depends(get_db)):
    return db.query(VendorMaster).all()


@router.put("/update/{vendor_id}")
def update_vendor(
    vendor_id: int,
    vendor_name: str,
    vendor_code: str = None,
    vendor_type: str = None,
    contact_person: str = None,
    mobile_no: str = None,
    alternate_no: str = None,
    email_id: str = None,
    address: str = None,
    city: str = None,
    state: str = None,
    pincode: str = None,
    pan_number: str = None,
    gst_no: str = None,
    bank_name: str = None,
    account_number: str = None,
    ifsc_code: str = None,
    account_type: str = None,
    status: str = "ACTIVE",
    remarks: str = None,
    db: Session = Depends(get_db)
):
    db_vendor = db.query(VendorMaster).filter(VendorMaster.vendor_id == vendor_id).first()

    if not db_vendor:
        raise HTTPException(status_code=404, detail="Vendor not found")

    db_vendor.vendor_name = vendor_name
    db_vendor.vendor_code = vendor_code
    db_vendor.vendor_type = vendor_type
    db_vendor.contact_person = contact_person
    db_vendor.mobile_no = mobile_no
    db_vendor.alternate_no = alternate_no
    db_vendor.email_id = email_id
    db_vendor.address = address
    db_vendor.city = city
    db_vendor.state = state
    db_vendor.pincode = pincode
    db_vendor.pan_number = pan_number
    db_vendor.gst_no = gst_no
    db_vendor.bank_name = bank_name
    db_vendor.account_number = account_number
    db_vendor.ifsc_code = ifsc_code
    db_vendor.account_type = account_type
    db_vendor.status = status
    db_vendor.remarks = remarks

    db.commit()
    db.refresh(db_vendor)
    return db_vendor
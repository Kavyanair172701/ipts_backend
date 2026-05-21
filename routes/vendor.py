from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db
from models import VendorMaster

router = APIRouter()


@router.post("/create")
def create_vendor(
    vendor_name: str,
    contact_person: str = None,
    mobile_no: str = None,
    email_id: str = None,
    gst_no: str = None,
    address: str = None,
    db: Session = Depends(get_db)
):

    vendor = VendorMaster(
        vendor_name=vendor_name,
        contact_person=contact_person,
        mobile_no=mobile_no,
        email_id=email_id,
        gst_no=gst_no,
        address=address
    )

    db.add(vendor)
    db.commit()
    db.refresh(vendor)

    return {
        "message": "Vendor Created Successfully",
        "vendor_id": vendor.vendor_id
    }


@router.get("/")
def get_vendors(db: Session = Depends(get_db)):

    vendors = db.query(VendorMaster).all()

    return vendors
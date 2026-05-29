

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db
from models import IonMaster
from schemas import IonCreate
from schemas import VendorCreate, VendorUpdate, VendorResponse

router = APIRouter()


@router.post("/create")
def create_ion(ion: IonCreate, db: Session = Depends(get_db)):

    new_ion = IonMaster(
        ion_no=ion.ion_no,
        ion_date=ion.ion_date,
        department=ion.department,
        work_name=ion.work_name,
        vendor_name=ion.vendor_name,
        po_no=ion.po_no,
        po_date=ion.po_date,
        total_amount=ion.total_amount,
        paid_amount=0,
        balance_amount=ion.total_amount,
        status="CREATED",
        status_colour="WHITE",
        remarks=ion.remarks
    )

    db.add(new_ion)
    db.commit()
    db.refresh(new_ion)

    return {
        "message": "ION Created Successfully",
        "ion_id": new_ion.ion_id
    }


@router.get("/")
def get_ions(db: Session = Depends(get_db)):

    ions = db.query(IonMaster).all()

    return ions
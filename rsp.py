from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from models import RSP

router = APIRouter(prefix="/rsp", tags=["RSP"])

@router.post("/create")
def create_rsp(
    title_type: str = "",
    company_name: str = "",
    rsp_date: str = "",
    vendor_name: str = "",
    cheque_name: str = "",
    project_name: str = "",
    work_name: str = "",
    invoice_type: str = "",
    invoice_no: str = "",
    invoice_date: str = "",
    amount_payable: float = 0,
    amount_words: str = "",
    db: Session = Depends(get_db)
):
    new_rsp = RSP(
        title_type=title_type,
        company_name=company_name,
        rsp_date=rsp_date,
        vendor_name=vendor_name,
        cheque_name=cheque_name,
        project_name=project_name,
        work_name=work_name,
        invoice_type=invoice_type,
        invoice_no=invoice_no,
        invoice_date=invoice_date,
        amount_payable=amount_payable,
        amount_words=amount_words
    )

    db.add(new_rsp)
    db.commit()
    db.refresh(new_rsp)

    return {"message": "RSP Saved Successfully", "data": new_rsp}


@router.get("/")
def get_all_rsp(db: Session = Depends(get_db)):
    return db.query(RSP).order_by(RSP.rsp_id.desc()).all()
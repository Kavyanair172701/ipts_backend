from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db
from models import PurchaseOrder

router = APIRouter(
    prefix="/purchase-order",
    tags=["Purchase Order"]
)


@router.post("/create")
def create_purchase_order(
    company_name: str = "",
    po_date: str = "",
    po_ref_no: str = "",
    vendor_name: str = "",
    vendor_address: str = "",
    gstin: str = "",
    kind_attention: str = "",
    proforma_invoice_no: str = "",
    project_name: str = "",
    duration_from: str = "",
    duration_to: str = "",
    amount: float = 0,
    gst_percent: float = 18,
    gst_amount: float = 0,
    grand_total: float = 0,
    amount_words: str = "",
    payment_terms: str = "",
    cheque_favour: str = "",
    db: Session = Depends(get_db)
):
    po = PurchaseOrder(
        company_name=company_name,
        po_date=po_date,
        po_ref_no=po_ref_no,
        vendor_name=vendor_name,
        vendor_address=vendor_address,
        gstin=gstin,
        kind_attention=kind_attention,
        proforma_invoice_no=proforma_invoice_no,
        project_name=project_name,
        duration_from=duration_from,
        duration_to=duration_to,
        amount=amount,
        gst_percent=gst_percent,
        gst_amount=gst_amount,
        grand_total=grand_total,
        amount_words=amount_words,
        payment_terms=payment_terms,
        cheque_favour=cheque_favour
    )

    db.add(po)
    db.commit()
    db.refresh(po)

    return {
        "message": "Purchase Order Saved Successfully",
        "data": po
    }


@router.get("/")
def get_purchase_orders(db: Session = Depends(get_db)):
    return db.query(PurchaseOrder).order_by(PurchaseOrder.po_id.desc()).all()


@router.get("/{po_id}")
def get_purchase_order(po_id: int, db: Session = Depends(get_db)):
    return db.query(PurchaseOrder).filter(
        PurchaseOrder.po_id == po_id
    ).first()


@router.delete("/{po_id}")
def delete_purchase_order(po_id: int, db: Session = Depends(get_db)):
    po = db.query(PurchaseOrder).filter(
        PurchaseOrder.po_id == po_id
    ).first()

    if po:
        db.delete(po)
        db.commit()

    return {"message": "Deleted Successfully"}
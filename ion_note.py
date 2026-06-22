from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models import IonNote

router = APIRouter(prefix="/ion-note", tags=["ION NOTE"])


@router.post("/create")
def create_ion_note(
    company_name: str = "",
    ion_date: str = "",
    ion_ref_no: str = "",
    subject: str = "",
    vendor_name: str = "",
    work_name: str = "",
    project_name: str = "",
    duration_from: str = "",
    duration_to: str = "",
    base_amount: float = 0,
    gst_percent: float = 18,
    gst_amount: float = 0,
    grand_total: float = 0,
    db: Session = Depends(get_db)
):
    new_ion = IonNote(
        company_name=company_name,
        ion_date=ion_date,
        ion_ref_no=ion_ref_no,
        subject=subject,
        vendor_name=vendor_name,
        work_name=work_name,
        project_name=project_name,
        duration_from=duration_from,
        duration_to=duration_to,
        base_amount=base_amount,
        gst_percent=gst_percent,
        gst_amount=gst_amount,
        grand_total=grand_total
    )

    db.add(new_ion)
    db.commit()
    db.refresh(new_ion)

    return {
        "message": "ION Note Saved Successfully",
        "data": new_ion
    }


@router.get("/")
def get_all_ion_notes(db: Session = Depends(get_db)):
    return (
        db.query(IonNote)
        .order_by(IonNote.ion_note_id.desc())
        .all()
    )


@router.get("/{ion_note_id}")
def get_ion_note(
    ion_note_id: int,
    db: Session = Depends(get_db)
):
    ion_note = (
        db.query(IonNote)
        .filter(IonNote.ion_note_id == ion_note_id)
        .first()
    )

    if not ion_note:
        raise HTTPException(
            status_code=404,
            detail="ION Note Not Found"
        )

    return ion_note


@router.delete("/{ion_note_id}")
def delete_ion_note(
    ion_note_id: int,
    db: Session = Depends(get_db)
):
    ion_note = (
        db.query(IonNote)
        .filter(IonNote.ion_note_id == ion_note_id)
        .first()
    )

    if not ion_note:
        raise HTTPException(
            status_code=404,
            detail="ION Note Not Found"
        )

    db.delete(ion_note)
    db.commit()

    return {
        "message": "ION Note Deleted Successfully"
    }
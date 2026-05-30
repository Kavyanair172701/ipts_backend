from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from models import RSP

router = APIRouter(prefix="/rsp", tags=["RSP"])

@router.post("/create")
def create_rsp(
    amount_payable: float = 0,
    amount_words: str = "",
    db: Session = Depends(get_db)
):
    new_rsp = RSP(
        amount_payable=amount_payable,
        amount_words=amount_words
    )

    db.add(new_rsp)
    db.commit()
    db.refresh(new_rsp)

    return {"message": "RSP Saved Successfully"}
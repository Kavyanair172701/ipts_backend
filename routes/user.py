from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import func

from passlib.context import CryptContext

from database import get_db
from models import UserMaster
from schemas import UserCreate, UserLogin

router = APIRouter()

pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)


def hash_password(password: str):
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str):
    return pwd_context.verify(
        plain_password,
        hashed_password
    )


@router.post("/create")
def create_user(
    user: UserCreate,
    db: Session = Depends(get_db)
):

    existing_user = db.query(UserMaster).filter(
        UserMaster.username == user.username
    ).first()

    if existing_user:
        raise HTTPException(
            status_code=400,
            detail="Username already exists"
        )

    new_user = UserMaster(
        username=user.username,
        password=hash_password(user.password),
        first_name=user.first_name,
        last_name=user.last_name,
        email=user.email,
        is_superuser=user.is_superuser,
        is_staff=user.is_staff,
        is_active=user.is_active
    )

    db.add(new_user)

    db.commit()

    db.refresh(new_user)

    return {
        "message": "User Created Successfully",
        "user_id": new_user.id,
        "username": new_user.username
    }


@router.post("/login")
def login_user(
    user: UserLogin,
    db: Session = Depends(get_db)
):

    db_user = db.query(UserMaster).filter(
        UserMaster.username == user.username
    ).first()

    if not db_user:
        raise HTTPException(
            status_code=401,
            detail="Invalid username or password"
        )

    if db_user.is_active != 1:
        raise HTTPException(
            status_code=403,
            detail="User inactive"
        )

    if not verify_password(
        user.password,
        db_user.password
    ):
        raise HTTPException(
            status_code=401,
            detail="Invalid username or password"
        )

    db_user.last_login = func.now()

    db.commit()

    return {
        "message": "Login Successful",
        "user_id": db_user.id,
        "username": db_user.username,
        "first_name": db_user.first_name,
        "email": db_user.email
    }


@router.get("/")
def get_users(
    db: Session = Depends(get_db)
):

    return db.query(UserMaster).all()
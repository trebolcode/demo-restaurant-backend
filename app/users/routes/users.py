from typing import Optional, List
from fastapi import APIRouter,status,Depends

# Database
from sqlalchemy.orm import Session
from config.database import get_db


# Schema
import app.users.schemas.users as schemas

# Model
import app.users.models.users as models

router = APIRouter(tags=["Users"])


@router.get(
    path="/users",
    status_code=status.HTTP_200_OK,
    response_model=List[schemas.Users],
)
def get_all_users(db: Session = Depends(get_db)):
    """
    Documentation:
    """
    users = db.query(models.Users).all()
    return users


@router.post(
    path="/users",
    status_code=status.HTTP_201_CREATED,
    response_model=schemas.Users,
)
def create_user(reservation:schemas.Users,db: Session = Depends(get_db),):
    """
    Documentation:
    """
    new_User = models.Users(**reservation.dict())
    db.add(new_User)
    db.commit()
    db.refresh(new_User)

    return new_User

from typing import Optional, List
from fastapi import APIRouter,status,Depends

# Database
from sqlalchemy.orm import Session
from config.database import get_db

# Schema
import app.reservations.schemas.reservations as schemas

# Model
import app.reservations.models.reservations as models

router = APIRouter(tags=["Reservations"])


@router.get(
    path="/reservations",
    status_code=status.HTTP_200_OK,
    response_model=List[schemas.BookTable],
)
def get_all_reservations(db: Session = Depends(get_db)):
    """
    Documentation:
    """
    reservations = db.query(models.Reservations).all()
    return reservations


@router.post(
    path="/reservations",
    status_code=status.HTTP_201_CREATED,
    response_model=schemas.BookTable,
)
def make_reservation(reservation:schemas.BookTableInput,db: Session = Depends(get_db),):
    """
    Documentation:
    """
    new_reservation = models.Reservations(**reservation.dict())
    db.add(new_reservation)
    db.commit()
    db.refresh(new_reservation)

    return new_reservation

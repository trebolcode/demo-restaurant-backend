from typing import Optional, List
from fastapi import APIRouter, status, Depends

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
    response_model=List[schemas.UsersOut],
)
def get_all_users(
        limit: int = 10,
        skip: int = 0,
        db: Session = Depends(get_db),
):
    """
    Documentation:
    Return all users.
    """
    users = db.query(models.Users).limit(limit).offset(skip).all()
    return users


@router.get(
    path="/users/{user_id}",
    status_code=status.HTTP_200_OK,
    response_model=schemas.UsersOut,
)
def get_an_user(user_id: int, db: Session = Depends(get_db)):
    """
    Documentation:
    Return only one user by ID.
    """
    user = db.query(models.Users).filter_by(id=user_id).first()
    return user


@router.post(
    path="/users",
    status_code=status.HTTP_201_CREATED,
    response_model=schemas.UsersOut,
)
def create_user(user: schemas.UsersIn, db: Session = Depends(get_db),):
    """
    Documentation:
    """
    new_User = models.Users(**user.dict())
    db.add(new_User)
    db.commit()
    db.refresh(new_User)

    return new_User

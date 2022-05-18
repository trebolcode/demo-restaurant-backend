from typing import Optional, List
from fastapi import APIRouter, Query, status, Depends, HTTPException

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
    summary="Get all users",
    response_description="You can get all users.",
)
def get_all_users(
        limit: int = 10,
        skip: int = Query(
            alias="skip", description="Initial value of the index", default=0),
        db: Session = Depends(get_db),
):
    """
    Return all users:

    Values:
    - **limit**: pending
    - **skip**: pending

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


@router.delete(
    path="/users/{user_id}",
    status_code=status.HTTP_200_OK,
    response_model={},
)
def delete_user(user_id: int, db: Session = Depends(get_db)):
    """
    Documentation:

    """

    user = db.query(models.Users).filter_by(id=user_id)

    data_user = user.first()

    if data_user == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'User {user_id} not exist.')

    user.delete(synchronize_session=False)
    db.commit()

    return {"msg": f'User {user_id} was deleted.'}

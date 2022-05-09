from typing import Optional, List
from fastapi import APIRouter, status, Depends

# Database
from sqlalchemy.orm import Session
from config.database import get_db

# Schema
import app.reviews.schemas.reviews as schemas

# Model
import app.reviews.models.reviews as models
import app.users.models.users as model_Users


router = APIRouter(tags=["Reviews"])


@router.get(
    path="/reviews",
    status_code=status.HTTP_200_OK,
    response_model=List[schemas.ReviewOut],
)
def get_all_reviews(db: Session = Depends(get_db)):
    """
    Documentation:
    """
    reviews = db.query(models.Reviews).all()
    return reviews


@router.get(
    path="/reviews/{id_review}",
    status_code=status.HTTP_200_OK,
    #response_model=schemas.ReviewOutUser,
)
def get_a_review(id_review:int,db: Session = Depends(get_db)):
    """
    Documentation:
    """
    #review = db.query(models.Reviews).filter(models.Reviews.id==id_review).first()

#    reviews = db.query(models.Reviews,model_Users.Users).join(models.Reviews,models.Reviews.id_user==model_Users.Users.id,isouter=True).all()
    reviews = db.query(
            models.Reviews.id,
            models.Reviews.title,
            models.Reviews.rating,
            models.Reviews.comments,
            models.Reviews.created_at,
            model_Users.Users.name,
            model_Users.Users.last_name,
        ).join(models.Reviews,models.Reviews.id_user==model_Users.Users.id,isouter=True).filter(models.Reviews.id==id_review).first()


    return reviews

@router.post(
    path="/reviews",
    status_code=status.HTTP_201_CREATED,
    response_model=schemas.ReviewOut,
)
def make_review(review: schemas.ReviewIn, db: Session = Depends(get_db),):
    """
    Documentation:
    """
    new_review = models.Reviews(**review.dict())
    db.add(new_review)
    db.commit()
    db.refresh(new_review)

    return new_review

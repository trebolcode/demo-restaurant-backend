from typing import Optional, List
from fastapi import APIRouter, status, Depends

# Database
from sqlalchemy.orm import Session
from config.database import get_db

# Schema
import app.reviews.schemas.reviews as schemas

# Model
import app.reviews.models.reviews as models

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

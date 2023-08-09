from fastapi import APIRouter, Depends, HTTPException, status, Response
from app.api.schemas.feed import Feed, FeedCreate
from app.api.models.feed import Feed as models_feed
from app.core.database import get_db
from sqlalchemy.orm import Session

router = APIRouter()


@router.get("/", response_model=list[Feed])
def get_feeds(db: Session = Depends(get_db)):
    """
    Retrieve all feeds from the feeds.
    """
    feeds = db.query(models_feed).all()
    return feeds


@router.get("/{feed_id}", response_model=Feed)
def get_feed(feed_id: int, db: Session = Depends(get_db)):
    """
    Retrieve a specific feed by its ID.
    """
    feed = db.query(models_feed).filter(models_feed.id == feed_id).first()
    if not feed:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"feed with id: {feed_id} does not exist")
    return feed


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=Feed)
def create_feed(feed: FeedCreate, db: Session = Depends(get_db)):
    """
    Create a new feed.
    """
    new_feed = models_feed(**feed.model_dump())
    db.add(new_feed)
    db.commit()
    db.refresh(new_feed)
    return new_feed


@router.put("/{feed_id}", response_model=Feed)
def update_feed(feed_id: int, feed: FeedCreate, db: Session = Depends(get_db)):
    """
    Update an existing feed.
    """
    db_feed = db.query(Feed).filter(models_feed.id == feed_id).first()
    if not db_feed:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"feed with id: {feed_id} does not exist")
    for key, value in feed.model_dump(exclude_unset=True).items():
        setattr(db_feed, key, value)
    db.commit()
    db.refresh(db_feed)
    return db_feed


@router.delete("/{feed_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_feed(feed_id: int, db: Session = Depends(get_db)):
    """
    Delete a feed by its ID.
    """
    db_feed = db.query(Feed).filter(models_feed.id == feed_id).first()
    if not db_feed:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"feed with id: {feed_id} does not exist")
    db.delete(db_feed)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)

from fastapi import APIRouter, Depends, HTTPException, status, Response
from sqlalchemy.orm import Session

from app.api.models.author import Author as ModelsAuthor
from app.api.schemas.author import Author, AuthorCreate
from app.core.database import get_db

router = APIRouter()


@router.get("/{author_id}", response_model=Author)
def get_author(author_id: int, db: Session = Depends(get_db)):
    """
    Retrieve a specific author by its ID.
    """
    author = db.query(ModelsAuthor).filter(ModelsAuthor.id == author_id).first()
    if not author:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"author with id: {author_id} does not exist")
    return author


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=Author)
def create_author(author: AuthorCreate, db: Session = Depends(get_db)):
    """
    Create a new author.
    """
    new_author = ModelsAuthor(**author.model_dump())
    db.add(new_author)
    db.commit()
    db.refresh(new_author)
    return new_author


@router.put("/{author_id}", response_model=Author)
def update_author(author_id: int, author: AuthorCreate, db: Session = Depends(get_db)):
    """
    Update an existing author.
    """
    db_author = db.query(ModelsAuthor).filter(ModelsAuthor.id == author_id).first()
    if not db_author:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"author with id: {author_id} does not exist")

    for key, value in author.model_dump(exclude_unset=True).items():
        setattr(db_author, key, value)
    db.commit()
    db.refresh(db_author)
    return db_author


@router.delete("/{author_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_author(author_id: int, db: Session = Depends(get_db)):
    """
    Delete a author by its ID.
    """
    db_author = db.query(ModelsAuthor).filter(ModelsAuthor.id == author_id).first()
    if not db_author:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"author with id: {author_id} does not exist")
    db.delete(db_author)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)

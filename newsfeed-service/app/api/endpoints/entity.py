from fastapi import APIRouter, Depends, HTTPException, status, Response
from sqlalchemy.orm import Session

from app.api.models.entity import Entity as ModelsEntity
from app.api.schemas.entity import Entity, EntityCreate
from app.core.database import get_db

router = APIRouter()


@router.get("/{entity_id}", response_model=Entity)
def get_entity(entity_id: int, db: Session = Depends(get_db)):
    """
    Retrieve a specific entity by its ID.
    """
    entity = db.query(ModelsEntity).filter(ModelsEntity.id == entity_id).first()
    if not entity:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"entity with id: {entity_id} does not exist")
    return entity


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=Entity)
def create_entity(entity: EntityCreate, db: Session = Depends(get_db)):
    """
    Create a new entity.
    """
    new_entity = ModelsEntity(**entity.model_dump())
    db.add(new_entity)
    db.commit()
    db.refresh(new_entity)
    return new_entity


@router.put("/{entity_id}", response_model=Entity)
def update_entity(entity_id: int, entity: EntityCreate, db: Session = Depends(get_db)):
    """
    Update an existing entity.
    """
    db_entity = db.query(ModelsEntity).filter(ModelsEntity.id == entity_id).first()
    print(db_entity)
    if not db_entity:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"entity with id: {entity_id} does not exist")

    for key, value in entity.model_dump(exclude_unset=True).items():
        setattr(db_entity, key, value)
    db.commit()
    db.refresh(db_entity)
    return db_entity


@router.delete("/{entity_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_entity(entity_id: int, db: Session = Depends(get_db)):
    """
    Delete a entity by its ID.
    """
    db_entity = db.query(ModelsEntity).filter(ModelsEntity.id == entity_id).first()
    if not db_entity:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"entity with id: {entity_id} does not exist")
    db.delete(db_entity)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)

from sqlalchemy.orm import Session
from app import models,schemas


def create_task(db:Session,task:schemas.TaskCreate):
    db_task = models.Task(**task.dict())
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

def get_tasks(db:Session):
    return db.query(models.Task).all()

def update_task(db:Session,task_id:int,updates:schemas.TaskUpdate):
    db_task = db.query(models.Task).filter(models.Task.id == task_id).first()
    if not db_task:
        return None
    for key,value in updates.dict(exclude_unset=True).items():
        setattr(db_task,key,value)
    db.commit()
    db.refresh(db_task)
    return db_task 

def delete_task(db:Session,task_id:int):
    db_task = db.query(models.Task).filter(models.Task.id == task_id).first()
    if db_task:
        db.delete(db_task)
        db.commit()
    return db_task   

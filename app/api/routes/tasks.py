from fastapi import APIRouter,Depends,HTTPException
from sqlalchemy.orm import Session
from app.db.session import SessionLocal
from app import schemas,services

router = APIRouter(prefix="/tasks",tags=["Tasks"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/",response_model=schemas.TaskRead)
def create_task(task:schemas.TaskCreate,db:Session = Depends(get_db)):
    return services.task_service.create_task(db,task)

@router.get("/",response_model=list[schemas.TaskRead])
def get_tasks(db:Session = Depends(get_db)):
    return services.task_service.get_tasks(db)

@router.put("/{task_id}",response_model=schemas.TaskRead)
def update_task(task_id:int,updates:schemas.TaskUpdate,db:Session=Depends(get_db)):
    task = services.update_task(db,task_id,updates)
    if not task:
        raise HTTPException(status_code=404,detail="Task not found")
    return task

@router.delete("/{task_id}")
def delete_user(task_id:int,db:Session=Depends(get_db)):
    task = services.delete_task(db,task_id)
    if not task:
        raise HTTPException(status_code=404,detail="Task not found")
    return {"message":"Task deleted successfully"}

from fastapi import APIRouter,Depends
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

@router.post("/",response_model=schemas.Task)
def create_task(task:schemas.TaskCreate,db:Session = Depends(get_db)):
    return services.task_service.create_task(db,task)

@router.get("/",response_model=list[schemas.Task])
def get_tasks(db:Session = Depends(get_db)):
    return services.task_service.get_tasks(db)
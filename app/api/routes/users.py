from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from app.db.session import SessionLocal
from app import schemas,services

router = APIRouter(prefix="/users",tags=["Users"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/",response_model=schemas.User)
def create_user(user:schemas.UserCreate,db: Session = Depends(get_db)):
    return services.user_service.create_user(db,user)

@router.get("/",response_model=list[schemas.User])
def get_users(db:Session = Depends(get_db)):
    return services.user_service.get_users(db)
    
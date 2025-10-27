from fastapi import APIRouter,Depends,HTTPException
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

@router.post("/",response_model=schemas.UserRead)
def create_user(user:schemas.UserCreate,db: Session = Depends(get_db)):
    return services.user_service.create_user(db,user)

@router.get("/",response_model=list[schemas.UserRead])
def get_users(db:Session = Depends(get_db)):
    return services.user_service.get_users(db)

@router.put("/{user_id}",response_model=schemas.UserRead)
def update_user(user_id:int,updates:schemas.UserCreate,db:Session = Depends(get_db)):
    user = services.update_user(db,user_id,updates)
    if not user:
        raise HTTPException(status_code=404,detail="User not found")
    return user

@router.delete("/{user_id}")
def delete(user_id:int, db:Session=Depends(get_db)):
    user = services.delete_user(db,user_id)
    if not user:
        raise HTTPException(status_code=404,detail="User not found")
    return {"message": "User deleted successfully"}

    
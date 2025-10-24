from pydantic import BaseModel

class TaskBase(BaseModel):
    title: str
    description: str | None = None
    user_id: int

class TaskCreate(TaskBase):
    user_id: int  # Required for creation

class Task(TaskBase):
    id: int

    class Config:
        from_attributes = True
        
from pydantic import BaseModel

class TaskBase(BaseModel):
    title: str
    description: str | None = None


class TaskCreate(TaskBase):
    user_id: int

class TaskUpdate(BaseModel):
    title: str | None = None
    description: str | None = None
    completed: bool | None = None


class TaskRead(TaskBase):
    id: int
    completed: bool | None = False
    user_id: int | None = None  

    class Config:
        from_attributes = True
        
from fastapi import FastAPI
from app.api.routes import users,tasks
from app.db import base, session

app = FastAPI(title="Simple CRUD API")

base.Base.metadata.create_all(bind=session.engine)

app.include_router(users.router)
app.include_router(tasks.router)

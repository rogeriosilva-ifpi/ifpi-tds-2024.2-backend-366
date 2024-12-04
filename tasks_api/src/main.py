from fastapi import FastAPI
from .tasks_controller import router as task_router
from .users_controller import router as user_router
from .database import init_db


app = FastAPI()

app.include_router(router=task_router)
app.include_router(router=user_router)

init_db()


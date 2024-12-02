from fastapi import FastAPI
from .tasks_controller import router
from .database import init_db


app = FastAPI()

app.include_router(router=router)

init_db()


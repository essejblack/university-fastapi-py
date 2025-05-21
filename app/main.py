from fastapi import FastAPI
from app.routes import student
import alembic

app = FastAPI(title="University")
app.include_router(student.router)

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/status")
async def read_status():
    return {"status_code": 200,"message": "OK"}

from fastapi import FastAPI
from app.routes import employee_routes
from app.db.db import init_indexes, init_schema

app = FastAPI(title="Employee Assessment API")

@app.on_event("startup")
async def startup_event():
    await init_indexes()
    await init_schema()

app.include_router(employee_routes.router)

@app.get("/")
async def root():
    return {"message": "FastAPI MongoDB Assessment Running"}

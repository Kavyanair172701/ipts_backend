from fastapi import FastAPI

from database import engine, Base
import models

from routes.ion import router as ion_router
from routes.vendor import router as vendor_router

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(ion_router, prefix="/ions", tags=["IONS"])

app.include_router(vendor_router, prefix="/vendors", tags=["VENDORS"])


@app.get("/")
def home():
    return {"message": "IPTS Backend Running Successfully"}
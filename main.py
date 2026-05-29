from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from database import engine, Base
import models

from routes.ion import router as ion_router
from routes.vendor import router as vendor_router
from routes.user import router as user_router

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="IPTS Backend",
    description="IPTS Backend API",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(ion_router, prefix="/ions", tags=["IONS"])
app.include_router(vendor_router, prefix="/vendors", tags=["VENDORS"])
app.include_router(user_router, prefix="/users", tags=["USERS"])


@app.get("/")
def home():
    return {
        "message": "IPTS Backend Running Successfully",
        "available_routes": [
            "/ions",
            "/vendors",
            "/users",
            "/users/create",
            "/users/login",
            "/docs"
        ]
    }


@app.get("/health")
def health_check():
    return {
        "status": "OK",
        "message": "Backend is running"
    }
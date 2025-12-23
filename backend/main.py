from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.config.settings import settings
from backend.api import (
    classes,
    member,
    user,
    room,
    department,
    auth,
)

app = FastAPI(
    title="Project HIM API",
    description="Church Management System API",
    version="1.0.0"
)

# CORS Configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include all routers
app.include_router(auth.router)
app.include_router(user.router)
app.include_router(member.router)
app.include_router(classes.router)
app.include_router(room.router)
app.include_router(department.router)

@app.get("/")
async def root():
    """Health check endpoint"""
    return {"message": "Project HIM API is running", "version": "1.0.0"}


@app.get("/health")
async def health_check():
    """Health check for monitoring"""
    return {"status": "healthy"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "app.main:app",
        host="0.0.0.0",
        port=8000,
        reload=True
    )
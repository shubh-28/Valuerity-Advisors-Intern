from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import router

app = FastAPI()

# Allow communication with the frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://76ac-2405-201-6007-9123-686a-daec-1aa4-824c.ngrok-free.app"],  # Update with the frontend URL in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routes
app.include_router(router)

@app.get("/")
def root():
    return {"message": "FastAPI backend is running!"}



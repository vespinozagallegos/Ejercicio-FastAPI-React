from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Permitir que React (por ejemplo en http://localhost:3000) pueda acceder al backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # En producción deberías poner solo tu dominio
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/greeting")
def get_greeting():
    return {"message": "Hola desde FastAPI"}

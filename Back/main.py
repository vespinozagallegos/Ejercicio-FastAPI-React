from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel  # Para definir el modelo de datos

app = FastAPI()

# Permitir que React (por ejemplo en http://localhost:3000) pueda acceder al backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # En producción debería poner solo el dominio
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/greeting")
def get_greeting():
    return {"message": "Hola desde FastAPI"}

# Definimos un modelo para los datos que esperamos recibir
class FormData(BaseModel):
    name: str
    email: str

# Endpoint POST que recibe un formulario
@app.post("/api/form")
def receive_form(data: FormData):
    # Por ahora solo devolvemos los datos recibidos
    return {"received_data": data}

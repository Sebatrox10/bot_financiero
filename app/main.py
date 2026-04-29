from fastapi import FastAPI
from pydantic import BaseModel
from core_crypto import obtener_precios_core
from satellite_stocks import obtener_precios_energia
from analista_nlp import analizar_sentimiento_mercado

app = FastAPI(title="API Financiera - Estrategia Cuantitativa")

# Modelo de datos para cuando le enviemos noticias
class PeticionNoticias(BaseModel):
    noticias: str

@app.get("/")
def estado_servidor():
    return {"status": "ok", "mensaje": "Analista Financiero activo y monitoreando el mercado."}

@app.get("/precios-cripto")
def endpoint_cripto():
    """Devuelve los precios en tiempo real de los activos Core y Satélite crypto"""
    return obtener_precios_core()

@app.get("/precios-acciones")
def endpoint_acciones():
    """Devuelve los precios del sector energético"""
    return obtener_precios_energia()

@app.post("/analizar-mercado")
def endpoint_nlp(peticion: PeticionNoticias):
    """Evalúa noticias y devuelve un veredicto táctico"""
    veredicto = analizar_sentimiento_mercado(peticion.noticias)
    return {"sentimiento_tactico": veredicto}
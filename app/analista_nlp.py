import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel('gemini-2.5-flash')

def analizar_sentimiento_mercado(noticias: str):
    prompt_cuantitativo = f"""
    Eres un analista financiero cuantitativo experto en estrategias Core-Satellite. 
    Analiza el siguiente resumen de noticias y eventos macroeconómicos.
    
    1. Determina el sentimiento general del mercado a corto plazo (ALCISTA, BAJISTA o NEUTRAL).
    2. Da una recomendación táctica de máximo 3 líneas considerando un portafolio expuesto a Cripto y Sector Energético.
    
    NOTICIAS DEL DÍA:
    {noticias}
    """
    
    try:
        respuesta = model.generate_content(prompt_cuantitativo).text.strip()
        return respuesta
    except Exception as e:
        return f"⚠️ Error en el procesamiento NLP: {str(e)}"
import psycopg2
import json
import os
from dotenv import load_dotenv

# Cargamos las variables del archivo .env
load_dotenv()

def obtener_portafolio_dinamico():
    try:
        # Usamos os.getenv() para leer las credenciales seguras
        conexion = psycopg2.connect(
            host=os.getenv("DB_HOST", "postgres-vector"),
            database=os.getenv("DB_NAME", "agente_db"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            port=os.getenv("DB_PORT", "5432")
        )
        cursor = conexion.cursor()
        
        cursor.execute("SELECT json_activos FROM portafolio_estrategia WHERE id = 1;")
        resultado = cursor.fetchone()
        
        cursor.close()
        conexion.close()

        if resultado and resultado[0]:
            return json.loads(resultado[0])
        else:
            return {"core": [], "satelite": []}

    except Exception as e:
        print(f"Error leyendo portafolio de DB: {e}")
        return {"core": ["BTC", "ETH"], "satelite": []}
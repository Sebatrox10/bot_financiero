import yfinance as yf
from db_portafolio import obtener_portafolio_dinamico

def obtener_precios_energia():
    try:
        portafolio = obtener_portafolio_dinamico()
        tickers_satelite = portafolio.get("satelite", [])
        
        if not tickers_satelite:
            return {"mensaje_telegram": "⚠️ No hay activos tácticos en el portafolio Satélite."}

        datos_acciones = {}
        texto_telegram = "🎯 **Reporte Táctico (Satélite)**\n\n"
        
        for t in tickers_satelite:
            try:
                # Añadimos un intento de conexión rápida
                stock = yf.Ticker(f"{t}-USD")
                hist = stock.history(period="5d", timeout=5) # Timeout de 5 segundos
                
                if not hist.empty:
                    precio_actual = round(hist['Close'].iloc[-1], 2)
                    datos_acciones[t] = {"precio_usd": precio_actual}
                    texto_telegram += f"🔹 **{t}**: ${precio_actual}\n"
            except Exception:
                texto_telegram += f"🔹 **{t}**: ⏳ (Servidor de datos temporalmente no disponible)\n"
                
        return {
            "data": datos_acciones, 
            "mensaje_telegram": texto_telegram
        }
    except Exception as e:
        return {"mensaje_telegram": f"❌ Error: {str(e)}"}
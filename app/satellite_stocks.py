import yfinance as yf
from db_portafolio import obtener_portafolio_dinamico

def obtener_precios_energia():
    try:
        portafolio = obtener_portafolio_dinamico()
        tickers_satelite = portafolio.get("satelite", [])
        
        if not tickers_satelite:
            return {"mensaje": "No hay activos tácticos en el portafolio Satélite."}

        datos_acciones = {}
        
        for t in tickers_satelite:
            # Si Gemini detecta una cripto en satélite, le añadimos "-USD" para Yahoo Finance
            ticker_yf = f"{t}-USD" if t in ["BTC", "ETH", "SOL", "LINK", "ICP", "FIL"] else t
            
            stock = yf.Ticker(ticker_yf)
            hist = stock.history(period="5d")
            
            if not hist.empty:
                precio_actual = hist['Close'].iloc[-1]
                datos_acciones[t] = {
                    "precio_usd": round(precio_actual, 2)
                }
                
        return datos_acciones
    except Exception as e:
        return {"error": str(e)}
import yfinance as yf

def obtener_precios_energia():
    try:
        # Tickers tácticos del sector energético (Ejemplo: ExxonMobil, Chevron, NextEra Energy)
        tickers = ['XOM', 'CVX', 'NEE']
        datos_acciones = {}
        
        for t in tickers:
            stock = yf.Ticker(t)
            # Extraemos el historial de 1 día para sacar el precio de cierre más reciente
            hist = stock.history(period="5d")
            if not hist.empty:
                precio_actual = hist['Close'].iloc[-1]
                datos_acciones[t] = {
                    "precio_usd": round(precio_actual, 2)
                }
        return datos_acciones
    except Exception as e:
        return {"error": str(e)}
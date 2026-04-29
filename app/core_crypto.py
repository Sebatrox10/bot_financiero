from pycoingecko import CoinGeckoAPI
from db_portafolio import obtener_portafolio_dinamico

cg = CoinGeckoAPI()

# Traductor de Tickers a IDs de CoinGecko
MAPEO_CG = {
    "BTC": "bitcoin", "ETH": "ethereum", "SOL": "solana", 
    "ICP": "internet-computer", "LINK": "chainlink", "FIL": "filecoin"
}

def obtener_precios_core():
    try:
        portafolio = obtener_portafolio_dinamico()
        tickers_core = portafolio.get("core", [])
        
        if not tickers_core:
            return {"mensaje": "No hay activos en el portafolio Core."}

        # Traducimos los tickers (ej. ["BTC", "ETH"] -> "bitcoin,ethereum")
        ids_coingecko = [MAPEO_CG.get(t) for t in tickers_core if MAPEO_CG.get(t)]
        string_ids = ",".join(ids_coingecko)
        
        datos = cg.get_price(ids=string_ids, vs_currencies='usd', include_24hr_change=True)
        
        # Formateamos la respuesta de vuelta con el Ticker original
        precios_actualizados = {}
        for ticker in tickers_core:
            id_cg = MAPEO_CG.get(ticker)
            if id_cg and id_cg in datos:
                precios_actualizados[ticker] = {
                    "precio_usd": datos[id_cg]['usd'],
                    "variacion_24h": round(datos[id_cg]['usd_24h_change'], 2)
                }
                
        return precios_actualizados
    except Exception as e:
        return {"error": str(e)}
from pycoingecko import CoinGeckoAPI
from db_portafolio import obtener_portafolio_dinamico

cg = CoinGeckoAPI()

MAPEO_CG = {
    "BTC": "bitcoin", "ETH": "ethereum", "SOL": "solana", 
    "ICP": "internet-computer", "LINK": "chainlink", "FIL": "filecoin"
}

def obtener_precios_core():
    try:
        portafolio = obtener_portafolio_dinamico()
        tickers_core = portafolio.get("core", [])
        
        if not tickers_core:
            return {"mensaje_telegram": "⚠️ No hay activos en el portafolio Core."}

        ids_coingecko = [MAPEO_CG.get(t) for t in tickers_core if MAPEO_CG.get(t)]
        string_ids = ",".join(ids_coingecko)
        
        datos = cg.get_price(ids=string_ids, vs_currencies='usd', include_24hr_change=True)

        # Traducimos los tickers filtrando los que no existen en nuestro mapeo
        ids_coingecko = [MAPEO_CG.get(t) for t in tickers_core if t in MAPEO_CG]
        
        if not ids_coingecko:
            return {"mensaje_telegram": "⚠️ Los activos detectados no están soportados para rastreo en tiempo real."}
        
        precios_actualizados = {}
        texto_telegram = "📊 **Reporte Cripto (Core)**\n\n"
        
        for ticker in tickers_core:
            id_cg = MAPEO_CG.get(ticker)
            if id_cg and id_cg in datos:
                precio = datos[id_cg]['usd']
                var = round(datos[id_cg]['usd_24h_change'], 2)
                precios_actualizados[ticker] = {
                    "precio_usd": precio,
                    "variacion_24h": var
                }
                # Añade un icono visual según el rendimiento
                icono = "🟢" if var > 0 else "🔴"
                texto_telegram += f"{icono} **{ticker}**: ${precio} ({var}%)\n"
                
        return {
            "data": precios_actualizados, 
            "mensaje_telegram": texto_telegram
        }
    except Exception as e:
        return {"mensaje_telegram": f"❌ Error: {str(e)}"}
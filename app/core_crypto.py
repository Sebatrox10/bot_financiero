from pycoingecko import CoinGeckoAPI

cg = CoinGeckoAPI()

def obtener_precios_core():
    try:
        # Preconfigurado con tu portafolio: Bitcoin y Ethereum (Core) + Solana (Satélite/Táctico)
        ids = 'bitcoin,ethereum,solana'
        datos = cg.get_price(ids=ids, vs_currencies='usd', include_24hr_change=True)
        
        # Formateamos la respuesta para que sea fácil de leer en React o Telegram
        portafolio = {}
        for moneda, info in datos.items():
            portafolio[moneda] = {
                "precio_usd": info['usd'],
                "variacion_24h": round(info['usd_24h_change'], 2)
            }
        return portafolio
    except Exception as e:
        return {"error": str(e)}
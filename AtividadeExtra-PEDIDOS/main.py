from fastapi import FastAPI,HTTPException
import pandas as pd
app = FastAPI()

df = pd.read_csv('20250702_Pedidos_csv_2025.csv', encoding='utf-16', sep=';')
print(df.columns.tolist())  

@app.get("/pedidos/{IdPedido}")
def listar_pedidos(IdPedido:int):
    pedido = df[df['IdPedido'] == IdPedido]
    
    if pedido.empty:
        raise HTTPException(status_code=404, detail="Pedido não encontrado")
    
    return pedido.to_dict(orient='records')[0]
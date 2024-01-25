from fastapi import FastAPI # importar a classe da fastapi 

#app é o codigo que iniciamos no temrinal uvicorn main:app --reload 
app = FastAPI() #depois instanciar o app do import e ativar api

#criar as routes
@app.get("/")
def home():
    return "FAST API: ONLINE"

vendas = {
    1: {"item": "caixa de biscoitos", "preco_unitario": 3.5, "quantidade": 7},
    2: {"item": "detergente líquido", "preco_unitario": 2.2, "quantidade": 4},
    3: {"item": "sabão em pó", "preco_unitario": 5, "quantidade": 6},
    4: {"item": "pão de forma", "preco_unitario": 2, "quantidade": 3},
    5: {"item": "macarrão instantâneo", "preco_unitario": 1.8, "quantidade": 5},
    6: {"item": "sucos naturais", "preco_unitario": 4.5, "quantidade": 8},
    7: {"item": "lata de atum", "preco_unitario": 3, "quantidade": 2},
    8: {"item": "papel toalha", "preco_unitario": 4, "quantidade": 10},
    9: {"item": "molho barbecue", "preco_unitario": 6.5, "quantidade": 1},
    10: {"item": "shampoo anti-caspa", "preco_unitario": 7, "quantidade": 3},
    11: {"item": "caixa de cereais", "preco_unitario": 4, "quantidade": 5},
    12: {"item": "leite 1L", "preco_unitario": 3.2, "quantidade": 6},
    13: {"item": "sabonete", "preco_unitario": 1.5, "quantidade": 8},
    14: {"item": "queijo fatiado", "preco_unitario": 5, "quantidade": 4},
    15: {"item": "iogurte natural", "preco_unitario": 2.8, "quantidade": 7},
    16: {"item": "saco de batatas", "preco_unitario": 4, "quantidade": 5},
    17: {"item": "barras de chocolate", "preco_unitario": 2.5, "quantidade": 9},
    18: {"item": "arroz 5kg", "preco_unitario": 8, "quantidade": 3},
    19: {"item": "macarrão", "preco_unitario": 1.2, "quantidade": 6},
    20: {"item": "vinho tinto", "preco_unitario": 12, "quantidade": 2},
    21: {"item": "frango congelado", "preco_unitario": 7, "quantidade": 4},
    22: {"item": "azeitonas", "preco_unitario": 3, "quantidade": 3},
    23: {"item": "detergente", "preco_unitario": 1.8, "quantidade": 10},
    24: {"item": "pão integral", "preco_unitario": 2.5, "quantidade": 5},
    25: {"item": "limões", "preco_unitario": 1.5, "quantidade": 8},
    26: {"item": "sopa enlatada", "preco_unitario": 2.7, "quantidade": 7},
    27: {"item": "bife de carne bovina", "preco_unitario": 9.5, "quantidade": 2},
    28: {"item": "mel", "preco_unitario": 6, "quantidade": 1},
    29: {"item": "salmão fresco", "preco_unitario": 15, "quantidade": 2},
    30: {"item": "abacate", "preco_unitario": 4.5,}
}

@app.get("/vendas") #definir um path opertador .GET pega a path que seria a BARRA /
def root(): #definir o local
    return {"vendas": len(vendas)} #dicionario

@app.get("/vendas/{id_venda}") #definir um path opertador .GET pega a path que seria a BARRA /
def pegar_id(id_venda: int): #definir o local
    return vendas[id_venda] #dicionario

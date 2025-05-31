from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import httpx
# uvicorn main:app --reload

app = FastAPI()

class Endereco(BaseModel):
    cep: str
    logradouro: str
    bairro: str
    localidade: str
    uf: str
 
def buscar_cep(cep: str):
    url = f"https://viacep.com.br/ws/{cep}/json/"
    response = httpx.get(url)
    if response.status_code != 200:
        raise HTTPException(status_code=404, detail="CEP não encontrado")
    return response.json() 
 
    
@app.get("/cep/{cep}", response_model=Endereco)
async def consultar_cep(cep: str):
    url = f"https://viacep.com.br/ws/{cep}/json/"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        if response.status_code != 200:
            raise HTTPException(status_code=404, detail="CEP não encontrado")
        return response.json()
    
def main():
    cep = input('Digite o Cep: ')
    endereco = buscar_cep(cep)
    if not endereco:
        print("CEP não encontrado.")
    else:
        print(f"CEP: {endereco['cep']}")
        print(f"Logradouro: {endereco['logradouro']}")
        print(f"Bairro: {endereco['bairro']}")
        print(f"Localidade: {endereco['localidade']}")
        print(f"UF: {endereco['uf']}")
    
    
if __name__ == "__main__":
    main()

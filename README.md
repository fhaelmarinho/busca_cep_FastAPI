# Busca CEP

## Objetivo

Este projeto tem como objetivo fornecer uma ferramenta simples para consulta de endereços a partir do CEP, utilizando a API pública ViaCEP. Ele pode ser utilizado tanto via linha de comando (terminal) quanto como uma API REST utilizando FastAPI.

## Funcionalidades

- Consultar informações de endereço a partir de um CEP informado.
- Utilizar via terminal (modo interativo).
- Utilizar via API REST (FastAPI).
- Salvar consultas realizadas em um arquivo JSON (opcional, veja instruções).

## Tecnologias Utilizadas

- [Python 3.8+](https://www.python.org/)
- [FastAPI](https://fastapi.tiangolo.com/)
- [httpx](https://www.python-httpx.org/)
- [Pydantic](https://pydantic-docs.helpmanual.io/)
- [Uvicorn](https://www.uvicorn.org/) (para rodar a API)

## Como utilizar

### 1. Instale as dependências

Recomenda-se o uso de um ambiente virtual:

```bash
python3 -m venv venv
source venv/bin/activate
pip install fastapi httpx uvicorn pydantic
```

### 2. Rodar no terminal (modo interativo)

Execute o script diretamente:

```bash
python main.py
```

Você será solicitado a digitar um CEP. O endereço correspondente será exibido no terminal.

### 3. Rodar como API REST

Inicie o servidor FastAPI com Uvicorn:

```bash
uvicorn main:app --reload
```

Acesse a documentação interativa em:  
[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

Exemplo de requisição:
```
GET http://127.0.0.1:8000/cep/01001000
```

### 4. (Opcional) Salvar consultas em um arquivo JSON

Para salvar cada consulta realizada no terminal em um arquivo `consultas.json`, adicione a função de salvamento conforme sugerido nas respostas anteriores.

---

## Observações

- O projeto utiliza a API pública do ViaCEP, que pode ter limitações de uso.
- Certifique-se de estar conectado à internet para realizar as consultas.
- O código pode ser facilmente adaptado para outras formas de entrada ou integração.

---

## Licença

Este projeto é livre para uso educacional e pessoal.
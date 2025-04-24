# QuantumLine - Arena QuIIN 2025

Este projeto foi desenvolvido como parte do desafio do Arena QuIIN 2025: **Geradores Quânticos de Números Aleatórios para Instituições Financeiras**.

## Descrição

A aplicação valida saques bancários utilizando números verdadeiramente aleatórios gerados pela ANU (Australian National University), aplicando uma lógica simples:  
- Números pares: saque aprovado automaticamente  
- Números ímpares: saque enviado para análise manual

## Equipe 13

- Shirley Maria  
- Rafael Bittencourt  
- Cristian Griebler

## Como executar

1. Instale as dependências:
```
pip install -r requirements.txt
```

2. Execute o app:
```
streamlit run app.py
```

## Link da API

Os números são obtidos da API oficial da ANU:  
https://qrng.anu.edu.au/API/


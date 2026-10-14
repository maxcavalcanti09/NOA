# SauceDemo Ofertas (Selenium)

Robô que faz login em https://www.saucedemo.com/ (standard_user / secret_sauce),
mapeia todos os produtos da vitrine, extrai nome e preço e exibe no console e
salva em `ofertas.csv` apenas os produtos que custam menos de $20.00.

## Como executar

```bash
pip install -r requirements.txt
python saucedemo_ofertas.py
```

Requer Google Chrome instalado (o Selenium 4.6+ baixa o driver automaticamente).

## Saída esperada

4 ofertas de 6 produtos: Sauce Labs Bike Light, Sauce Labs Bolt T-Shirt,
Sauce Labs Onesie e Test.allTheThings() T-Shirt (Red).

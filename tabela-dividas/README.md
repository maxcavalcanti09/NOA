# Tabela de Dívidas (Selenium)

Script que acessa https://the-internet.herokuapp.com/tables, percorre as linhas
da "Table 1" e imprime Primeiro Nome, Último Nome e Web Site dos clientes com
"Due" superior a $50.00.

## Como executar

```bash
pip install -r requirements.txt
python tabela_dividas.py
```

Requer Google Chrome instalado (o Selenium 4.6+ baixa o driver automaticamente).

## Saída esperada

```
Clientes com dívida superior a $50.00:

Nome: Frank | Sobrenome: Bach | Site: http://www.frank.com
Nome: Jason | Sobrenome: Doe | Site: http://www.jdoe.com
```

# Livraria Scraper (Selenium)

Robô que acessa http://books.toscrape.com/, extrai Título e Preço dos livros da
página 1, clica em "Next", extrai os da página 2 e imprime o total (esperado: 40).

## Como executar

```bash
pip install -r requirements.txt
python livraria_scraper.py
```

Requer Google Chrome instalado (o Selenium 4.6+ baixa o driver automaticamente).

Para raspar mais páginas, altere `TOTAL_PAGINAS` no script.

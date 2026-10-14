# NOA
from decimal import Decimal
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

URL = "https://the-internet.herokuapp.com/tables"
LIMITE = Decimal("50.00")

# Ordem das colunas na Table 1:
# 0: Last Name | 1: First Name | 2: Email | 3: Due | 4: Web Site | 5: Action
COL_ULTIMO_NOME, COL_PRIMEIRO_NOME, COL_DUE, COL_SITE = 0, 1, 3, 4


def parse_valor(texto: str) -> Decimal:
    """Converte '$1,250.50' em Decimal('1250.50')."""
    return Decimal(texto.replace("$", "").replace(",", "").strip())


def main():
    driver = webdriver.Chrome()
    try:
        driver.get(URL)

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "table1"))
        )

        linhas = driver.find_elements(By.CSS_SELECTOR, "#table1 tbody tr")

        print("Clientes com dívida superior a $50.00:\n")
        for linha in linhas:
            celulas = linha.find_elements(By.TAG_NAME, "td")

            due = parse_valor(celulas[COL_DUE].text)
            if due > LIMITE:
                primeiro_nome = celulas[COL_PRIMEIRO_NOME].text
                ultimo_nome = celulas[COL_ULTIMO_NOME].text
                site = celulas[COL_SITE].text
                print(f"Nome: {primeiro_nome} | Sobrenome: {ultimo_nome} | Site: {site}")
    finally:
        driver.quit()


if __name__ == "__main__":
    main()
import csv
from decimal import Decimal

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

URL = "https://www.saucedemo.com/"
USUARIO = "standard_user"
SENHA = "secret_sauce"
LIMITE = Decimal("20.00")
ARQUIVO_SAIDA = "ofertas.csv"


def parse_preco(texto: str) -> Decimal:
    """Converte '$29.99' em Decimal('29.99')."""
    return Decimal(texto.replace("$", "").replace(",", "").strip())


def fazer_login(driver, wait):
    driver.get(URL)
    wait.until(EC.visibility_of_element_located((By.ID, "user-name"))).send_keys(USUARIO)
    driver.find_element(By.ID, "password").send_keys(SENHA)
    driver.find_element(By.ID, "login-button").click()
    wait.until(EC.presence_of_element_located((By.ID, "inventory_container")))


def mapear_produtos(driver):
    """Retorna lista de (nome, preco) de todos os itens da vitrine."""
    produtos = []
    for item in driver.find_elements(By.CSS_SELECTOR, ".inventory_item"):
        nome = item.find_element(By.CSS_SELECTOR, ".inventory_item_name").text
        preco = parse_preco(item.find_element(By.CSS_SELECTOR, ".inventory_item_price").text)
        produtos.append((nome, preco))
    return produtos


def main():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)

    try:
        fazer_login(driver, wait)
        produtos = mapear_produtos(driver)
    finally:
        driver.quit()

    ofertas = [(nome, preco) for nome, preco in produtos if preco < LIMITE]

    print(f"Produtos mapeados: {len(produtos)}")
    print(f"Ofertas abaixo de ${LIMITE}: {len(ofertas)}\n")
    for nome, preco in ofertas:
        print(f"{nome} | ${preco}")

    with open(ARQUIVO_SAIDA, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Nome", "Preco"])
        writer.writerows(ofertas)
    print(f"\nOfertas salvas em {ARQUIVO_SAIDA}")


if __name__ == "__main__":
    main()

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

URL = "http://books.toscrape.com/"
TOTAL_PAGINAS = 2


def extrair_livros_da_pagina(driver):
    """Retorna uma lista de (titulo, preco) dos livros da página atual."""
    livros = []
    for item in driver.find_elements(By.CSS_SELECTOR, "article.product_pod"):
        # O texto do link é truncado em títulos longos; o atributo 'title' é completo.
        titulo = item.find_element(By.CSS_SELECTOR, "h3 a").get_attribute("title")
        preco = item.find_element(By.CSS_SELECTOR, "p.price_color").text
        livros.append((titulo, preco))
    return livros


def main():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)
    todos_os_livros = []

    try:
        driver.get(URL)

        for pagina in range(1, TOTAL_PAGINAS + 1):
            wait.until(
                EC.presence_of_all_elements_located(
                    (By.CSS_SELECTOR, "article.product_pod")
                )
            )

            livros = extrair_livros_da_pagina(driver)
            print(f"--- Página {pagina}: {len(livros)} livros ---")
            for titulo, preco in livros:
                print(f"{titulo} | {preco}")
            todos_os_livros.extend(livros)

            if pagina < TOTAL_PAGINAS:
                # Guarda um elemento da página atual para detectar a troca de página
                livro_antigo = driver.find_element(By.CSS_SELECTOR, "article.product_pod")
                driver.find_element(By.CSS_SELECTOR, "li.next a").click()
                wait.until(EC.staleness_of(livro_antigo))

        print(f"\nTotal de livros extraídos: {len(todos_os_livros)}")
    finally:
        driver.quit()


if __name__ == "__main__":
    main()

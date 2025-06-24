# ===============================================================
# Objetivo:
# Aprender a navegar entre múltiples páginas (paginación),
# seguir enlaces tipo "Next", y recolectar información en cada una.
#
# Descripción:
# El script entra a https://quotes.toscrape.com,
# navega por las primeras 3 páginas,
# y recolecta todas las frases y sus autores.
#
# Qué se debe conseguir:
# Imprimir en consola frases como:
# Quote: “The world as we have created it is a process of our thinking...” - Albert Einstein
# Quote: “It is our choices, Harry, that show what we truly are...” - J.K. Rowling
# ...
# ===============================================================

from playwright.sync_api import sync_playwright

url = 'https://quotes.toscrape.com/page/1/'

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=1000) # Iniciar el navegador en modo no headless para ver la acción
    page = browser.new_page()
    page.goto(url)

    page.wait_for_load_state() # Esperar a que la página cargue completamente para todos los recursos

    for i in range(3):
        print(f"--- Página {i+1} ---")
        page.wait_for_selector("div.quote")  # Esperar a que carguen las citas
        quote = page.locator('div.quote')

        total_quotes = quote.count()
        for j in range(total_quotes):
            texto = quote.nth(j).locator('span.text').inner_text()
            autor = quote.nth(j).locator('small.author').inner_text()
            print(f'Quote: {texto} - {autor}')

        next_button = page.locator('li.next a')
        if next_button.count() > 0:
            next_button.click()
            

    print("Fin de la extracción de citas.")

    browser.close() # Cerrar el navegador



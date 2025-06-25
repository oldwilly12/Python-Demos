# ===============================================================
# Objetivo:
# Aprender a interactuar con formularios y botones,
# esperar resultados y extraer listas de elementos.
#
# Descripción:
# El script accede a https://duckduckgo.com,
# realiza una búsqueda con el texto "Python Playwright",
# y extrae los títulos de los primeros 5 resultados de búsqueda.
#
# Qué se debe conseguir:
# Imprimir en consola los títulos de los primeros resultados, por ejemplo:
# Result 1: Playwright: Fast and reliable end-to-end testing
# Result 2: Playwright · GitHub
# ...


from playwright.sync_api import sync_playwright

url = 'https://www.google.com/'

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=1000) # Iniciar el navegador en modo no headless para ver la acción
    page = browser.new_page()
    page.goto(url)

    page.wait_for_load_state() # Esperar a que la página cargue completamente para todos los recursos

    page.locator("[name='q']").fill('Python Playwright');
    page.keyboard.press('Enter')
    # page.locator('button[type="submit"]').click();

    page.wait_for_selector('a.result__a') # Esperar a que la página cargue completamente para todos los recursos

    resultados = page.locator('article h2')
    print(resultados)

    for i in range(5):
        texto = resultados.nth(i).inner_text()
        print(f"Result {i+1}: {texto}")


    browser.close() # Cerrar el navegador


    # extras
    # simular enter
    # page.keyboard.press('Enter')
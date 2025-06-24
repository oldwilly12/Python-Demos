# ===============================================================
# Objetivo:
# Aprender a abrir una página web, esperar que cargue
# y extraer información básica como el título, encabezados y párrafos.
#
# Descripción:
# Este script visita https://example.com y obtiene:
# - El contenido de la etiqueta <title>
# - El texto del encabezado principal <h1>
# - El texto del primer párrafo <p>
#
# Qué se debe conseguir:
# Imprimir en consola:
# - Title: Example Domain
# - H1: Example Domain
# - Description: This domain is for use in illustrative examples in documents...
# ===============================================================


from playwright.sync_api import sync_playwright

url = 'https://es.wikipedia.org/wiki/Alejandro_Magno'

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=1000) # Iniciar el navegador en modo no headless para ver la acción
    page = browser.new_page()
    page.goto(url)

    page.wait_for_load_state() # Esperar a que la página cargue completamente para todos los recursos

    title = page.title()
    encabezas = page.locator('h1 span').first.text_content()
    primer_parrafo = page.locator("p").first.text_content()
    print(f"Title: {title}")
    print(f"H1: {encabezas}")
    print(f"Description: {primer_parrafo}")

    browser.close() # Cerrar el navegador
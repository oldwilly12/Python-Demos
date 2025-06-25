# ------------------------------------------------------------
# Objetivo:
# Extraer información desde múltiples páginas usando Playwright, 
# recorriendo la paginación automática (botón "Next").
#
# Descripción:
# Este ejercicio navega a un sitio web con varias páginas de contenido
# (https://quotes.toscrape.com/), y recorre todas las páginas haciendo 
# click en el botón "Next" hasta que ya no esté disponible. En cada página, 
# se extraen las citas (quote + autor) y se almacenan en una lista.
#
# Qué se debe conseguir:
# - Abrir la página de inicio
# - Extraer citas y autores de la primera página
# - Detectar si existe un botón "Next"
# - Si existe, hacer click y repetir el proceso
# - Finalizar cuando no haya más páginas
# - (Opcional) Guardar los resultados en un archivo CSV o JSON
#
# Herramientas clave:
# - while True: para recorrer indefinidamente
# - page.locator("li.next a") para detectar el botón de "Next"
# - .click() para cambiar de página
# - .inner_text() para obtener contenido de cada cita
# - with open(...) o pandas para guardar resultados
# ------------------------------------------------------------

from playwright.sync_api import sync_playwright
from datetime import date
import json
import os

def extract_quotes(url, folder_name):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=1000)
        page = browser.new_page()
        page.goto(url)

        page.wait_for_load_state()

        quotes = []

        while True:
            # Extraer citas y autores de la página actual
            quotes_elements = page.locator("div.quote")
            quotes_count = quotes_elements.count()
            for i in range(quotes_count):
                quotes_text = quotes_elements.nth(i).locator("span.text").inner_text()
                author_text = quotes_elements.nth(i).locator("span small.author").inner_text()

                quotes.append({
                    "quote": quotes_text,
                    "author": author_text
                })

            next_button = page.locator("li.next a")
            if next_button.count() == 0:
                break

            next_button.click()
            page.wait_for_selector('div.quote')

        
        # Guardar los resultados en un archivo JSON
        today = date.today().strftime("%Y-%m-%d")
        filename = f"quotes_{today}.json"

        if not os.path.exists(folder_name):
            os.makedirs(folder_name)

        filename = os.path.join(folder_name, filename)

        with open(filename, "w", encoding="utf-8") as f:
            json.dump(quotes, f, indent=4, ensure_ascii=False)

        print(f"Resultados guardados en {filename}")



extract_quotes("https://quotes.toscrape.com/", 'quotes_Json')

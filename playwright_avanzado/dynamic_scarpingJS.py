# ------------------------------------------------------------
# Objetivo:
# Aprender a extraer datos de páginas que cargan contenido de forma
# dinámica mediante JavaScript o peticiones AJAX.
#
# Descripción:
# Muchas páginas modernas no cargan todos sus datos al principio,
# sino que los insertan después de unos segundos, scroll o acciones.
# Este ejercicio se enfoca en detectar y esperar correctamente
# la aparición de este contenido para poder hacer scraping exitoso.
#
# Qué se debe conseguir:
# - Cargar una página con contenido dinámico (por ejemplo: https://quotes.toscrape.com/scroll o https://books.toscrape.com/)
# - Esperar con precisión hasta que el contenido deseado aparezca
# - Extraer datos una vez cargados (por ejemplo, libros o posts)
# - Evitar errores por intentar leer contenido que aún no existe
#
# Herramientas clave:
# - page.wait_for_selector('selector') para esperar que algo aparezca
# - page.wait_for_timeout(ms) como forma básica de esperar tiempo fijo
# - page.locator('...').count() para verificar si ya hay resultados
# - page.evaluate() si quieres esperar por condiciones en el DOM
# ------------------------------------------------------------

from playwright.sync_api import sync_playwright
from datetime import date
import json 
import os

def scroll_and_scrape_quotes(url, folder_name='scroll_quotes'):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=1000)
        page = browser.new_page()
        page.goto(url)

        page.wait_for_selector('div.quote')

        previus_count = 0
        max_scrolls = 20
        quotes_data = []

        for _ in range(max_scrolls):
            doc = page.evaluate('() => window.scrollBy(0, document.body.scrollHeight)')
            quotes = page.locator('div.quote')
            current_count = quotes.count()

            if current_count == previus_count:
                print(f'No hay mas citas para extraer. Se han extraido {len(quotes_data)} citas.')
                break

            for i in range(previus_count, current_count):
                quotes_text = quotes.nth(i).locator('span.text').inner_text()
                author_text = quotes.nth(i).locator('span small.author').inner_text()

                quotes_data.append({
                    "quote": quotes_text,
                    "author": author_text
                })

            previus_count = current_count

            # Scroll hacia abajo para cargar mas
            # with evaluate_handle or evaluate but like a function () => {}
            page.evaluate_handle("window.scrollBy(0, document.body.scrollHeight)")
            page.wait_for_timeout(1000)  # Esperar a que se cargue más contenido

        # Guardar los datos en un archivo JSON
        today = date.today().strftime("%d-%m-%Y")
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)

        filename = os.path.join(folder_name, f"quotes_{today}.json")
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(quotes_data, f, indent=4, ensure_ascii=False)

        print(f'Se han extraido {len(quotes_data)} citas y se han guardado en {filename}')

        browser.close()





scroll_and_scrape_quotes('https://quotes.toscrape.com/scroll')

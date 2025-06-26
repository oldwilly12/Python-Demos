# ------------------------------------------------------------
# Objetivo:
# Aprender a interactuar con elementos tipo dropdown/select y filtros
# dinámicos en una página web usando Playwright.
#
# Descripción:
# Este ejercicio consiste en abrir una página que contiene un dropdown
# (menú desplegable) o filtros para seleccionar categorías, colores,
# u otras opciones. El objetivo es seleccionar diferentes opciones
# y extraer el contenido filtrado que aparece en la página después
# de cada selección.
#
# Qué se debe conseguir:
# - Abrir una página web con dropdown o filtros (ejemplo: https://www.demoblaze.com/)
# - Interactuar con el dropdown para cambiar la selección
# - Esperar a que la página muestre el contenido filtrado
# - Extraer y mostrar la información correspondiente a la selección
#
# Herramientas clave:
# - page.select_option(selector, value) para elegir una opción en dropdown
# - page.locator(selector).click() para interactuar con filtros
# - page.wait_for_selector(selector) para esperar cambios en el contenido
# - page.locator(selector).inner_text() para obtener texto actualizado
# ------------------------------------------------------------

from playwright.sync_api import sync_playwright

def info_dropdown(url):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=1000)
        page = browser.new_page()
        page.goto(url)

        page.wait_for_load_state()

        list_group_a = page.locator('div.list-group a#itemc')
        list_count = list_group_a.count()

        # thorugh categories
        for i in range(list_count):
            category =list_group_a.nth(i).inner_text()
            list_group_a.nth(i).click()
            print(f'category: {category}')
            page.wait_for_selector('div.card-block')
            cards_blocks = page.locator('div.card-block')
            cards_count = cards_blocks.count()
        #     # through cards
            for j in range(cards_count):
                object_name = cards_blocks.nth(j).locator('h4 a').inner_text()
                price = cards_blocks.nth(j).locator('h5').inner_html()
                print(f'object_name: {object_name} - price: {price}')
                



info_dropdown('https://www.demoblaze.com/')






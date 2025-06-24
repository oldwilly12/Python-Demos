# ------------------------------------------------------------
# Objetivo:
# Realizar scraping de una tabla HTML desde una página web y
# guardar los datos extraídos en un archivo CSV local.
#
# Descripción:
# Este ejercicio utiliza Playwright para abrir una página que 
# contiene una tabla de datos (por ejemplo, estadísticas de 
# población, COVID, economía, etc.). Se extraen los encabezados 
# de la tabla (<th>) y el contenido de cada fila (<td>), 
# organizándolos en un formato estructurado para exportarlos a CSV.
#
# Qué se debe conseguir:
# - Navegar a una página web con tabla (ej: https://www.worldometers.info/coronavirus/)
# - Esperar a que cargue la tabla
# - Extraer los encabezados de la tabla (nombres de columna)
# - Extraer cada fila de datos de forma ordenada
# - Guardar los datos en un archivo .csv usando Python
#
# Herramientas clave:
# - page.locator("table") o page.locator("table tbody tr")
# - row.locator("td").nth(i).inner_text() para acceder a cada celda
# - row.locator("th").nth(i).inner_text() para encabezados si están en <th>
# - csv.writer() para guardar los datos en un archivo CSV
# - page.wait_for_selector("table") para asegurar que la tabla esté lista
# ------------------------------------------------------------

from playwright.sync_api import sync_playwright
from datetime import date
import pandas as pd
import csv
import os

def scrape_table_to_csv(url, csv_folder='data'):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=1000)
        page = browser.new_page()
        page.goto(url)

        page.wait_for_selector('table')  # Esperar a que la tabla esté disponible

        thead = page.locator('table#main_table_countries_today thead tr th')

        thead_count = thead.count()
        
        headers = [thead.nth(i).inner_text().strip() for i in range(thead_count)]

        tbody = page.locator('tbody')
        tr = tbody.locator('tr')
        rows_count = tr.count()

        data = []

        for i in range(rows_count):
            row = tr.nth(i)
            row_data = []
            for j in range(thead_count):
                cell = row.locator('td').nth(j)
                cell_text = cell.inner_text().strip()
                row_data.append(cell_text)
            if any(row_data):
                data.append(row_data)

        #Create DataFrame con pandas
        df = pd.DataFrame(data, columns=headers)

        hoy = date.today()
        if not os.path.exists(csv_folder):
            os.makedirs(csv_folder)

        csv_filename = os.path.join(csv_folder, f'coronavirus_data_{hoy.strftime("%Y-%m-%d")}.csv')

        df.to_csv(csv_filename, index=False, encoding='utf-8')

        print(f"Archivo CSV guardado en: {csv_filename}")

        browser.close()


scrape_table_to_csv('https://www.worldometers.info/coronavirus/', 'coronavirus_data.csv')
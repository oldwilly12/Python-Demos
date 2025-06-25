# ------------------------------------------------------------
# Objetivo:
# Realizar un scraping de imágenes desde una página web y 
# descargarlas en una carpeta local utilizando Playwright y requests.
#
# Descripción:
# Este ejercicio utiliza Playwright para navegar por un sitio web 
# (como books.toscrape.com), encontrar todas las imágenes visibles 
# en una sección, extraer la URL de cada imagen (`src`) y luego 
# descargarlas con la biblioteca `requests`.
#
# Qué se debe conseguir:
# - Abrir una página con múltiples imágenes (por ejemplo, portadas de libros).
# - Localizar todos los elementos <img> y obtener el atributo src.
# - Completar las URLs relativas si es necesario (base URL + src).
# - Usar requests para descargar cada imagen.
# - Guardar las imágenes en una carpeta local con nombres únicos.
#
# Herramientas clave:
# - page.locator("img") → para obtener todos los elementos <img>
# - .get_attribute("src") → para extraer el enlace de la imagen
# - requests.get(url).content → para descargar la imagen
# - with open(...) as f: f.write(...) → para guardarla localmente

# url: https://books.toscrape.com/
# ------------------------------------------------------------

from playwright.sync_api import sync_playwright
from urllib.parse import urljoin
import requests
import os

def download_images_from_page(url, download_folder='downloaded_images'):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=1000)
        page = browser.new_page()
        page.goto(url)

        page.wait_for_load_state()  # Esperar a que la página cargue completamente

        # Localizar todos los elementos <img>
        images = page.locator('img')
        
        if not os.path.exists(download_folder):
            os.makedirs(download_folder)

        imgCount = images.count()
        for i in range(imgCount):
            src = images.nth(i).get_attribute('src')
            if src:
                # completar url
                if not src.startswith('http'):
                    src = urljoin(url, src)

                # descargar imagen
                response = requests.get(src)
                if response.status_code == 200:
                    img_name = f'image_{i+1}.jpg'
                    img_path = os.path.join(download_folder, img_name)
                    with open(img_path, 'wb') as f:
                        #wb = write binary
                        # Esto es necesario cuando escribes imágenes, PDFs o archivos que no son texto
                        f.write(response.content)
                    

        browser.close()  # Cerrar el navegador



download_images_from_page(url='https://books.toscrape.com/')
print("Descarga de imágenes completada.")
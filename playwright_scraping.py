from playwright.sync_api import sync_playwright

url = 'https://midu.dev/'

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=1000) # Iniciar el navegador en modo no headless para ver la acción
    page = browser.new_page()
    page.goto(url)

    first_article_anchor = page.locator('article a').first
    first_article_anchor.click()

    page.wait_for_load_state() # Esperar a que la página cargue completamente para todos los recursos

    first_image = page.locator('main img').first
    image_src = first_image.get_attribute('src')
    print(f"La URL de la imagen es: {image_src}") # Imprimir la URL de la imagen en la consola (image_src)

    ## buscar con text
    curso_context_container = page.locator('text="Contenido del curso"')
    curso_contect_simbling = curso_context_container.locator('xpath=./following-sibling::*')

    browser.close() # Cerrar el navegador
# ------------------------------------------------------------
# Objetivo:
# Acceder a una página web protegida por login, iniciar sesión
# con credenciales y hacer scraping de contenido solo disponible
# para usuarios autenticados.
#
# Descripción:
# Este ejercicio utiliza Playwright para simular un inicio de sesión 
# en un sitio web con formulario (usuario/contraseña). Una vez 
# dentro, se accede a la página protegida y se extrae información 
# como textos, enlaces u otros datos que no son visibles sin sesión.
# Se puede aplicar a foros, paneles de usuario, dashboards, etc.
#
# Qué se debe conseguir:
# - Navegar a la página de login (ej: https://quotes.toscrape.com/login)
# - Rellenar los campos de usuario y contraseña con Playwright
# - Hacer clic en el botón de "Login" o enviar el formulario
# - Verificar si el login fue exitoso (ej: que aparezca un botón de logout o el nombre del usuario)
# - Navegar a una página protegida (como https://quotes.toscrape.com/)
# - Extraer contenido exclusivo para usuarios autenticados
#
# Herramientas clave:
# - page.fill('input[name="username"]', 'usuario')
# - page.fill('input[name="password"]', 'contraseña')
# - page.locator('input[type="submit"]').click()  # para enviar el formulario
# - page.wait_for_url(...) o page.wait_for_selector(...) después del login
# - Comprobación post-login (buscar texto, enlaces o cookies)
# - Scraping normal después de estar autenticado
# ------------------------------------------------------------


from playwright.sync_api import sync_playwright

def login_and_scrape(url):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=1000)
        page = browser.new_page()
        page.goto(url)

        page.wait_for_load_state()

        page.fill('input#username', 'oldWillxxx')
        page.fill('input#password', 'Zimgir12')

        page.locator('input[type="submit"]').click()

        page.wait_for_selector('div.quote')  # Esperar a que la página cargue después del login

        # Verificar si el login fue exitoso
        if page.locator('a[href="/logout"]').is_visible():
            print("Login exitoso")
        else:
            print("Login fallido")
            browser.close()
            return
        
        qutoes = page.locator('div.quote')
        quotes_count = qutoes.count()

        print(f"quotes on the first page: {quotes_count} \n")

        for i in range(quotes_count):
            quote_text = qutoes.nth(i).locator('span.text').inner_text()
            author = qutoes.nth(i).locator('small.author').inner_text()
            print(f'Quote {i+1}: {quote_text} - {author}')

        browser.close()


login_and_scrape('https://quotes.toscrape.com/login')






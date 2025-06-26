# ------------------------------------------------------------
# Objetivo:
# Aprender a iniciar sesión en un sitio, guardar la sesión
# (cookies o localStorage), y reutilizarla en futuras ejecuciones
# sin volver a hacer login.
#
# Descripción:
# El script realiza el login con usuario/contraseña y guarda
# la sesión en un archivo. En la próxima ejecución, detecta si
# ese archivo existe y la reutiliza sin mostrar el formulario.
#
# Qué se debe conseguir:
# - Iniciar sesión en un sitio (por ejemplo, https://quotes.toscrape.com/login)
# - Guardar las cookies y/o localStorage después del login
# - Leer esas cookies/localStorage en el siguiente inicio
# - Verificar que estamos logueados automáticamente (sin formulario)
#
# Herramientas clave:
# - context.storage_state(path="archivo.json")
# - browser.new_context(storage_state="archivo.json")
# - page.context.add_cookies(...) (alternativa avanzada)
# ------------------------------------------------------------


from playwright.sync_api import sync_playwright
import os

SESSION_FILE = 'session.json'
LOGIN_URL = 'https://quotes.toscrape.com/login'
HOME_URL = 'https://quotes.toscrape.com/'

def save_session(playwright):
    browser = playwright.chromium.launch(headless=False, slow_mo=1000)
    context = browser.new_context()
    page = context.new_page()
    page.goto(LOGIN_URL)

    page.fill('input#username', 'admin')
    page.fill('input#password', 'admin')
    page.click('input[type="submit"]')

    # Confirmar que el login fue exitoso
    if page.locator('a[href="/logout"]').is_visible():
        print("✅ Login exitoso. Guardando sesión...")
        context.storage_state(path=SESSION_FILE)
    else:
        print("❌ Login fallido. Revisa las credenciales.")

    browser.close()

def reuse_session(playwright):
    browser = playwright.chromium.launch(headless=False, slow_mo=1000)
    context = browser.new_context(storage_state=SESSION_FILE)
    page = context.new_page()
    page.goto(HOME_URL)

    if page.locator('a[href="/logout"]').is_visible():
        print("✅ Sesión reutilizada exitosamente. Ya estás logueado.")
    else:
        print("❌ No se pudo reutilizar la sesión.")

    browser.close()

def main():
    with sync_playwright() as playwright:
        if os.path.exists(SESSION_FILE):
            reuse_session(playwright)
        else:
            save_session(playwright)
            reuse_session(playwright)

main()




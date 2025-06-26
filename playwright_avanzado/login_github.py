from playwright.sync_api import sync_playwright
import os

SESSION_FILE = 'session.json'
LOGIN_URL = 'https://github.com/login'
HOME_URL = 'https://github.com/login'

def save_session(playwright):
    browser = playwright.chromium.launch(headless=False, slow_mo=1000)
    context = browser.new_context()
    page = context.new_page()
    page.goto(LOGIN_URL)

    page.fill('input#login_field', '###########')
    page.fill('input#password', '###########')
    page.click('input[type="submit"]')

    # Confirmar que el login fue exitoso
    if page.locator('div.AppHeader-user').is_visible():
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

    if page.locator('div.AppHeader-user').is_visible():
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


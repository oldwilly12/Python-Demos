# ------------------------------------------------------------
# Objetivo: Entrar al SAT, llenar RFC y contraseña,
# dejar que el usuario resuelva el CAPTCHA manualmente
# y guardar la sesión para reutilizarla después.
# ------------------------------------------------------------

from playwright.sync_api import sync_playwright
import os

LOGIN_URL = "https://login.siat.sat.gob.mx/"  # URL de login del SAT
HOME_URL ="https://login.siat.sat.gob.mx/nidp/portal?locale=en_US"
SESSION_FILE = "sat_session.json"

RFC = "##############"  # reemplaza con tu RFC real
PASSWORD = "###########"  # reemplaza con tu contraseña real

def guardar_sesion_manual():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=500)
        context = browser.new_context()
        page = context.new_page()
        page.goto(LOGIN_URL)

        page.wait_for_load_state("networkidle")
        # Llenar RFC y contraseña automáticamente (ajusta selectores si cambian)


        page.fill('input[name="Ecom_User_ID"]', RFC)
        page.fill('input#password', PASSWORD)

        print("\n🛑 Por favor resuelve el CAPTCHA manualmente y haz clic en 'Enviar'")
        print("▶ Cuando estés logueado, cierra sesión o avanza a otra página para validar acceso.")

        # Esperar a que el usuario loguee manualmente y aparezca algún elemento indicativo
        page.wait_for_selector('div#userDropdown', timeout=0)  # espera sin límite hasta que detecte logout

        print("✅ Login exitoso. Guardando sesión...")
        context.storage_state(path=SESSION_FILE)

        browser.close()
        print(f"💾 Sesión guardada en: {SESSION_FILE}")


def reuse_session(playwright):
    browser = playwright.chromium.launch(headless=False, slow_mo=1000)
    context = browser.new_context(storage_state=SESSION_FILE)
    page = context.new_page()
    page.goto(HOME_URL)

    page.wait_for_load_state("networkidle")

    if page.locator('div#userDropdown').count() > 0:
        print("✅ Sesión reutilizada exitosamente. Ya estás logueado.")
    else:
        print("❌ No se pudo reutilizar la sesión.")

    browser.close()

def main():
    with sync_playwright() as playwright:
        if os.path.exists(SESSION_FILE):
            reuse_session(playwright)
        else:
            guardar_sesion_manual(playwright)


main()
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









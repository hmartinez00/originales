**Paso 1: Importar las librerías necesarias**

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
```

**Paso 2: Definir el script**

```python
# Tiempo de espera (en segundos) para que la página se cargue
TIMEOUT = 10

# URL de la página
URL = "https://ejemplo.com"

# XPath del menú desplegable
MENU_XPATH = "//select[@id='menu']"

# XPath de la opción del menú desplegable
OPTION_XPATH = "//select[@id='menu']/option[@value='opcion1']"

# XPath de la tabla
TABLE_XPATH = "//table[@id='tabla']"

# Inicializar el navegador
driver = webdriver.Chrome()

# Abrir la página en modo pantalla completa
driver.maximize_window()

# Esperar a que la página se cargue
driver.get(URL)
WebDriverWait(driver, TIMEOUT).until(EC.presence_of_element_located((By.XPATH, TABLE_XPATH)))

# Desplegar el menú desplegable
menu_element = driver.find_element(By.XPATH, MENU_XPATH)
menu_element.click()

# Esperar a que el menú desplegable se abra
WebDriverWait(driver, TIMEOUT).until(EC.visibility_of_element_located((By.XPATH, OPTION_XPATH)))

# Seleccionar la opción del menú desplegable
option_element = driver.find_element(By.XPATH, OPTION_XPATH)
option_element.click()

# Extraer los datos de la tabla
table_element = driver.find_element(By.XPATH, TABLE_XPATH)
rows = table_element.find_elements(By.TAG_NAME, "tr")

# Iterar sobre las filas de la tabla e imprimir los datos
for row in rows:
    cells = row.find_elements(By.TAG_NAME, "td")
    for cell in cells:
        print(cell.text)
```
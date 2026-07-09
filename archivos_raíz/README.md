# 🧪 Automatización de Pruebas de API: Creación de Kits en Urban Grocers

Este proyecto se enfoca en la automatización de pruebas funcionales y de frontera (boundary testing) para el endpoint de creación de kits de productos en la plataforma Urban Grocers. El objetivo principal es garantizar que el backend valide correctamente el parámetro `name` según las reglas de negocio de la apiDoc oficial, manejando adecuadamente los flujos correctos y rechazando las peticiones inválidas.

---

## 🎯 Escenarios de Prueba Automatizados

El script implementa **9 pruebas funcionales específicas** utilizando técnicas de diseño de pruebas como clases de equivalencia y análisis de valores límite:

### ✅ Pruebas Positivas (Esperan HTTP 201 Created y validación de datos)
*   `test_create_kit_1_character_name_allowed`: Validación del límite inferior permitido (1 carácter).
*   `test_create_kit_511_character_name_allowed`: Validación del límite superior permitido (511 caracteres).
*   `test_create_kit_special_character_name_allowed`: Soporte para caracteres especiales (`№%@`).
*   `test_create_kit_space_character_name_allowed`: Manejo correcto de espacios intermedios (`A Aaa`).
*   `test_create_kit_number_character_name_allowed`: Aceptación de números formateados como string (`"123"`).

### ❌ Pruebas Negativas (Esperan HTTP 400 Bad Request e "Invalid parameters")
*   `test_create_kit_empty_character_name_not_allowed`: Rechazo de cadenas vacías (`""`).
*   `test_create_kit_512_character_name_not_allowed`: Bloqueo de valores que exceden el límite máximo (512 caracteres).
*   `test_create_kit_no_name_parameter_not_allowed`: Validación de payload inválido cuando el parámetro `name` está ausente (`{}`).
*   `test_create_kit_no_string_character_name_not_allowed`: Control de tipos de datos incorrectos (envío de un entero `123` en lugar de un string).

---

## 🛠️ Stack Tecnológico y Buenas Prácticas

*   **Lenguaje:** Python 3.x
*   **Framework de Testing:** Pytest
*   **Librerías Clave:** `requests` (Manejo de peticiones HTTP)
*   **Patrón de Diseño:** Modularización y separación de responsabilidades (Configuración, Datos y Peticiones).

### Aspectos Técnicos Destacados:
*   **Modularidad (Principio DRY):** Implementación de funciones helper de aserción (`check_positive_kit_response` y `check_negative_kit_response`) para evitar la duplicación de código de validación.
*   **Aislamiento de Datos:** Uso del método `.copy()` sobre el diccionario base (`data.kit_body`) para asegurar que la mutación de los payloads en una prueba no contamine ni altere el estado de los demás escenarios.
*   **Gestión de Autenticación:** Integración de flujos dinámicos mediante la generación automática de tokens de usuario (`get_new_user_token()`) requeridos para la cabecera de autorización de la API.

---

## 📁 Estructura del Proyecto

El repositorio está organizado de la siguiente manera para mantener el código limpio y mantenible:

*   `configuration.py`: Almacena las URLs base y las rutas de los endpoints de la API.
*   `data.py`: Contiene los headers base, cuerpos de solicitudes (payloads) y estructuras de datos de prueba.
*   `sender_stand_request.py`: Gestiona la lógica de las peticiones HTTP (`POST`, `GET`) utilizando la librería `requests`.
*   `create_kit_name_kit_test.py`: Contiene la suite lógica de las 9 pruebas automatizadas con Pytest *(este archivo aloja el código principal)*.

---

## Mi Rol y Decisiones de QA

Como **QA Engineer Junior**, mi objetivo principal en este proyecto fue asegurar la calidad funcional del sistema y el cumplimiento de las reglas del negocio, enfocándome en la validación y robustez del parámetro `name`.

### ¿Qué analicé?
* **Documentación oficial:** Revisé a detalle la especificación de la `apiDoc` para el endpoint de creación de kits.
* **Objetivo:** Identificar y desglosar los límites permitidos para el ingreso de cadenas de texto (strings).

### Técnicas de diseño de pruebas aplicadas
Para no hacer pruebas repetitivas y optimizar el tiempo, apliqué los conceptos teóricos básicos de testing:
* **Partición de Equivalencia**
* **Análisis de Valores Límite (Boundary Testing)**

### Riesgos cubiertos y casos de prueba
Diseñé y ejecuté escenarios específicos para evitar fallos comunes en producción:
* **Entradas inválidas:** Validé el comportamiento del sistema usando caracteres especiales, strings vacíos y espacios en blanco.
* **Pruebas de longitud extrema:** Validé los límites del campo ingresando longitudes críticas: `0`, `1`, `2`, un carácter menos del límite, el límite exacto y un carácter de más.
* **Control de errores:** Verifiqué que las peticiones inválidas devuelvan los mensajes de error corporativos correctos en lugar de romper el servidor (evitando los molestos errores 500).

### 💡 Aprendizajes clave
Este proyecto me ayudó a entender cómo aplicar la teoría matemática de límites en el día a día. Logré reducir el número de scripts necesarios, haciendo mi suite de pruebas mucho más eficiente.

---

## 🚀 Cómo Ejecutar las Pruebas Localmente

### 1. Clonar el repositorio
```bash
git clone https://github.com/AxelCastanedaG/qa-project-Urban-Grocers-app-es.git
cd qa-project-Urban-Grocers-app-es
```

### 2. Instalar dependencias
Asegúrate de contar con un entorno virtual activo e instala los paquetes necesarios usando el archivo de requerimientos:
```bash
pip install -r requirements.txt
```

### 3. Ejecutar la suite de pruebas
Para correr las pruebas y verificar las aserciones, ejecuta en tu terminal:
```bash
pytest create_kit_name_kit_test.py
```

---

## 📊 Impacto de Calidad (QA)
*   **Automatización Eficiente:** Sustitución de validaciones manuales repetitivas por una suite ejecutable en segundos.
*   **Robustez del Backend:** Verificación completa del comportamiento de strings y tipos de datos en la capa del cliente, previniendo fallos inesperados de tipo 500 en producción.

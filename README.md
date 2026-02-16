# Tarea-Manuel-

===========================================
YUGIOH CARDS - ETL + API + MONGODB + POWER BI
===========================================

📌 Descripción del Proyecto
Este proyecto consiste en la construcción de un proceso ETL para obtener información de cartas
desde una API externa, almacenarlas en MongoDB Atlas, exponer los datos mediante una API
desarrollada en FastAPI y finalmente visualizarlos en Power BI.

El objetivo es demostrar integración de tecnologías modernas de análisis de datos
y visualización empresarial.

-------------------------------------------
🛠 Tecnologías Utilizadas
-------------------------------------------

- Python
- FastAPI
- MongoDB Atlas
- PyMongo
- Pandas
- Power BI
- Requests
- Uvicorn

-------------------------------------------
📊 Arquitectura del Proyecto
-------------------------------------------

1️⃣ Extracción (Extract)
Se obtienen datos desde una API pública utilizando la librería requests.

2️⃣ Transformación (Transform)
Los datos son procesados con Pandas:
- Limpieza de valores nulos
- Selección de columnas relevantes
- Conversión de tipos de datos

3️⃣ Carga (Load)
Los datos transformados se insertan en MongoDB Atlas utilizando PyMongo.

4️⃣ Exposición de Datos
Se crea una API REST con FastAPI que permite:
- Obtener cartas con límite configurable
- Consultar estadísticas por atributo
- Generar agregaciones mediante pipelines de MongoDB

5️⃣ Visualización
Power BI consume los endpoints de la API para:
- Crear gráficos de distribución por atributo
- Mostrar estadísticas generales
- Generar dashboards interactivos

-------------------------------------------
📂 Endpoints Principales
-------------------------------------------

GET /
Mensaje de prueba para verificar que la API funciona.

GET /cards?limit=50
Obtiene un listado de cartas desde la base de datos.

GET /stats/attribute-distribution
Devuelve la distribución de cartas agrupadas por atributo
usando un pipeline de agregación en MongoDB.

-------------------------------------------
🚀 Cómo Ejecutar el Proyecto
-------------------------------------------

1. Clonar el repositorio
2. Instalar dependencias:
   pip install -r requirements.txt

3. Ejecutar la API:
   uvicorn main:app --reload

4. Acceder a:
   http://127.0.0.1:8000/docs

-------------------------------------------
📈 Integración con Power BI
-------------------------------------------

1. Publicar la API en ejecución
2. En Power BI seleccionar:
   Obtener datos → Web
3. Ingresar la URL del endpoint
4. Transformar datos si es necesario
5. Crear visualizaciones

-------------------------------------------
🎯 Objetivo Académico / Profesional
-------------------------------------------

Este proyecto demuestra:

- Implementación completa de un proceso ETL
- Uso de bases de datos NoSQL
- Creación de APIs REST modernas
- Integración con herramientas de Business Intelligence
- Construcción de dashboards interactivos

-------------------------------------------
👨‍💻 Autor
-------------------------------------------

Tomás Corvalán
Desarrollador Web & Data Projects
Chile

===========================================

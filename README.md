# Análisis de Datos de Películas TMDB 5000

Proyecto de análisis de datos que explora un conjunto de 5,000 películas de The Movie Database (TMDB), enfocándose en el rendimiento financiero, tendencias de género, evolución temporal y redes de colaboración entre actores.

## 📊 Descripción del Proyecto

Este proyecto analiza datos de películas para extraer insights sobre:
- **Rendimiento Financiero**: Análisis de ROI (Retorno de Inversión) por géneros y períodos
- **Tendencias Temporales**: Evolución de la duración de películas en los últimos 50 años
- **Redes de Colaboración**: Patrones de co-aparición de actores y colaboraciones frecuentes

## 🗂️ Dataset

**Fuente**: TMDB 5000 Movie Dataset
- `tmdb_5000_movies.csv`: Metadatos de películas (presupuesto, ingresos, géneros, fechas de estreno, duración)
- `tmdb_5000_credits.csv`: Información de reparto y equipo técnico

**Características principales**:
- ~5,000 películas
- Datos financieros (presupuesto, ingresos)
- Fechas de estreno e información temporal
- Clasificaciones por género (formato JSON)
- Información de reparto (formato JSON)

## 🔧 Tecnologías

- **Python 3.14**
- **Análisis de Datos**: pandas, numpy
- **Visualización**: matplotlib, seaborn
- **Análisis de Redes**: networkx
- **Entorno**: Jupyter Notebook, FastAPI
- **Gestión de paquetes**: pip, venv

## 📈 Análisis Principales

### 1. Análisis de ROI (Retorno de Inversión)
- Cálculo de ROI para películas con datos financieros válidos
- Identificación de mejores y peores resultados financieros
- Análisis de distribución de ROI por género
- Hallazgo: Los géneros de Terror/Thriller muestran ROI elevado debido a presupuestos controlados

**Fórmula**: `ROI = revenue / budget`

### 2. Rendimiento por Género
- Parseo de datos de género en formato JSON
- Cálculo de ROI promedio y mediano por género
- Visualización de los 15 géneros principales por ROI promedio
- Comparación de géneros individuales contra el promedio global

### 3. Evolución de la Duración (Runtime)
- Análisis de tendencias de duración de películas en los últimos 50 años
- Agregación de datos por década
- Seguimiento de cambios en duración promedio y mediana a lo largo del tiempo
- Identificación de patrones temporales en la producción cinematográfica

### 4. Red de Colaboración de Actores
- Extracción de información de reparto desde datos de créditos
- Construcción de red de co-apariciones (actores que aparecen juntos en ≥3 películas)
- Visualización de patrones de colaboración usando diseño de grafos dirigido por fuerzas
- Identificación de actores clave con alta frecuencia de colaboración
- Tamaño de nodos escalado por grado (número de colaboraciones)
- Etiquetas con fondo para mejor legibilidad

## 📁 Estructura del Proyecto

```
data_analyst/
├── data/
│   ├── tmdb_5000_movies.csv
│   ├── tmdb_5000_movies.csv.zip
│   ├── tmdb_5000_credits.csv
│   └── tmdb_5000_credits.csv.zip
├── artifacts/
│   ├── coacting_network.png
│   ├── roi_by_genre.png
│   └── roi_distribution.png
├── services/
│   ├── __init__.py
│   ├── data_loader.py
│   ├── roi_service.py
│   ├── runtime_evolution_service.py
│   └── actor_network_service.py
├── data_analyst.ipynb
├── app.py
├── requirements.txt
└── README.md
```

## 🚀 Comenzando

### Prerrequisitos

```bash
python3.14 -m venv .env
source .env/bin/activate  # En Linux/Mac
pip install -r requirements.txt
```

### Ejecutar el Análisis

1. Clonar el repositorio:
```bash
git clone <repository-url>
cd data_analyst
```

2. Activar el entorno virtual:
```bash
source .env/bin/activate
```

3. Ejecutar el notebook de Jupyter:
```bash
jupyter notebook data_analyst.ipynb
```

4. Ejecutar la API (FastAPI):
```bash
uvicorn app:app --reload || fastapi dev app.py
```

La API estará disponible en: `http://127.0.0.1:8000`

## 🌐 API Endpoints

- `GET /roi_by_genre` - Obtiene análisis de ROI por género
- `GET /roi_by_country` - Obtiene análisis de ROI por país
- `GET /runtime_evolution` - Obtiene evolución de duración por década
- `GET /actor_network` - Obtiene métricas de red de colaboración de actores

## 📊 Hallazgos Clave

### ROI y Rentabilidad
- **Distribución**: Altamente sesgada con pocas películas logrando retornos significativos
- **Géneros más rentables**: Horror/Thriller demuestran la mayor eficiencia de ROI
- **Rango**: La mayoría de películas tienen ROI entre 0.5 y 3.0
- **Outliers**: Algunas películas de bajo presupuesto logran ROI excepcionales (>100x)

### Evolución Temporal
- **Duración promedio**: Variación notable entre décadas
- **Tendencia**: Las películas modernas tienden a tener duraciones más consistentes
- **Rango típico**: 90-120 minutos para películas mainstream

### Redes de Colaboración
- **Red densa**: Actores frecuentes forman grupos de colaboración cerrados
- **Actores clave**: Ciertos actores funcionan como conectores entre diferentes grupos
- **Colaboraciones frecuentes**: Pares de actores que aparecen juntos en 3+ películas
- **Tamaño de red**: Cientos de nodos con miles de conexiones

## 🔍 Limpieza de Datos

### Tratamiento de valores nulos
- Filtrado de películas con presupuesto y revenue válidos (> 0)
- Manejo apropiado de valores faltantes en runtime
- Limpieza de fechas de estreno inválidas

### Transformación de datos
- Conversión de fechas de estreno a formato datetime
- Extracción de características: año, década
- Parseo de datos JSON estructurados (géneros, reparto)
- Cálculo de métricas derivadas (ROI)

### Preparación para análisis
- Normalización de nombres de actores
- Eliminación de duplicados
- Filtrado de outliers extremos cuando es necesario

## 📓 Estructura del Notebook

El notebook `data_analyst.ipynb` contiene:

1. **Lectura y Descripción del Dataset**
   - Carga de datos desde CSV
   - Exploración inicial de estructura y tipos

2. **Limpieza y Preparación**
   - Tratamiento de nulos
   - Conversión de tipos de datos
   - Parseo de campos JSON

3. **Análisis Exploratorio (EDA)**
   - Gráficos de distribución
   - Estadísticas descriptivas
   - Visualizaciones por categorías

4. **Respuestas a Preguntas de Análisis**
   - ROI por género (con visualizaciones)
   - Evolución temporal de runtime
   - Red de colaboración de actores

5. **Conclusiones y Comentarios**
   - Insights parciales en cada sección
   - Hallazgos principales
   - Recomendaciones

6. **Generación de Resultados**
   - Exportación de gráficos a `/artifacts`
   - Preparación de datos para la API

## 📝 Mejoras Futuras

- Añadir modelado predictivo para ROI
- Analizar influencia de directores en el rendimiento financiero
- Incorporar datos de calificaciones y reseñas
- Expandir análisis temporal con valores ajustados por inflación
- Añadir detección de comunidades en redes de actores
- Análisis de correlación entre presupuesto y éxito crítico
- Estudiar el impacto de las plataformas de streaming
- Análisis de palabras clave y temáticas recurrentes

## 🛠️ Servicios Implementados

### `data_loader.py`
Carga y preprocesa los datos de películas y créditos.

### `roi_service.py`
Calcula y agrupa ROI por género y país.

### `runtime_evolution_service.py`
Analiza la evolución de la duración de películas por década.

### `actor_network_service.py`
Construye y analiza la red de colaboración entre actores usando NetworkX.

## 📦 Dependencias Principales

```
fastapi
uvicorn
pandas
numpy
matplotlib
seaborn
networkx
jupyter
```

Ver `requirements.txt` para la lista completa de dependencias.

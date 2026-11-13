# 🧙‍♂️ DSLR - Data Science x Logistic Regression (42)

Implementación desde cero de herramientas de análisis estadístico, visualización de datos y un clasificador de **Regresión Logística Multiclase (Softmax)** en Python puro para recrear el Sombrero Seleccionador de Hogwarts.

---

## 📋 Tabla de Contenidos
- [Descripción del Proyecto](#-descripción-del-proyecto)
- [Arquitectura del Modelo](#-arquitectura-del-modelo)
- [Estructura del Repositorio](#-estructura-del-repositorio)
- [Instalación y Uso](#-instalación-y-uso)
- [Resultados Obtenidos](#-resultados-obtenidos)

---

## 📖 Descripción del Proyecto

El objetivo de **DSLR** es explorar un conjunto de datos con calificaciones de estudiantes de Hogwarts en 13 asignaturas mágicas y construir un modelo de aprendizaje automático capaz de clasificar a cada alumno en su casa correspondiente (*Gryffindor*, *Hufflepuff*, *Ravenclaw* o *Slytherin*) sin utilizar librerías de alto nivel para los cálculos matemáticos o estadísticos.

El proyecto se divide en tres fases:
1. **Análisis Estadístico (`describe.py`):** Cálculo manual de métricas descriptivas (conteo, media, desviación estándar, mínimo, cuartiles y máximo) ignorando valores nulos (`NaN`).
2. **Visualización de Datos (`histogram.py`, `scatter_plot.py`, `pair_plot.py`):** Identificación de distribuciones homogéneas, características correlacionadas y selección de variables relevantes para el entrenamiento.
3. **Clasificación Multiclase (`logreg_train.py`, `logreg_predict.py`):** Entrenamiento mediante descenso de gradiente y generación de predicciones sobre datos nuevos.

---

## 🧠 Arquitectura del Modelo

El clasificador está implementado en `ft_dslr.py` utilizando únicamente la biblioteca estándar de Python (`math`, `random`, `csv`, `json`):

* **Preprocesamiento y Normalización (Z-Score):** Estandarización de las 13 características numéricas (\(z = \frac{x - \mu}{\sigma}\)) para evitar desbordamientos numéricos y acelerar la convergencia. Los parámetros μ y σ del conjunto de entrenamiento se almacenan en `model.json` para escalar los datos de prueba e imputar valores faltantes (`NaN`).
* **Función de Activación (Softmax):** Conversión de puntuaciones lineales en probabilidades normalizadas con estabilidad numérica (`max_z` trick).
* **Función de Coste (Cross-Entropy Loss):** Optimización mediante **Descenso de Gradiente Estocástico (SGD)** con mezcla aleatoria (*shuffle*) de muestras en cada época.

---

## 📂 Estructura del Repositorio

```text
├── data_analysis.py       # Clase de carga, limpieza y estadística descriptiva
├── data_visualization.py  # Utilidades gráficas
├── describe.py            # Resumen estadístico estilo pandas.describe()
├── histogram.py           # Histogramas de distribución por asignatura y casa
├── scatter_plot.py        # Gráficos de dispersión para detectar correlaciones
├── pair_plot.py           # Matriz de dispersión entre asignaturas
├── ft_dslr.py             # Implementación de la clase LogisticRegression
├── logreg_train.py        # Script de entrenamiento y exportación de pesos (model.json)
├── logreg_predict.py      # Script de predicción y generación de houses.csv
├── logreg_test.py         # Script de evaluación y comparación de métricas
├── model.json             # Pesos, sesgos y parámetros de normalización entrenados
└── houses.csv             # Predicciones generadas sobre el conjunto de prueba
```

---

## 🚀 Instalación y Uso

### 1. Clonar el repositorio
```bash
git clone https://github.com
cd Ft_dslr-42
```

### 2. Análisis Descriptivo
```bash
python describe.py dataset_train.csv
```

### 3. Visualización de Datos
```bash
python histogram.py dataset_train.csv
python scatter_plot.py dataset_train.csv
python pair_plot.py dataset_train.csv
```

### 4. Entrenamiento del Modelo
Entrena el clasificador durante 1500 épocas y guarda los parámetros aprendidos en `model.json`:
```bash
python logreg_train.py dataset_train.csv
```

### 5. Predicción
Carga `model.json`, imputa valores faltantes con las medias del entrenamiento y exporta las predicciones a `houses.csv`:
```bash
python logreg_predict.py dataset_test.csv model.json
```

---

## 📊 Resultados Obtenidos

El modelo alcanzó una convergencia estable con un coste final de **Loss: `0.1009`**, logrando un **99.00% de precisión** (396/400 aciertos) frente al conjunto de validación oficial (`dataset_truth.csv`), superando el umbral del 98% requerido por el proyecto.

| Casa de Hogwarts | Predicciones (`houses.csv`) | Reales (`dataset_truth.csv`) | Diferencia |
| :--- | :---: | :---: | :---: |
| **Gryffindor** | 79 | 78 | +1 |
| **Hufflepuff** | 144 | 142 | +2 |
| **Ravenclaw** | 114 | 114 | 0 |
| **Slytherin** | 63 | 66 | -3 |
| **Total** | **400** | **400** | **99.00% Accuracy** |

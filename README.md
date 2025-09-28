# Consumo de café y parámetros de salud ☕️🩺🖥

Este proyecto analiza un dataset público proveniente de Kaggle, que contiene información sobre hábitos de consumo de café en diferentes grupos demográficos. El objetivo fue limpiar los datos, explorar patrones de consumo teniendo en cuenta género, edad y país de residencia, y generar visualizaciones que permitan obtener insights relevantes, particularmente respecto a la relación entre el consumo y parámetros de salud, tales como la calidad del sueño, hábitos de actividad física, frecuencia cardíaca, índice de masa corporal (BMI), entre otros.


Fuente: https://www.kaggle.com/datasets/uom190346a/global-coffee-health-dataset

#Variables principales:

 🔸"Age":	Integer - Edad del participante en años cumplidos (18-80 años)
 
 🔸"Gender":	Categórico	- Hombre, Mujer, Otro
 
 🔸"Country":	Categórico	- País de residencia (20 países encuestados)
 
 🔸"Coffee_Intake":	Float -	Consumo diario de café en tazas (0-10)
 
 🔸"Caffeine_mg":	Float	- Ingesta diaria estimada de cafeína en mg (1 taza ≈ 95 mg)
 
 🔸"Sleep_Hours":	Float -	Promedio de horas de sueño por noche (3-10 horas)
 
 🔸"Sleep_Quality":	Categórico -	Pobre, Regular, Bueno, Excelente (basado en las horas de sueño)
 
 🔸"BMI":	Float -	Índice de masa corporal (15-40)
 
 🔸"Heart_Rate":	Integer	- Frecuencia cardíaca en reposo (50-110 lpm)
 
 🔸"Stress_Level": Categórico	- Bajo, Medio, Alto (basado en las horas de sueño y el estilo de vida)
 
 🔸"Physical_Activity_Hours":	Float	- Actividad física semanal (0-15 horas)
 
 🔸"Occupation":	Categórico	- Oficina, Cuidado de la salud, Estudiante, Servicio, Otro
 

#Metodología de trabajo:
 1. Importar librerías para exploración y limpieza de datos
 2. Cargar datos
 3. Limpieza de datos
 Búsqueda de valores nulos
 4. Análisis exploratorio
 Estadísticas descriptivas

## Dashboard Power BI
#Se complementan los primeros hallazgos identificados a través de las visualizaciones con recursos de Power BI para generar un reporte.
- Archivo: Reporte Coffee Project.pbit
- Visualiza las tendencias
- Requiere Power BI Desktop para abrir

#Resultados: 

  🔷 Entre los países evaluados, España y Noruega muestran un consumo ligeramente mayor, pero las diferencias entre países son pequeñas, lo que sugiere una homogeneidad global en los hábitos de café.

  🔷 Dentro de los participantes de la muestra, se reconoce un sesgo entre los jóvenes de 18 años, que representan una proporción amplia de la muestra, pero un bajo consumo real de café. Esto indica que gran parte de ellos no consume café, mientras que otros grupos etarios, con menores unidades de análisis consumirían más café.

  🔷 No hubo una diferencia significativa en las tazas de café consumidas en función del sexo, ni de la ocupación de las personas. Los consumos se mantienen dentro de un rango estable de 2,4 a 2,6 tazas, lo que refuerza la idea de que el café es un hábito transversal, independiente del rol social.

  🔷 La suma de horas de actividad física y tazas de café consumidas según índice de masa corporal, muestra que los mayores consumos de café y niveles de actividad física se concentran en personas con IMC dentro del rango saludable (20–25), lo que podría indicar que el café acompaña estilos de vida más activos, mostrando una distribución normal.

  🔷 A mayores consumos de cafeína, se aprecia una mayor frecuencia cardíaca en reposo, y una disminución de las horas de sueño. Asimismo, el promedio de horas de sueño se relaciona de manera inversa con niveles de estrés y promedio de cafeína consumida, impactando en la calidad del sueño. Estos hallazgos refuerzan la idea de que los hábitos de consumo de café interactúan con factores fisiológicos y psicosociales.





 


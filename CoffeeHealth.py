# Exploración y limpieza de datos
# 1. Importar librerías
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# 2. Cargar datos
coffee = pd.read_csv("synthetic_coffee_health_10000 - Copy.csv")
# Vista inicial
print(coffee.head())
print(coffee.info())
# 3. Limpieza de datos
# Búsqueda de valores nulos
print(coffee.isna().sum())

#Reemplazo de valores nulos en la variable categórica Health_Issues. Los valores faltantes se
# reemplazaron por el término "No condition" para evitar confusión, ya que no se trataba de una
# categoría en sí misma, sino de la ausencia de información.

coffee["Health_Issues"].fillna("No condition", inplace=True)

# 4. Análisis exploratorio
# Estadísticas descriptivas

print(coffee["Coffee_Intake"].describe())
print(coffee["Gender"].describe())
print(coffee["Country"].describe())
print(coffee["Age"].describe())
# Consumo promedio por país
avg_country = (coffee.groupby("Country")["Coffee_Intake"]
                      .mean()
                      .sort_values(ascending=False))
print(avg_country.head())
# 5. Visualizaciones
# Histograma de edad
sns.histplot(coffee["Age"], bins=10, color="brown")
plt.title("Distribución de participantes por edad")
plt.xlabel("Edad")
plt.ylabel("Frecuencia")
plt.show()
# Boxplot por género
sns.boxplot(data=coffee, x="Gender", y="Caffeine_mg", palette="Set2")
plt.title("Consumo de café por género")
plt.xlabel("Género")
plt.ylabel("Mg por día")
plt.show()
# Relación entre consumo y calidad de sueño
sns.scatterplot(data=coffee, x="Caffeine_mg", y="Sleep_Hours", alpha=0.2)
sns.regplot(data=coffee, x="Caffeine_mg", y="Sleep_Hours",
            scatter=False, color="red")
plt.title("Consumo de café vs Calidad del sueño")
plt.xlabel("Mg de cafeína por día")
plt.ylabel("Horas de sueño")
plt.show()

plt.hexbin(coffee["Caffeine_mg"], coffee["Sleep_Hours"], gridsize=30, cmap="Blues", alpha=0.8)
plt.colorbar(label="Número de personas")
plt.xlabel("Mg de cafeína por día")
plt.ylabel("Horas de sueño")
plt.title("Consumo de café vs Calidad del sueño")
plt.ylim(1, 10)
plt.show()

#Se complementan estos primeros hallazgos identificados a través de las visualizaciones con recursos
# de Power BI para generar un reporte.

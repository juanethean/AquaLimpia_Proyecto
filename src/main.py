import sys
import os
import matplotlib.pyplot as plt
import seaborn as sns

# Asegurar que el script encuentre el módulo
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import funciones_limpias as fa

# 1. Cargar datos
ruta_datos = 'data/dataset_set_A_aguas_residuales.xlsx'
df = fa.cargar_datos(ruta_datos)

if df is not None:
    # 2. Generar reportes
    print("\n--- Generando Reportes ---")
    fa.generar_reporte_operaciones(df, 'outputs/reporte_operaciones.csv')
    fa.generar_reporte_ambiental(df, 'outputs/reporte_ambiental.csv')
    
    # 3. Construir Dashboard
    print("\n--- Generando Dashboard ---")
    sns.set_theme(style="whitegrid")
    fig, axes = plt.subplots(2, 2, figsize=(16, 12))
    fig.suptitle('Dashboard Exploratorio: Desempeño Plantas AquaLimpia S.A.', fontsize=18)

    # Gráficos usando los nombres exactos de tus columnas
    sns.barplot(ax=axes[0, 0], data=df, x='planta', y='DBO_salida_mg_L', errorbar=None, palette='viridis')
    axes[0, 0].set_title('Promedio de DBO de Salida por Planta')

# Ajustamos el hue para que use los números 0 y 1 en lugar de texto
    sns.scatterplot(ax=axes[0, 1], data=df, x='caudal_entrada_m3_d', y='DBO_salida_mg_L', hue='cumplimiento_norma', palette={0: 'green', 1: 'red'})
    axes[0, 1].set_title('Impacto del Caudal en la DBO de Salida')
    

    sns.boxplot(ax=axes[1, 0], data=df, x='planta', y='energia_aeracion_kWh', palette='Set2')
    axes[1, 0].set_title('Distribución del Consumo de Energía')

# Ajustamos el hue para los números
    sns.countplot(ax=axes[1, 1], data=df, x='planta', hue='cumplimiento_norma', palette={0: 'green', 1: 'red'})
    axes[1, 1].set_title('Estado de Cumplimiento Normativo')
 

    plt.tight_layout()
    plt.savefig('outputs/dashboard_aqualimpia.png') 
    print("¡Dashboard guardado exitosamente en 'outputs/'!")

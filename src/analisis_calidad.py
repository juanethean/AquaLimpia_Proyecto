import pandas as pd
import numpy as np

# 1. Simulando la carga del dataset original
np.random.seed(42)
datos = {
    'Fecha': pd.date_range(start="2026-04-01", periods=100),
    'Planta': np.random.choice(['Planta Norte', 'Planta Centro', 'Planta Sur'], 100),
    'Caudal_m3': np.random.normal(4000, 500, 100),
    'DBO_Entrada': np.random.normal(250, 30, 100),
    'DBO_Salida': np.random.normal(30, 10, 100),
    'energia_aireacion_kWh': np.random.normal(1500, 200, 100)
}
df = pd.DataFrame(datos)

# 2. Corrompiendo los datos (Introduciendo NULOS y OUTLIERS)
# Generando valores nulos en DBO y Energía
df.loc[10:18, 'DBO_Salida'] = np.nan
df.loc[45:52, 'energia_aireacion_kWh'] = np.nan

# Generando valores atípicos absurdos (Outliers)
df.loc[5, 'energia_aireacion_kWh'] = 99999.0  # Consumo imposible
df.loc[80, 'DBO_Salida'] = -50.0              # DBO negativa (error de sensor)

# 3. Imprimiendo el análisis en consola (Lo que vas a capturar)
print("="*60)
print("  ANÁLISIS DE CALIDAD DE DATOS: AQUA LIMPIA S.A.  ")
print("="*60)
print("\n[INFO] Ejecutando df.info() para detectar registros nulos...\n")
df.info()

print("\n" + "-"*60)
print("\n[WARNING] Resumen estadístico: Detección de Valores Atípicos (Outliers)...\n")
print(df[['DBO_Salida', 'energia_aireacion_kWh']].describe())
print("\n" + "="*60)

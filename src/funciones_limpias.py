import pandas as pd

def cargar_datos(ruta):
    return pd.read_excel(ruta)

def generar_reporte_operaciones(df, ruta_salida):
    columnas = ['fecha_registro', 'planta', 'caudal_entrada_m3_d', 'DBO_entrada_mg_L', 'energia_aeracion_kWh', 'lodos_generados_kg_d']
    df[columnas].to_csv(ruta_salida, index=False)
    print(f"Reporte de operaciones guardado en {ruta_salida}")

def generar_reporte_ambiental(df, ruta_salida):
    columnas = ['fecha_registro', 'planta', 'DBO_salida_mg_L', 'cumplimiento_norma']
    df[columnas].to_csv(ruta_salida, index=False)
    print(f"Reporte ambiental guardado en {ruta_salida}")

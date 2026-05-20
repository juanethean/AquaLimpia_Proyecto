import pandas as pd

def cargar_datos(ruta):
    try:
        df = pd.read_excel(ruta)
        print("Datos cargados exitosamente.")
        return df
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo en la ruta {ruta}")
        return None

def generar_reporte_operaciones(df, ruta_salida):
    columnas = ['fecha_registro', 'planta', 'caudal_entrada', 'dbo_entrada', 
                'dbo_salida', 'consumo_energia', 'lodos_generados']
    df_operaciones = df[columnas]
    df_operaciones.to_csv(ruta_salida, index=False)
    print(f"Reporte de operaciones guardado en {ruta_salida}")

def generar_reporte_ambiental(df, ruta_salida, limite_dbo=30):
    df_ambiental = df.copy()
    df_ambiental['cumplimiento_normativo'] = df_ambiental['dbo_salida'].apply(
        lambda x: 'Cumple' if x <= limite_dbo else 'No Cumple'
    )
    columnas = ['fecha_registro', 'planta', 'dbo_salida', 'cumplimiento_normativo']
    df_final = df_ambiental[columnas]
    df_final.to_csv(ruta_salida, index=False)
    print(f"Reporte ambiental guardado en {ruta_salida}")

import pandas as pd

def Corregir_decimal(df):
    if "Duración parada" in df.columns:
        # Convierte la columna a cadena de texto
        df["Duración parada"] = df["Duración parada"].astype(str)
        df["Duración parada"] = df["Duración parada"].str.split(',', n=1).str[0]  # Queda con lo que está antes de la coma
        df["Duración parada"] = pd.to_numeric(df["Duración parada"], errors='coerce')  

    return df

def actualizar_class_aviso(df):
    if "Clase de aviso" in df.columns:
        df["Clase de aviso"] = df["Clase de aviso"].replace({
            "MC": "Correctivo",
            "MF": "Fabricacion",
            "MZ": "Correctivo",
            "MT": "Instalacion"
        })

    return df

def actualizar_grup_planif(df):
    if "Grupo planif." in df.columns:
        df["Grupo planif."] = df["Grupo planif."].replace({
            "P41": "Electromecanico",
            "P42": "Frigoristas",
            "P43": "Infraestructura",
            "P44": "Metrologia",
            "P91": "Electromecanico",
        })

    return df

# Leer todas las hojas
df = pd.read_csv(r"C:\Users\calza\Documents\Documentos_SAP\Dashboard_python\Dashboard_Mttopv\Data\IW28.csv", delimiter=",", encoding="utf-8", on_bad_lines='skip')
df = actualizar_class_aviso(df)
df = Corregir_decimal(df)
set_data_aviso = actualizar_grup_planif(df)
# cambios nuevos
# df.to_csv("Avisos.csv", index=False)
# ajuste de cambios nuevos
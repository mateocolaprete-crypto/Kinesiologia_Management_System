import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import os

def generar_grafico():
    #la ruta
    directorio_actual = os.path.dirname(os.path.abspath(__file__))
    ruta_db = os.path.join(directorio_actual, 'Kinesiologia_Demo.db')
    
    try:
        #cargamos datos
        conexion = sqlite3.connect(ruta_db)
        df = pd.read_sql_query("SELECT Date, Price_Session, Cost_Rent FROM Sessions", conexion)
        conexion.close()

        #procesamos datos
        df['Date'] = pd.to_datetime(df['Date'])
        df['Ganancia_Neta'] = df['Price_Session'] - df['Cost_Rent']

        #agrupamos por mes
        ganancias_mensuales = df.resample('ME', on='Date')['Ganancia_Neta'].sum()

        #creamos grafico
        plt.figure(figsize=(10, 6))
        ganancias_mensuales.plot(kind='bar', color='skyblue', edgecolor='navy')

        #personalizamos
        plt.title('Ganancias Netas Mensuales - Análisis de Negocio', fontsize=16)
        plt.xlabel('Mes', fontsize=12)
        plt.ylabel('Ganancia ($)', fontsize=12)
        plt.xticks(rotation=45)
        plt.grid(axis='y', linestyle='--', alpha=0.7)

        plt.tight_layout()
        print("📊 Generando gráfico de ganancias...")
        plt.show()

    except Exception as e:
        print(f"⚠️ Error al generar el gráfico: {e}")
        print("💡 Asegurate de haber corrido 'database_setup.py' primero.")

if __name__ == "__main__":
    generar_grafico()
import sqlite3
import pandas as pd
import os

def buscar_paciente():
    directorio_actual = os.path.dirname(os.path.abspath(__file__))
    ruta_db = os.path.join(directorio_actual, 'Kinesiologia_Demo.db')
    
    #conexión segura
    try:
        conexion = sqlite3.connect(ruta_db)
        
        #pedimos nombre
        nombre = input("🔍 Ingresá el nombre del paciente a buscar (o parte del nombre): ")
        
        #unimos tablas de sql
        query = f"""
        SELECT 
            p.FirstName AS Nombre, 
            p.LastName AS Apellido, 
            s.Date AS Fecha, 
            s.Price_Session AS Precio, 
            s.Methodology AS Tipo
        FROM Patients p
        JOIN Sessions s ON p.PatientID = s.PatientID
        WHERE p.FirstName LIKE '%{nombre}%' OR p.LastName LIKE '%{nombre}%'
        ORDER BY s.Date DESC
        """
        
        df = pd.read_sql_query(query, conexion)
        
        if df.empty:
            print(f"❌ No se encontraron sesiones para: {nombre}")
        else:
            print(f"\n✅ Historial encontrado:")
            print("-" * 60)
            #index=False para que no se vean los numeritos de la izquierda
            print(df.to_string(index=False))
            
            #estadísticas 
            total_sesiones = len(df)
            total_facturado = df['Precio'].sum()
            ultima_visita = df['Fecha'].max()
            
            print("-" * 60)
            print(f"📊 RESUMEN PARA: {nombre.upper()}")
            print(f"   - Sesiones totales: {total_sesiones}")
            print(f"   - Total facturado: ${total_facturado}")
            print(f"   - Última visita: {ultima_visita}")
            
    except Exception as e:
        print(f"⚠️ Error: {e}")
    finally:
        if 'conexion' in locals():
            conexion.close()

if __name__ == "__main__":
    buscar_paciente()
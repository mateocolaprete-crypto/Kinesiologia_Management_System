import sqlite3
import os

def inicializar_base_datos():
    #definimos la ruta donde se  va a crear la base de datos
    directorio_actual = os.path.dirname(os.path.abspath(__file__))
    ruta_db = os.path.join(directorio_actual, 'Kinesiologia_Demo.db')
    
    print(f"🛠️ Iniciando creación de base de datos en: {ruta_db}")
    
    #conexión y creación de tablas
    conexion = sqlite3.connect(ruta_db)
    cursor = conexion.cursor()

    #tabla de Pacientes
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Patients (
        PatientID INTEGER PRIMARY KEY AUTOINCREMENT,
        FirstName TEXT NOT NULL,
        LastName TEXT NOT NULL
    )""")

    #tabla de Sesiones
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Sessions (
        SessionsID INTEGER PRIMARY KEY AUTOINCREMENT,
        PatientID INTEGER,
        Date TEXT NOT NULL,
        Price_Session REAL,
        Cost_Rent REAL,
        Methodology TEXT,
        FOREIGN KEY(PatientID) REFERENCES Patients(PatientID)
    )""")

    #insertamos datos de prueba (Lionel y Angel para que el demo tenga algo)
    print("📝 Insertando datos de prueba (Modo Demo)...")
    
    pacientes_demo = [
        ('Lionel', 'Messi'),
        ('Angel', 'Di Maria')
    ]
    cursor.executemany("INSERT INTO Patients (FirstName, LastName) VALUES (?, ?)", pacientes_demo)

    #Sesiones de prueba:
    #Messi (hace más de 30 días para que salte la ALERTA)
    #Di María (reciente para que aparezca en el GRÁFICO y BUSCADOR)
    sesiones_demo = [
        (1, '2025-12-15', 50000, 5000, 'Consultorio'),
        (2, '2026-01-28', 50000, 5000, 'Domicilio')
    ]
    cursor.executemany("INSERT INTO Sessions (PatientID, Date, Price_Session, Cost_Rent, Methodology) VALUES (?, ?, ?, ?, ?)", sesiones_demo)

    conexion.commit()
    conexion.close()
    
    print("✅ ¡Éxito! Archivo 'Kinesiologia_Demo.db' creado correctamente.")
    print("🚀 Ahora podés ejecutar los scripts de Alerta, Buscador o Gráficos.")

if __name__ == "__main__":
    inicializar_base_datos()
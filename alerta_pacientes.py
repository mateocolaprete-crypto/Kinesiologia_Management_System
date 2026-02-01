import sqlite3
import os

def inicializar_demo():
    #ruta dinámica
    directorio = os.path.dirname(os.path.abspath(__file__))
    ruta_db = os.path.join(directorio, 'Kinesiologia_Demo.db')
    
    print(f"🛠️ Creando base de datos demo en: {ruta_db}")
    conexion = sqlite3.connect(ruta_db)
    cursor = conexion.cursor()

    #crear tablas
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Patients (
        PatientID INTEGER PRIMARY KEY AUTOINCREMENT,
        FirstName TEXT,
        LastName TEXT
    )""")

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

    #insertamos datos (datos creados para el publico)
    #Messi vino hace 40 días (debería saltar alerta)
    #Di María vino hace 10 días (no debería saltar)
    cursor.execute("INSERT INTO Patients (FirstName, LastName) VALUES ('Lionel', 'Messi')")
    cursor.execute("INSERT INTO Patients (FirstName, LastName) VALUES ('Angel', 'Di Maria')")
    
    cursor.execute("INSERT INTO Sessions (PatientID, Date, Price_Session, Cost_Rent, Methodology) VALUES (1, '2025-12-20', 50000, 5000, 'Consultorio')")
    cursor.execute("INSERT INTO Sessions (PatientID, Date, Price_Session, Cost_Rent, Methodology) VALUES (2, '2026-01-25', 50000, 5000, 'Consultorio')")

    conexion.commit()
    conexion.close()
    print("✅ Base de datos Demo lista con Lionel y Angel.")

if __name__ == "__main__":
    inicializar_demo()
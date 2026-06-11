import sqlite3


def conectar():
    return sqlite3.connect("prospectos.db")


def crear_tabla():
    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS prospectos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        telefono TEXT NOT NULL,
        correo TEXT,
        mensaje TEXT NOT NULL,
        fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    conexion.commit()
    conexion.close()


def guardar_prospecto(nombre, telefono, correo, mensaje):
    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("""
    INSERT INTO prospectos
    (nombre, telefono, correo, mensaje)
    VALUES (?, ?, ?, ?)
    """, (nombre, telefono, correo, mensaje))

    conexion.commit()
    conexion.close()


def obtener_prospectos():
    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("""
    SELECT *
    FROM prospectos
    ORDER BY id DESC
    """)

    prospectos = cursor.fetchall()

    conexion.close()

    return prospectos


def eliminar_prospecto(id):
    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute(
        "DELETE FROM prospectos WHERE id = ?",
        (id,)
    )

    conexion.commit()
    conexion.close()
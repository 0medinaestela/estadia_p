import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from models import (
    alumnos_col, proyectos_col, usuarios_col,
    colegios_col, comentarios_col
)

# Insertar alumno de prueba
alumnos_col.insert_one({
    "nombre": "Estela Gómez",
    "matricula": "A0001",
    "estado": "activo",
    "correo": "estela@example.com"
})

# Insertar proyecto de prueba
proyectos_col.insert_one({
    "titulo": "Sistema de seguimiento académico",
    "estado": "pendiente",
    "responsable": "Estela Gómez"
})

# Insertar usuario coordinador
usuarios_col.insert_one({
    "usuario": "admin",
    "rol": "coordinador",
    "activo": True,
    "correo": "admin@example.com"
})

# Insertar colegio de prueba
colegios_col.insert_one({
    "nombre": "Colegio Gómez Morin",
    "clave": "CGM001",
    "activo": True
})

# Insertar comentario de prueba
comentarios_col.insert_one({
    "autor": "admin",
    "mensaje": "Bienvenida al sistema",
    "fecha": "2025-10-16"
})

print("✅ Datos de prueba insertados correctamente.")
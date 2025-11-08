from pymongo import MongoClient
from config import MONGO_URI, DB_NAME

# Conexión a la base de datos
client = MongoClient(MONGO_URI)
db = client[DB_NAME]

# Colecciones
alumnos_col = db["alumnos"]
proyectos_col = db["proyectos"]
usuarios_col = db["usuarios"]
instituciones_col = db["instituciones"]
comentarios_col = db["comentarios"]
horarios_col = db["horarios"]
asistencia_col = db["asistencia"]
asistencia_new_col = db["asistencia_new"]
alumnos_password_col = db["alumnos_password"]
alumnos_servicio_col = db["alumnos_servicio"]
alumnos_servicio_new_col = db["alumnos_servicio_new"]
colegios_col = db["colegios"]
logs_col = db["logs"]  # ✅ Colección para registrar acciones del sistema
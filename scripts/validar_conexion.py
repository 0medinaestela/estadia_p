import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from models import db

try:
    colecciones = db.list_collection_names()
    print("✅ Conexión exitosa. Colecciones disponibles:")
    for col in colecciones:
        print(f" - {col}")
except Exception as e:
    print("❌ Error de conexión:", e)
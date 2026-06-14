from fintrack.database import get_connection

conn = get_connection()

print("Conectado!")

conn.close()
from app.db.database import get_db_connection

class ClienteModel:
    @staticmethod
    def crear(cliente):
        conn = get_db_connection()
        cursor = conn.cursor()
        query = "INSERT INTO clientes (nombre, telefono, email) VALUES (%s, %s, %s)"
        cursor.execute(query, (cliente.nombre, cliente.telefono, cliente.email))
        conn.commit()
        last_id = cursor.lastrowid
        conn.close()
        return last_id

    @staticmethod
    def listar_todos():
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM clientes")
        res = cursor.fetchall()
        conn.close()
        return res
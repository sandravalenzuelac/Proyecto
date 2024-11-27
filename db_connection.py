import mysql.connector  # Importa el módulo para conectarse a bases de datos MySQL.
from mysql.connector import Error  # Importa la clase Error para manejar excepciones específicas de MySQL.

def create_connection():
    try:
        # Establece la conexión con la base de datos utilizando los parámetros especificados.
        connection = mysql.connector.connect(
            host='localhost',      # Dirección del servidor de la base de datos.
            port='3308',           # Puerto en el que MySQL está escuchando (se usa 3308 en lugar del predeterminado 3306).
            user='root',           # Nombre de usuario para acceder a la base de datos.
            password='root',       # Contraseña del usuario.
            database='sistema_usuarios'  # Nombre de la base de datos a la que se desea conectar.
        )
        # Verifica si la conexión se ha establecido correctamente.
        if connection.is_connected():
            print("Conexión exitosa a la base de datos")  # Mensaje de éxito.
            return connection  # Devuelve el objeto de conexión para ser usado en otras operaciones.
    except Error as e:  # Captura cualquier error que ocurra durante la conexión.
        # Imprime un mensaje de error junto con el detalle de la excepción.
        print(f"Error al conectarse a la base de datos: {e}")
        return None  # Devuelve None si no se pudo establecer la conexión.

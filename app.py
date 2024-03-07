from flask import Flask, jsonify, request
from flask_mysqldb import MySQL
from flask_cors import CORS

app = Flask(__name__)

CORS(app)
# Especifica el origen permitido

# Configuración de la base de datos MySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'anyel'
app.config['MYSQL_DB'] = 'svelte'

mysql = MySQL(app)

# Nombres de los campos de la tabla productos
CAMPOS_PRODUCTOS = ["id_productos", "descripcion", "codigo", "categoria", "cantidad"]

# Ruta para verificar la conexión
@app.route('/verificar_conexion', methods=['GET'])
def verificar_conexion():
    try:
        # Conectar a la base de datos
        cur = mysql.connection.cursor()

        # Ejecutar una consulta simple para verificar la conexión
        cur.execute("SELECT 1")

        # Cerrar la conexión a la base de datos
        cur.close()

        return jsonify({"status": "Conexión exitosa"})
    
    except Exception as e:
        return jsonify({"error": str(e), "status": "Error de conexión"})

# Ruta para obtener todos los productos
@app.route('/productos', methods=['GET'])
def obtener_productos():
    try:
        # Conectar a la base de datos
        cur = mysql.connection.cursor()

        # Ejecutar la consulta SQL para obtener todos los productos
        cur.execute("SELECT * FROM productos")

        # Obtener todos los resultados
        productos = cur.fetchall()

        # Cerrar la conexión a la base de datos
        cur.close()

        # Convertir los resultados a un formato JSON con nombres de campo
        productos_con_nombres = [
            {campo: valor for campo, valor in zip(CAMPOS_PRODUCTOS, producto)}
            for producto in productos
        ]

        return jsonify(productos_con_nombres)
    
    except Exception as e:
        return jsonify({"error": str(e)})


# Ruta para crear un nuevo producto
@app.route('/productos', methods=['POST'])
def crear_producto():
    try:
        # Conectar a la base de datos
        cur = mysql.connection.cursor()

        # Obtener los datos del nuevo producto desde el cuerpo de la solicitud
        nuevo_producto = request.json
        # se instal con pip install request
        # Crear la consulta SQL para insertar el nuevo producto
        consulta = "INSERT INTO productos (descripcion, codigo, categoria, cantidad) VALUES (%s, %s, %s, %s)"
        datos = (nuevo_producto['descripcion'], nuevo_producto['codigo'], nuevo_producto['categoria'], nuevo_producto['cantidad'])

        # Ejecutar la consulta SQL
        cur.execute(consulta, datos)

        # Confirmar y cerrar la conexión a la base de datos
        mysql.connection.commit()
        cur.close()

        return jsonify({"status": "Producto creado exitosamente"})
    
    except Exception as e:
        return jsonify({"error": str(e)})



if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')

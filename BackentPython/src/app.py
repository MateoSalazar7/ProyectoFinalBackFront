from flask import Flask, jsonify, request
from flask_mysqldb import MySQL
from flask_cors import CORS, cross_origin

from config import config
from VALIDACIONES.validaciones import *
from CREATE.Regitros import *
app = Flask(__name__)

# CORS(app)
CORS(app, resources={r"/registro/*": {"origins": "http://localhost:4200"}})
CORS(app, resources={r"/login/*": {"origins": "http://localhost:4200"}})
conexion = MySQL(app)

#Metodos propios de mapi
@app.route('/categoria', methods=['GET'])
def leer_acudientes():
    try:
        curso=categorias()
        if curso != None:
            return jsonify({'curso': curso, 'mensaje': "Sin categorias.", 'exito': True})
        else:
            return jsonify({'mensaje': "Categorias no encontradas.", 'exito': False})
    except Exception as ex:
        return jsonify({'mensaje': "Error", 'exito': False})


def categorias():
    try:
        cursor = conexion.connection.cursor()
        sql = "SELECT * FROM acudiente"
        cursor.execute(sql)
        datos = cursor.fetchone()
        if datos != None:
            curso = {'cedula_acudiente': datos[0], 'nombre': datos[1], 'apellido': datos[2], 'telefono':datos[3],'telefono_2': datos[4], 'acudiente_alternativo':datos[5],'telefono_alternativo': datos[6], 'clave':datos[7]}
            return curso
        else:
            return None
    except Exception as ex:
        raise ex

# <----------------LOGIN---------------->
@app.route('/login', methods=['POST'])
def iniciar_sesion():
    # Tomo los datos que provienen del JSON
    # request.json
    # Obtengo el correo y la contrasena de la base de datos usando el correo que me entregan por el JSON
    correo = request.json['correo']
    clave = request.json['clave']
    cursor = conexion.connection.cursor()
    sql = "SELECT correo, clave FROM usuario WHERE correo='%s'" %correo
    cursor.execute(sql)
    resultado = cursor.fetchone()
    if resultado is not None:
        if (clave == resultado[0]):
            return jsonify({'usuario':"usuario", 'exito': True,'correo':resultado[1],'correo':correo}), 200
        else:
            return " Contraseña Incorrecta" 
    else:
        cursor = conexion.connection.cursor()
        sql = "SELECT correo,clave FROM usuario WHERE correo='%s'" %correo
        cursor.execute(sql)
        resultado = cursor.fetchone()
        if resultado is not None:
            if (clave == resultado[0]):
                return jsonify({'usuario':"usuario", 'exito': True,'correo':resultado[1],'correo':correo}), 200
            else:
                return " Contraseña Incorrecta" 
        return "Usuario no registrado"


# #CRUD usuario
@app.route('/registrousuario', methods=['POST'])
def registro_usuario():
        try:
            if registrar_usuario(request):
                return jsonify({'mensaje': "Usuario registrado.", 'exito': True}), 200
            else:
                return jsonify({'mensaje': "No se pudo realizar el registro", 'exito': False}), 400
        except Exception as ex:
            print(ex)
            return jsonify({'mensaje': "Servidor caido", 'exito': False}), 400


#CRUD categoria
@app.route('/registrocategoria', methods=['POST'])
def registrar_categoria():
        try:
            if registro_categoria(request):
                return jsonify({'mensaje': "Categoria registrado.", 'exito': True}), 200
            else:
                return jsonify({'mensaje': "No se pudo realizar el registro", 'exito': False}), 400
        except Exception as ex:
            print(ex)
            return jsonify({'mensaje': "Servidor caido", 'exito': False}), 400
       

#CRUD Producto
@app.route('/registroproducto', methods=['POST'])
def registrar_producto():
        try:
            if registro_producto(request):
                return jsonify({'mensaje': "Producto registrado.", 'exito': True}), 200
            else:
                return jsonify({'mensaje': "No se pudo realizar el registro", 'exito': False}), 400
        except Exception as ex:
            print(ex)
            return jsonify({'mensaje': "Servidor caido", 'exito': False}), 400

        
# #CRUD Usuario
# @app.route('/registrousuario', methods=['POST'])
# def registrar_usuario():
#         try:
#             if registro_usuario(request):
#                 return jsonify({'mensaje': "Usuario registrado.", 'exito': True}), 200
#             else:
#                 return jsonify({'mensaje': "No se pudo realizar el registro", 'exito': False}), 400
#         except Exception as ex:
#             print(ex)
#             return jsonify({'mensaje': "Servidor caido", 'exito': False}), 400

#CRUD Ingreso
@app.route('/registroingreso', methods=['POST'])
def registrar_Ingreso():
        try:
            if registro_ingreso(request):
                return jsonify({'mensaje': "Ingreso registrado.", 'exito': True}), 200
            else:
                return jsonify({'mensaje': "No se pudo realizar el registro", 'exito': False}), 400
        except Exception as ex:
            print(ex)
            return jsonify({'mensaje': "Servidor caido", 'exito': False}), 400

                
#CRUD Factura
@app.route('/registrofactura', methods=['POST'])
def registrar_Factura():

        try:
            if registro_factura(request):
                return jsonify({'mensaje': "Factura registrado.", 'exito': True}), 200
            else:
                return jsonify({'mensaje': "No se pudo realizar el registro", 'exito': False}), 400
        except Exception as ex:
            print(ex)
            return jsonify({'mensaje': "Servidor caido", 'exito': False}), 400

        
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 


# <----------------LEER Y ACTUALIZAR DATOS---------------->
# @cross_origin
@app.route('/actualizar', methods=['GET'])
def listar_datos():
    try:
        cursor = conexion.connection.cursor()
        sql = "SELECT Id_usuario, nombre_usuario, correo, clave FROM usuario ORDER BY nombre_usuario ASC"
        cursor.execute(sql)
        datos = cursor.fetchall()
        usuarios = []
        for fila in datos:
            usuario = {'Id_usuario': fila[0], 'nombre_usuario': fila[1], 'correo': fila[2], 'clave': fila[3]}
            usuarios.append(usuario)
        return jsonify({'usuarios': usuario, 'mensaje': "Usuarios listados.", 'exito': True})
    except Exception as ex:
        return jsonify({'mensaje': "Error", 'exito': False})


def leer_datos_bd(Id_usuario):
    try:
        cursor = conexion.connection.cursor()
        sql = "SELECT Id_usuario, nombre_usuario, correo, clave FROM usuario WHERE Id_usuario = '{0}'".format(Id_usuario)
        cursor.execute(sql)
        datos = cursor.fetchone()
        if datos != None:
            usuario = {'Id_usuario': datos[0], 'nombre_usuario': datos[1], 'correo': datos[2], 'clave': datos[3]}
            return usuario
        else:
            return None
    except Exception as ex:
        raise ex


@app.route('/actualizar/<Id_usuario>', methods=['GET'])
def leer_datos(Id_usuario):
    try:
        usuario = leer_datos_bd(Id_usuario)
        if usuario != None:
            return jsonify({'usuario': usuario, 'mensaje': "Usuario encontrado.", 'exito': True})
        else:
            return jsonify({'mensaje': "Usuario no encontrado.", 'exito': False})
    except Exception as ex:
        return jsonify({'mensaje': "Error", 'exito': False})

# ACTUALIZAR DATOS
@app.route('/actualizar/<Id_usuario>', methods=['PUT'])
def actualizar_datos(Id_usuario):
    if (validar_nombres(Id_usuario) and validar_correo(request.json['nombre_usuario']) and validar_clave(request.json['nombre_usuario'])):
        try:
            usuario = leer_datos_bd(Id_usuario)
            if usuario != None:
                cursor = conexion.connection.cursor()
                sql = """UPDATE usuario SET nombre_usuario = '{0}', clave = '{1}'
                WHERE Id_usuario = '{2}'""".format(request.json['nombre_usuario'], request.json['clave'], Id_usuario)
                cursor.execute(sql)
                conexion.connection.commit()  # Confirma la acción de actualización.
                return jsonify({'mensaje': "Usuario actualizado.", 'exito': True})
            else:
                return jsonify({'mensaje': "Usuario no encontrado.", 'exito': False})
        except Exception as ex:
            return jsonify({'mensaje': "Error", 'exito': False})
    else:
        return jsonify({'mensaje': "Parámetros inválidos...", 'exito': False})
    
    
    
    

#<----------------LEER ACTUALIZAR PRODUCTOS----------------> 
@app.route('/actualizarproductos', methods=['GET'])
def listar_producto():
    try:
        cursor = conexion.connection.cursor()
        sql = "SELECT id_Producto, nombre_producto FROM producto ORDER BY nombre_producto ASC"
        cursor.execute(sql)
        datos = cursor.fetchall()
        productos = []
        for fila in datos:
            producto = {'id_Producto': fila[0], 'nombre_producto': fila[1]}
            productos.append(producto)
        return jsonify({'usuarios': producto, 'mensaje': "Productos listados.", 'exito': True})
    except Exception as ex:
        return jsonify({'mensaje': "Error", 'exito': False})
    
def leer_producto_bd(id_Producto):
    try:
        cursor = conexion.connection.cursor()
        sql = "SELECT id_Producto, nombre_producto FROM producto WHERE id_Producto = '{0}'".format(id_Producto)
        cursor.execute(sql)
        datos = cursor.fetchone()
        if datos != None:
            producto = {'id_Producto': datos[0], 'nombre_producto': datos[1]}
            return producto
        else:
            return None
    except Exception as ex:
        raise ex
    
@app.route('/actualizarproductos/<id_Producto>', methods=['GET'])
def leer_producto(id_Producto):
    try:
        producto = leer_producto_bd(id_Producto)
        if producto != None:
            return jsonify({'usuario': producto, 'mensaje': "Producto encontrado.", 'exito': True})
        else:
            return jsonify({'mensaje': "Producto no encontrado.", 'exito': False})
    except Exception as ex:
        return jsonify({'mensaje': "Error", 'exito': False})

# ACTUALIZAR PRODUCTOS
@app.route('/actualizarproductos/<id_Producto>', methods=['PUT'])
def actualizar_producto(id_Producto):
    if (validar_producto(id_Producto)):
        try:
            producto = leer_producto_bd(id_Producto)
            if producto != None:
                cursor = conexion.connection.cursor()
                sql = """UPDATE producto SET nombre_producto = '{0}', descripcion = '{1}', valor_venta = '{2}', cantidad_stock = '{3}', Estado = '{4}'
                WHERE id_Producto = '{5}'""".format(request.json['nombre_producto'], request.json['descripcion'], request.json['valor_venta'], request.json['cantidad_stock'], request.json['Estado'],id_Producto)
                cursor.execute(sql)
                conexion.connection.commit()  # Confirma la acción de actualización.
                return jsonify({'mensaje': "Producto actualizado.", 'exito': True})
            else:
                return jsonify({'mensaje': "Producto no encontrado.", 'exito': False})
        except Exception as ex:
            return jsonify({'mensaje': "Error", 'exito': False})
    else:
        return jsonify({'mensaje': "Parámetros inválidos...", 'exito': False})




# <----------------LEER Y ACTUALIZAR CATEGORIA---------------->
# @cross_origin
@app.route('/actualizarcategoria', methods=['GET'])
def listar_categoria():
    try:
        cursor = conexion.connection.cursor()
        sql = "SELECT Id_Categoria, nombre_categoria FROM categoria ORDER BY nombre_categoria ASC"
        cursor.execute(sql)
        datos = cursor.fetchall()
        categorias = []
        for fila in datos:
            categoria = {'Id_Categoria': fila[0], 'nombre_categoria': fila[1]}
            categorias.append(categoria)
        return jsonify({'categoria': categoria, 'mensaje': "Categorias listadas.", 'exito': True})
    except Exception as ex:
        return jsonify({'mensaje': "Error", 'exito': False})


def leer_categoria_bd(Id_Categoria):
    try:
        cursor = conexion.connection.cursor()
        sql = "SELECT Id_Categoria, nombre_categoria FROM categoria WHERE Id_Categoria = '{0}'".format(Id_Categoria)
        cursor.execute(sql)
        datos = cursor.fetchone()
        if datos != None:
            categoria = {'Id_Categoria': datos[0], 'nombre_categoria': datos[1]}
            return categoria
        else:
            return None
    except Exception as ex:
        raise ex


@app.route('/actualizarcategoria/<Id_Categoria>', methods=['GET'])
def leer_categoria(Id_Categoria):
    try:
        categoria = leer_categoria_bd(Id_Categoria)
        if categoria != None:
            return jsonify({'categoria': categoria, 'mensaje': "Categoria encontrado.", 'exito': True})
        else:
            return jsonify({'mensaje': "Categoria no encontrado.", 'exito': False})
    except Exception as ex:
        return jsonify({'mensaje': "Error", 'exito': False})

# ACTUALIZAR CATEGORIA
@app.route('/actualizarcategoria/<Id_Categoria>', methods=['PUT'])
def actualizar_categoria(Id_Categoria):
    if (validar_categoria(Id_Categoria)):
        try:
            categoria = leer_categoria_bd(Id_Categoria)
            if categoria != None:
                cursor = conexion.connection.cursor()
                sql = """UPDATE categoria SET nombre_categoria = '{0}', Estado = '{1}'
                WHERE Id_Categoria = '{2}'""".format(request.json['nombre_categoria'],  request.json['Estado'], Id_Categoria)
                cursor.execute(sql)
                conexion.connection.commit()  # Confirma la acción de actualización.
                return jsonify({'mensaje': "Categoria actualizada.", 'exito': True})
            else:
                return jsonify({'mensaje': "Categoria no encontrada.", 'exito': False})
        except Exception as ex:
            return jsonify({'mensaje': "Error", 'exito': False})
    else:
        return jsonify({'mensaje': "Parámetros inválidos...", 'exito': False})
    



@app.route('/eliminar/<Id_usuario>', methods=['DELETE'])
def eliminar_curso(Id_usuario):
    try:
        usuario = leer_datos_bd(Id_usuario)
        if usuario != None:
            cursor = conexion.connection.cursor()
            sql = "DELETE FROM usuario WHERE Id_usuario = '{0}'".format(Id_usuario)
            cursor.execute(sql)
            conexion.connection.commit()  # Confirma la acción de eliminación.
            return jsonify({'mensaje': "Usuario eliminado.", 'exito': True})
        else:
            return jsonify({'mensaje': "Usuario no encontrado.", 'exito': False})
    except Exception as ex:
        return jsonify({'mensaje': "Error", 'exito': False})


def pagina_no_encontrada(error):
    return "<h1>Página no encontrada</h1>", 404


if __name__ == '__main__':
    app.config.from_object(config['development'])
    app.register_error_handler(404, pagina_no_encontrada)
    app.run()

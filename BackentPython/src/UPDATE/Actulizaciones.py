from datetime import date
from datetime import datetime


def actualizar_datos(request):
    try :
        #Llamado a la base de datos, para no duplicidad
        from CONEXION.Conexion import conectar
        conexion=conectar()
        cursor = conexion.connection.cursor()
        sql = "CALL usuario('{0}', '{1}', '{2}', '{3}', '{4}')".format(request.json['Id_usuario'],request.json['nombre_usuario'],request.json['clave'],request.json['rol'])
        print("Id_usuario sql", sql)
        cursor.execute(sql)
        conexion.connection.commit()
        return True
    except Exception as ex:
        return False
    
def actualizar_producto(request):
    try :
        #Llamado a la base de datos, para no duplicidad
        from CONEXION.Conexion import conectar
        conexion=conectar()
        cursor = conexion.connection.cursor()
        sql = "CALL producto('{0}', {1}, {2}, {3}, {4}, {5})".format(request.json['id_Producto'],request.json['nombre_producto'],request.json['descripcion'],request.json['valor_venta'],request.json['cantidad_stock'],request.json['Estado'])
        print("id_Producto sql", sql)
        cursor.execute(sql)
        conexion.connection.commit()
        return True
    except Exception as ex:
        return False
    
    
def actualizar_categoria(request):
    try :
        #Llamado a la base de datos, para no duplicidad
        from CONEXION.Conexion import conectar
        conexion=conectar()
        cursor = conexion.connection.cursor()
        sql = "CALL categoria('{0}', '{1}', '{2}')".format(request.json['Id_Categoria'],request.json['nombre_categoria'],request.json['Estado'])
        print("Id_Categoria sql", sql)
        cursor.execute(sql)
        conexion.connection.commit()
        return True
    except Exception as ex:
        return False
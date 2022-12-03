from datetime import date
from datetime import datetime


def registrar_usuario(request):
    try :
        #Llamado a la base de datos, para no duplicidad
        from CONEXION.Conexion import conectar
        conexion=conectar()
        cursor = conexion.connection.cursor()
        sql = "CALL registro('{0}', '{1}', '{2}')".format(request.json['correo'],request.json['nombre_usuario'],request.json['clave'])
        print("codigo sql", sql)
        cursor.execute(sql)
        conexion.connection.commit()
        return True
    except Exception as ex:
        return False

def registro_categoria(request):
    try :
        #Llamado a la base de datos, para no duplicidad
        from CONEXION.Conexion import conectar
        conexion=conectar()
        cursor = conexion.connection.cursor()
        sql = """CALL Registrar_Categoria('{0}')""".format(request.json['nombre_categoria'])
        print("codigo sql", sql)
        cursor.execute(sql)
        conexion.connection.commit()
        return True
    except Exception as ex:
        return False


def registro_producto(request):
    try :
        from CONEXION.Conexion import conectar
        conexion=conectar()
        cursor = conexion.connection.cursor()
        sql = """CALL Registrar_Producto('{0}', '{1}', '{2}', '{3}', '{4}', '{5}')""".format(request.json['nombre_producto'],request.json['descripcion'],request.json['valor_venta'],request.json['cantidad_stock'],request.json['Id_Usuario'],request.json['Id_Categoria'])
        print("codigo sql", sql)
        # Ejecutar la sentencia SQL
        cursor.execute(sql)
        # Aceptar la sentencia SQL
        conexion.connection.commit()
        return True
    except Exception as ex:
        return False

def registro_usuario(request):
    try :
        from CONEXION.Conexion import conectar
        conexion=conectar()
        cursor = conexion.connection.cursor()
        sql = """CALL Registrar_Usuario('{0}', '{1}', '{2}', '{3}')""".format(request.json['nombre_usuario'],request.json['correo'],request.json['clave'],request.json['rol'])
        print("codigo sql", sql)
        # Ejecutar la sentencia SQL
        cursor.execute(sql)
        # Aceptar la sentencia SQL
        conexion.connection.commit()
        return True
    except Exception as ex:
        return False

def registro_ingreso(request):
    try :
        from CONEXION.Conexion import conectar
        conexion=conectar()
        cursor = conexion.connection.cursor()
        sql = """CALL Registrar_Ingreso('{0}', '{1}', '{2}', '{3}')""".format(request.json['cantidad_ingresos'],request.json['fecha'],request.json['valor_compra'],request.json['Id_Producto'])
        print("codigo sql", sql)
        # Ejecutar la sentencia SQL
        cursor.execute(sql)
        # Aceptar la sentencia SQL
        conexion.connection.commit()
        return True
    except Exception as ex:
        return False


def registro_factura(request):
    try :
        from CONEXION.Conexion import conectar
        conexion=conectar()
        cursor = conexion.connection.cursor()
        sql = """CALL Registrar_Factura('{0}', '{1}', '{2}', '{3}', '{4}')""".format(request.json['fecha'],request.json['valor_factura'],request.json['iva'],request.json['valor_neto'],request.json['Id_Usuario'])
        print("codigo sql", sql)
        # Ejecutar la sentencia SQL
        cursor.execute(sql)
        # Aceptar la sentencia SQL
        conexion.connection.commit()
        return True
    except Exception as ex:
        return False        




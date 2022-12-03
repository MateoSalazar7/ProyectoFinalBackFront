
#Validar que el campo este lleno

    

# Valida el código (si es numérico y de longitud 6).
def validar_nombres(nombres: str) -> bool:
    return (len(nombres) > 0 and len(nombres) <= 30)

# Valida el nombre (si es un texto sin espacios en blanco de entre 1 y 30 caracteres).
def validar_apellidos(apellidos: str) -> bool:
    apellidos = apellidos.strip()
    return (len(apellidos) > 0 and len(apellidos) <= 30)

# Valida que los créditos estén entre 1 y 9.
def validar_correo(correo: str) -> bool:
    correo = correo.strip()
    return (len(correo) > 0 and len(correo) <= 30)

#Validar clave usuario
def validar_clave(clave: str) -> bool:
    clave = clave.strip()
    return (len(clave) > 0 and len(clave) <= 30)

#Validar producto
def validar_producto(nombre_producto: str) -> bool:
    nombre_producto = nombre_producto.strip()
    return (len(nombre_producto) > 0 and len(nombre_producto) <= 30)

#Validar categoria
def validar_categoria(nombre_categoria: str) -> bool:
    nombre_categoria = nombre_categoria.strip()
    return (len(nombre_categoria) > 0 and len(nombre_categoria) <= 30)
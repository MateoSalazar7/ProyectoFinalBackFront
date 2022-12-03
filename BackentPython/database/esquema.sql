CREATE TABLE Categoria(
    Id_Categoria int(30) AUTO_INCREMENT NOT null PRIMARY KEY,
    nombre_categoria varchar(250) NOT null
);

CREATE TABLE Usuario(
    Id_Usuario int(30) AUTO_INCREMENT NOT null PRIMARY KEY,
    nombre_usuario varchar(250),
    correo varchar(250),
    clave varchar(250),
    rol int(30)
);

CREATE TABLE Producto(
    id_Producto int(30) AUTO_INCREMENT NOT null PRIMARY KEY,
    nombre_producto varchar(250),
    descripcion varchar(250),
    valor_venta int(30),
    cantidad_stock int(30),
    Id_Usuario int(30),
    Id_Categoria int(30),
    FOREIGN KEY (Id_Usuario) REFERENCES Usuario(Id_Usuario),
    FOREIGN KEY (Id_Categoria) REFERENCES Categoria(Id_categoria) 
);

CREATE TABLE Factura(
    Id_Factura int(30) AUTO_INCREMENT NOT null PRIMARY KEY,
    fecha date,
    valor_factura int(30),
    iva int(30),
    valor_neto int(30),
    Id_Usuario int (30),
    FOREIGN KEY (Id_Usuario) REFERENCES Usuario (Id_Usuario)
);


CREATE TABLE Detalles_F(
Id_Detalle int(30) AUTO_INCREMENT NOT null PRIMARY KEY,
    cantidad int(30),
    subtotal int(30),
    Id_Producto int(30),
    Id_Factura int(30),
    FOREIGN KEY (Id_Producto) REFERENCES Producto (Id_Producto),
    FOREIGN KEY (Id_Factura) REFERENCES Factura (Id_Factura)
);

CREATE TABLE Ingresos(

Id_Ingreso int(30) AUTO_INCREMENT NOT null PRIMARY KEY,
    cantidad_ingresos int(30),
    fecha date,
    valor_compra int(30),
    Id_Producto int(30),
    FOREIGN KEY (Id_Producto) REFERENCES Producto (Id_Producto)   
);

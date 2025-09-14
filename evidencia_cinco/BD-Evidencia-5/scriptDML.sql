USE SmartHomeDB;
GO

-- USUARIOS (3)
INSERT INTO USUARIO (correo,nombres,apellidos,contrasena,es_activo) VALUES (N'nahuel@gmail.com',N'Nahuel',N'Mclay',N'1234',1);
INSERT INTO USUARIO (correo,nombres,apellidos,contrasena,es_activo) VALUES (N'mariano@gmail.com',N'Mariano',N'Batista',N'abcd',1);
INSERT INTO USUARIO (correo,nombres,apellidos,contrasena,es_activo) VALUES (N'cristian@gmail.com',N'Cristian',N'Murua',N'pass',0);
GO

-- VIVIENDAS (2)
INSERT INTO VIVIENDA (direccion,codigo_postal) VALUES (N'Calle 123',N'5000');
INSERT INTO VIVIENDA (direccion,codigo_postal) VALUES (N'Av. Siempreviva 742',N'5010');
GO

-- TIPOS DE DISPOSITIVO (3)
INSERT INTO TIPO_DISPOSITIVO (nombre) VALUES (N'iluminación');
INSERT INTO TIPO_DISPOSITIVO (nombre) VALUES (N'aspiradora');
INSERT INTO TIPO_DISPOSITIVO (nombre) VALUES (N'aire acondicionado');
GO

-- UBICACIONES (4)  -- (dependen de VIVIENDA)
INSERT INTO UBICACION (nombre,id_vivienda) VALUES (N'Cocina',1);
INSERT INTO UBICACION (nombre,id_vivienda) VALUES (N'Patio',1);
INSERT INTO UBICACION (nombre,id_vivienda) VALUES (N'Comedor',1);
INSERT INTO UBICACION (nombre,id_vivienda) VALUES (N'Dormitorio',2);
GO

-- USUARIO_VIVIENDA (3)  -- FK a USUARIO y VIVIENDA
INSERT INTO USUARIO_VIVIENDA (correo,id_vivienda,rol) VALUES (N'nahuel@gmail.com',1,N'Admin');
INSERT INTO USUARIO_VIVIENDA (correo,id_vivienda,rol) VALUES (N'mariano@gmail.com',1,N'Estandar');
INSERT INTO USUARIO_VIVIENDA (correo,id_vivienda,rol) VALUES (N'cristian@gmail.com',2,N'Admin');
GO

-- DISPOSITIVOS (3)  -- dependen de TIPO_DISPOSITIVO y UBICACION
INSERT INTO DISPOSITIVO (nombre,estado,fecha_hora,id_tipo,id_ubicacion) VALUES (N'Luz Patio',0,GETDATE(),1,2);
INSERT INTO DISPOSITIVO (nombre,estado,fecha_hora,id_tipo,id_ubicacion) VALUES (N'Aspiradora Comedor',0,GETDATE(),2,3);
INSERT INTO DISPOSITIVO (nombre,estado,fecha_hora,id_tipo,id_ubicacion) VALUES (N'Aire Dormitorio',1,GETDATE(),3,4);
GO

-- ACCIONES (6)
INSERT INTO ACCION (nombre,id_tipo) VALUES (N'Encender',1);
INSERT INTO ACCION (nombre,id_tipo) VALUES (N'Apagar',1);
INSERT INTO ACCION (nombre,id_tipo) VALUES (N'Activar',2);
INSERT INTO ACCION (nombre,id_tipo) VALUES (N'Desactivar',2);
INSERT INTO ACCION (nombre,id_tipo) VALUES (N'Subir Temp',3);
INSERT INTO ACCION (nombre,id_tipo) VALUES (N'Bajar Temp',3);
GO

-- CONFIGURACIONES (3)
INSERT INTO CONFIGURACION_DISPOSITIVO (id_dispositivo,atributo,valor) VALUES (1,N'intensidad',N'80');
INSERT INTO CONFIGURACION_DISPOSITIVO (id_dispositivo,atributo,valor) VALUES (2,N'modo',N'auto');
INSERT INTO CONFIGURACION_DISPOSITIVO (id_dispositivo,atributo,valor) VALUES (3,N'temperatura',N'24');
GO

-- AUTOMATIZACIONES (2)
INSERT INTO AUTOMATIZACIONES (nombre,id_vivienda,hora_inicio,hora_fin,activa) VALUES (N'Activar luces del Patio',1,'19:00:00','23:59:59',1);
INSERT INTO AUTOMATIZACIONES (nombre,id_vivienda,hora_inicio,hora_fin,activa) VALUES (N'activador/desactivador aspiradora',1,'09:00:00','11:00:00',1);
GO

-- AUTOMATIZACION_OBJETIVO (2)
INSERT INTO AUTOMATIZACION_OBJETIVO (id_automatizacion,id_tipo,id_ubicacion) VALUES (1,1,2); -- luces del patio
INSERT INTO AUTOMATIZACION_OBJETIVO (id_automatizacion,id_tipo,id_ubicacion) VALUES (2,2,3); -- aspiradora comedor
GO

-- Consultas 
SELECT * FROM USUARIO;
SELECT * FROM VIVIENDA;
SELECT * FROM USUARIO_VIVIENDA;
SELECT * FROM TIPO_DISPOSITIVO;
SELECT * FROM UBICACION;
SELECT * FROM DISPOSITIVO;
SELECT * FROM ACCION;
SELECT * FROM CONFIGURACION_DISPOSITIVO;
SELECT * FROM AUTOMATIZACIONES;
SELECT * FROM AUTOMATIZACION_OBJETIVO;
GO
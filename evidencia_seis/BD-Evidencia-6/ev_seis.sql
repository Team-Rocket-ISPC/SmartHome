# Mas inserts

USE SmartHomeDB;

-- USUARIOS (13)
INSERT INTO USUARIO (correo,nombres,apellidos,contrasena,es_activo) VALUES ('nahuel@gmail.com','Nahuel','Mclay','1234',1);
INSERT INTO USUARIO (correo,nombres,apellidos,contrasena,es_activo) VALUES ('mariano@gmail.com','Mariano','Batista','abcd',1);
INSERT INTO USUARIO (correo,nombres,apellidos,contrasena,es_activo) VALUES ('cristian@gmail.com','Cristian','Murua','pass',1);
INSERT INTO USUARIO (correo,nombres,apellidos,contrasena,es_activo) VALUES ('diego@gmail.com','Diego','Grenon','diepass',1);
INSERT INTO USUARIO (correo,nombres,apellidos,contrasena,es_activo) VALUES ('franco@gmail.com','Franco','Valdez','franpass',1);
INSERT INTO USUARIO (correo,nombres,apellidos,contrasena,es_activo) VALUES ('silvia@gmail.com','Silvia','Ayosa','silviapass',1);
INSERT INTO USUARIO (correo,nombres,apellidos,contrasena,es_activo) VALUES ('eugenio@gmail.com','Eugenio','Perez','eugepass',1);
INSERT INTO USUARIO (correo,nombres,apellidos,contrasena,es_activo) VALUES ('carlos@gmail.com','Carlos','Bellaco','carpass',1);
INSERT INTO USUARIO (correo,nombres,apellidos,contrasena,es_activo) VALUES ('lucia@gmail.com','Lucia','Gomez','lupass',1);
INSERT INTO USUARIO (correo,nombres,apellidos,contrasena,es_activo) VALUES ('pedro@gmail.com','Pedro','Sanchez','pepass',1);
INSERT INTO USUARIO (correo,nombres,apellidos,contrasena,es_activo) VALUES ('ana@gmail.com','Ana','Torres','anpass',1);
INSERT INTO USUARIO (correo,nombres,apellidos,contrasena,es_activo) VALUES ('juan@gmail.com','Juan','Cruz','jupass',1);
INSERT INTO USUARIO (correo,nombres,apellidos,contrasena,es_activo) VALUES ('maria@gmail.com','Maria','Lopez','mapass',1);

-- VIVIENDAS (12)
INSERT INTO VIVIENDA (direccion,codigo_postal) VALUES ('Calle 123','5000');
INSERT INTO VIVIENDA (direccion,codigo_postal) VALUES ('Av. Siempreviva 742','5010');
INSERT INTO VIVIENDA (direccion,codigo_postal) VALUES ('Av. Rivadavia 2350','1425');
INSERT INTO VIVIENDA (direccion,codigo_postal) VALUES ('Calle Florida 768','1005');
INSERT INTO VIVIENDA (direccion,codigo_postal) VALUES ('Av. Corrientes 3487','1193');
INSERT INTO VIVIENDA (direccion,codigo_postal) VALUES ('Calle Sarmiento 542','5500');
INSERT INTO VIVIENDA (direccion,codigo_postal) VALUES ('Av. San Martín 1245','5600');
INSERT INTO VIVIENDA (direccion,codigo_postal) VALUES ('Calle 9 de Julio 302','3000');
INSERT INTO VIVIENDA (direccion,codigo_postal) VALUES ('Av. Belgrano 875','4000');
INSERT INTO VIVIENDA (direccion,codigo_postal) VALUES ('Calle Urquiza 1567','3100');
INSERT INTO VIVIENDA (direccion,codigo_postal) VALUES ('Av. Colón 2033','5000');
INSERT INTO VIVIENDA (direccion,codigo_postal) VALUES ('Calle Mitre 987','7600');

-- USUARIO_VIVIENDA (3)  -- FK a USUARIO y VIVIENDA FALTAN DATOS
INSERT INTO USUARIO_VIVIENDA (correo,id_vivienda,rol) VALUES ('nahuel@gmail.com',1,'Admin');
INSERT INTO USUARIO_VIVIENDA (correo,id_vivienda,rol) VALUES ('mariano@gmail.com',1,'Estandar');
INSERT INTO USUARIO_VIVIENDA (correo,id_vivienda,rol) VALUES ('carlos@gmail.com',1,'Estandar');
INSERT INTO USUARIO_VIVIENDA (correo,id_vivienda,rol) VALUES ('eugenio@gmail.com',1,'Estandar');
INSERT INTO USUARIO_VIVIENDA (correo,id_vivienda,rol) VALUES ('lucia@gmail.com',1,'Estandar');
INSERT INTO USUARIO_VIVIENDA (correo,id_vivienda,rol) VALUES ('pedro@gmail.com',1,'Estandar');
INSERT INTO USUARIO_VIVIENDA (correo,id_vivienda,rol) VALUES ('cristian@gmail.com',2,'Admin');
INSERT INTO USUARIO_VIVIENDA (correo,id_vivienda,rol) VALUES ('diego@gmail.com',2,'Estandar');
INSERT INTO USUARIO_VIVIENDA (correo,id_vivienda,rol) VALUES ('mariano@gmail.com',2,'Estandar');
INSERT INTO USUARIO_VIVIENDA (correo,id_vivienda,rol) VALUES ('carlos@gmail.com',2,'Estandar');
INSERT INTO USUARIO_VIVIENDA (correo,id_vivienda,rol) VALUES ('eugenio@gmail.com',2,'Estandar');
INSERT INTO USUARIO_VIVIENDA (correo,id_vivienda,rol) VALUES ('lucia@gmail.com',2,'Estandar');
INSERT INTO USUARIO_VIVIENDA (correo,id_vivienda,rol) VALUES ('pedro@gmail.com',2,'Estandar');



-- TIPOS DE DISPOSITIVO (10)
INSERT INTO TIPO_DISPOSITIVO (nombre) VALUES ('Iluminacion');
INSERT INTO TIPO_DISPOSITIVO (nombre) VALUES ('Electrodomestico');
INSERT INTO TIPO_DISPOSITIVO (nombre) VALUES ('Climatizacion');
INSERT INTO TIPO_DISPOSITIVO (nombre) VALUES ('Seguridad');
INSERT INTO TIPO_DISPOSITIVO (nombre) VALUES ('Control de acceso');
INSERT INTO TIPO_DISPOSITIVO (nombre) VALUES ('Multimedia');
INSERT INTO TIPO_DISPOSITIVO (nombre) VALUES ('Riego');
INSERT INTO TIPO_DISPOSITIVO (nombre) VALUES ('Energia');
INSERT INTO TIPO_DISPOSITIVO (nombre) VALUES ('Persianas');
INSERT INTO TIPO_DISPOSITIVO (nombre) VALUES ('Asistente de voz');


-- UBICACIONES (12)  -- (dependen de VIVIENDA, solo para la 1 en este caso)
INSERT INTO UBICACION (nombre, id_vivienda) VALUES ('Cocina', 1);
INSERT INTO UBICACION (nombre, id_vivienda) VALUES ('Patio', 1);
INSERT INTO UBICACION (nombre, id_vivienda) VALUES ('Comedor', 1);
INSERT INTO UBICACION (nombre, id_vivienda) VALUES ('Dormitorio', 1);
INSERT INTO UBICACION (nombre, id_vivienda) VALUES ('Baño', 1);
INSERT INTO UBICACION (nombre, id_vivienda) VALUES ('Living', 1);
INSERT INTO UBICACION (nombre, id_vivienda) VALUES ('Lavadero', 1);
INSERT INTO UBICACION (nombre, id_vivienda) VALUES ('Garage', 1);
INSERT INTO UBICACION (nombre, id_vivienda) VALUES ('Jardín', 1);
INSERT INTO UBICACION (nombre, id_vivienda) VALUES ('Pasillo', 1);
INSERT INTO UBICACION (nombre, id_vivienda) VALUES ('Oficina', 1);
INSERT INTO UBICACION (nombre, id_vivienda) VALUES ('Antebaño', 1);
INSERT INTO UBICACION (nombre, id_vivienda) VALUES ('Porche', 1);


-- ILUMINACIÓN (id_tipo = 1)
INSERT INTO DISPOSITIVO (nombre,estado,fecha_hora,id_tipo,id_ubicacion) VALUES ('Luz Patio',0,now(),1,2);
INSERT INTO DISPOSITIVO (nombre,estado,fecha_hora,id_tipo,id_ubicacion) VALUES ('Luz Comedor',0,now(),1,3);
INSERT INTO DISPOSITIVO (nombre,estado,fecha_hora,id_tipo,id_ubicacion) VALUES ('Luz Dormitorio',1,now(),1,4);
INSERT INTO DISPOSITIVO (nombre,estado,fecha_hora,id_tipo,id_ubicacion) VALUES ('Luz Cocina',1,now(),1,1);
INSERT INTO DISPOSITIVO (nombre,estado,fecha_hora,id_tipo,id_ubicacion) VALUES ('Luz Baño',0,now(),1,5);
INSERT INTO DISPOSITIVO (nombre,estado,fecha_hora,id_tipo,id_ubicacion) VALUES ('Luz Living',0,now(),1,6);
INSERT INTO DISPOSITIVO (nombre,estado,fecha_hora,id_tipo,id_ubicacion) VALUES ('Luz Garage',0,now(),1,7);
INSERT INTO DISPOSITIVO (nombre,estado,fecha_hora,id_tipo,id_ubicacion) VALUES ('Luz Jardín',0,now(),1,8);
INSERT INTO DISPOSITIVO (nombre,estado,fecha_hora,id_tipo,id_ubicacion) VALUES ('Tira LED Pasillo',1,now(),1,9);
INSERT INTO DISPOSITIVO (nombre,estado,fecha_hora,id_tipo,id_ubicacion) VALUES ('Lámpara Escritorio',1,now(),1,10);

-- ELECTRODOMÉSTICO (id_tipo = 2)
INSERT INTO DISPOSITIVO (nombre,estado,fecha_hora,id_tipo,id_ubicacion) VALUES ('Aspiradora Comedor',0,now(),2,3);
INSERT INTO DISPOSITIVO (nombre,estado,fecha_hora,id_tipo,id_ubicacion) VALUES ('Heladera',1,now(),2,1);
INSERT INTO DISPOSITIVO (nombre,estado,fecha_hora,id_tipo,id_ubicacion) VALUES ('Microondas',0,now(),2,1);
INSERT INTO DISPOSITIVO (nombre,estado,fecha_hora,id_tipo,id_ubicacion) VALUES ('Cafetera',0,now(),2,1);
INSERT INTO DISPOSITIVO (nombre,estado,fecha_hora,id_tipo,id_ubicacion) VALUES ('Licuadora',0,now(),2,1);
INSERT INTO DISPOSITIVO (nombre,estado,fecha_hora,id_tipo,id_ubicacion) VALUES ('Horno',1,now(),2,1);
INSERT INTO DISPOSITIVO (nombre,estado,fecha_hora,id_tipo,id_ubicacion) VALUES ('Lavarropas',0,now(),2,5);
INSERT INTO DISPOSITIVO (nombre,estado,fecha_hora,id_tipo,id_ubicacion) VALUES ('Secarropas',0,now(),2,5);
INSERT INTO DISPOSITIVO (nombre,estado,fecha_hora,id_tipo,id_ubicacion) VALUES ('Lavavajillas',0,now(),2,1);
INSERT INTO DISPOSITIVO (nombre,estado,fecha_hora,id_tipo,id_ubicacion) VALUES ('Extractor Cocina',1,now(),2,1);

-- CLIMATIZACIÓN (id_tipo = 3)
INSERT INTO DISPOSITIVO (nombre,estado,fecha_hora,id_tipo,id_ubicacion) VALUES ('Aire Dormitorio',1,now(),3,4);
INSERT INTO DISPOSITIVO (nombre,estado,fecha_hora,id_tipo,id_ubicacion) VALUES ('Aire Living',0,now(),3,6);
INSERT INTO DISPOSITIVO (nombre,estado,fecha_hora,id_tipo,id_ubicacion) VALUES ('Ventilador Techo Comedor',1,now(),3,3);
INSERT INTO DISPOSITIVO (nombre,estado,fecha_hora,id_tipo,id_ubicacion) VALUES ('Calefactor Baño',0,now(),3,5);
INSERT INTO DISPOSITIVO (nombre,estado,fecha_hora,id_tipo,id_ubicacion) VALUES ('Radiador Oficina',0,now(),3,10);
INSERT INTO DISPOSITIVO (nombre,estado,fecha_hora,id_tipo,id_ubicacion) VALUES ('Termostato Central',1,now(),3,6);
INSERT INTO DISPOSITIVO (nombre,estado,fecha_hora,id_tipo,id_ubicacion) VALUES ('Deshumidificador Dormitorio',0,now(),3,4);
INSERT INTO DISPOSITIVO (nombre,estado,fecha_hora,id_tipo,id_ubicacion) VALUES ('Caldera',1,now(),3,7);
INSERT INTO DISPOSITIVO (nombre,estado,fecha_hora,id_tipo,id_ubicacion) VALUES ('Humidificador Cocina',0,now(),3,1);
INSERT INTO DISPOSITIVO (nombre,estado,fecha_hora,id_tipo,id_ubicacion) VALUES ('Ventilador Pie Living',0,now(),3,6);

-- SEGURIDAD (id_tipo = 4)
INSERT INTO DISPOSITIVO (nombre,estado,fecha_hora,id_tipo,id_ubicacion) VALUES ('Cámara Patio',1,now(),4,2);
INSERT INTO DISPOSITIVO (nombre,estado,fecha_hora,id_tipo,id_ubicacion) VALUES ('Cámara Garage',0,now(),4,7);
INSERT INTO DISPOSITIVO (nombre,estado,fecha_hora,id_tipo,id_ubicacion) VALUES ('Sensor Puerta Principal',1,now(),4,9);
INSERT INTO DISPOSITIVO (nombre,estado,fecha_hora,id_tipo,id_ubicacion) VALUES ('Sensor Movimiento Living',0,now(),4,6);
INSERT INTO DISPOSITIVO (nombre,estado,fecha_hora,id_tipo,id_ubicacion) VALUES ('Alarma General',1,now(),4,6);
INSERT INTO DISPOSITIVO (nombre,estado,fecha_hora,id_tipo,id_ubicacion) VALUES ('Cámara Jardín',0,now(),4,8);
INSERT INTO DISPOSITIVO (nombre,estado,fecha_hora,id_tipo,id_ubicacion) VALUES ('Detector Humo Cocina',0,now(),4,1);
INSERT INTO DISPOSITIVO (nombre,estado,fecha_hora,id_tipo,id_ubicacion) VALUES ('Detector Gas',0,now(),4,1);
INSERT INTO DISPOSITIVO (nombre,estado,fecha_hora,id_tipo,id_ubicacion) VALUES ('Cámara Dormitorio',0,now(),4,4);
INSERT INTO DISPOSITIVO (nombre,estado,fecha_hora,id_tipo,id_ubicacion) VALUES ('Sirena Exterior',0,now(),4,2);

-- CONTROL DE ACCESO (id_tipo = 5)
INSERT INTO DISPOSITIVO (nombre,estado,fecha_hora,id_tipo,id_ubicacion) VALUES ('Cerradura Principal',1,now(),5,9);
INSERT INTO DISPOSITIVO (nombre,estado,fecha_hora,id_tipo,id_ubicacion) VALUES ('Cerradura Garage',0,now(),5,7);
INSERT INTO DISPOSITIVO (nombre,estado,fecha_hora,id_tipo,id_ubicacion) VALUES ('Video Portero',1,now(),5,9);
INSERT INTO DISPOSITIVO (nombre,estado,fecha_hora,id_tipo,id_ubicacion) VALUES ('Teclado Acceso Oficina',0,now(),5,10);
INSERT INTO DISPOSITIVO (nombre,estado,fecha_hora,id_tipo,id_ubicacion) VALUES ('Sensor Huella Dormitorio',0,now(),5,4);
INSERT INTO DISPOSITIVO (nombre,estado,fecha_hora,id_tipo,id_ubicacion) VALUES ('Lector RFID Patio',0,now(),5,2);
INSERT INTO DISPOSITIVO (nombre,estado,fecha_hora,id_tipo,id_ubicacion) VALUES ('Cerradura Baño',0,now(),5,5);
INSERT INTO DISPOSITIVO (nombre,estado,fecha_hora,id_tipo,id_ubicacion) VALUES ('Botón Pánico Living',0,now(),5,6);
INSERT INTO DISPOSITIVO (nombre,estado,fecha_hora,id_tipo,id_ubicacion) VALUES ('Cerradura Dormitorio',0,now(),5,4);
INSERT INTO DISPOSITIVO (nombre,estado,fecha_hora,id_tipo,id_ubicacion) VALUES ('Sensor Ventana Comedor',0,now(),5,3);

-- MULTIMEDIA (id_tipo = 6)
INSERT INTO DISPOSITIVO (nombre,estado,fecha_hora,id_tipo,id_ubicacion) VALUES ('Smart TV Living',1,NOW(),6,6);
INSERT INTO DISPOSITIVO (nombre,estado,fecha_hora,id_tipo,id_ubicacion) VALUES ('Smart TV Dormitorio',0,NOW(),6,4);
INSERT INTO DISPOSITIVO (nombre,estado,fecha_hora,id_tipo,id_ubicacion) VALUES ('Parlante Inteligente Cocina',0,NOW(),6,1);
INSERT INTO DISPOSITIVO (nombre,estado,fecha_hora,id_tipo,id_ubicacion) VALUES ('Home Theater',1,NOW(),6,6);
INSERT INTO DISPOSITIVO (nombre,estado,fecha_hora,id_tipo,id_ubicacion) VALUES ('Proyector Oficina',0,NOW(),6,10);
INSERT INTO DISPOSITIVO (nombre,estado,fecha_hora,id_tipo,id_ubicacion) VALUES ('Sistema Sonido Comedor',1,NOW(),6,3);
INSERT INTO DISPOSITIVO (nombre,estado,fecha_hora,id_tipo,id_ubicacion) VALUES ('Tablet Control Casa',0,NOW(),6,6);
INSERT INTO DISPOSITIVO (nombre,estado,fecha_hora,id_tipo,id_ubicacion) VALUES ('Reproductor Streaming',0,NOW(),6,6);
INSERT INTO DISPOSITIVO (nombre,estado,fecha_hora,id_tipo,id_ubicacion) VALUES ('Radio Baño',0,NOW(),6,5);
INSERT INTO DISPOSITIVO (nombre,estado,fecha_hora,id_tipo,id_ubicacion) VALUES ('Parlante Jardín',0,NOW(),6,8);

-- RIEGO (id_tipo = 7)
INSERT INTO DISPOSITIVO (nombre,estado,fecha_hora,id_tipo,id_ubicacion) VALUES ('Riego Principal Jardín',1,NOW(),7,8);
INSERT INTO DISPOSITIVO (nombre,estado,fecha_hora,id_tipo,id_ubicacion) VALUES ('Riego Lateral Patio',0,NOW(),7,2);
INSERT INTO DISPOSITIVO (nombre,estado,fecha_hora,id_tipo,id_ubicacion) VALUES ('Riego Macetas Terraza',0,NOW(),7,8);
INSERT INTO DISPOSITIVO (nombre,estado,fecha_hora,id_tipo,id_ubicacion) VALUES ('Riego Canteros',0,NOW(),7,8);
INSERT INTO DISPOSITIVO (nombre,estado,fecha_hora,id_tipo,id_ubicacion) VALUES ('Sensor Humedad Jardín',1,NOW(),7,8);
INSERT INTO DISPOSITIVO (nombre,estado,fecha_hora,id_tipo,id_ubicacion) VALUES ('Sensor Lluvia Patio',0,NOW(),7,2);
INSERT INTO DISPOSITIVO (nombre,estado,fecha_hora,id_tipo,id_ubicacion) VALUES ('Válvula Riego Patio',0,NOW(),7,2);
INSERT INTO DISPOSITIVO (nombre,estado,fecha_hora,id_tipo,id_ubicacion) VALUES ('Timer Riego Jardín',0,NOW(),7,8);
INSERT INTO DISPOSITIVO (nombre,estado,fecha_hora,id_tipo,id_ubicacion) VALUES ('Riego Huerta',1,NOW(),7,8);
INSERT INTO DISPOSITIVO (nombre,estado,fecha_hora,id_tipo,id_ubicacion) VALUES ('Riego Césped',0,NOW(),7,8);

-- ENERGÍA (id_tipo = 8)
INSERT INTO DISPOSITIVO (nombre,estado,fecha_hora,id_tipo,id_ubicacion) VALUES ('Medidor Energía General',1,NOW(),8,6);
INSERT INTO DISPOSITIVO (nombre,estado,fecha_hora,id_tipo,id_ubicacion) VALUES ('Enchufe Inteligente Cocina',0,NOW(),8,1);
INSERT INTO DISPOSITIVO (nombre,estado,fecha_hora,id_tipo,id_ubicacion) VALUES ('Enchufe Inteligente Living',0,NOW(),8,6);
INSERT INTO DISPOSITIVO (nombre,estado,fecha_hora,id_tipo,id_ubicacion) VALUES ('Panel Solar Tejado',1,NOW(),8,8);
INSERT INTO DISPOSITIVO (nombre,estado,fecha_hora,id_tipo,id_ubicacion) VALUES ('UPS Oficina',0,NOW(),8,10);
INSERT INTO DISPOSITIVO (nombre,estado,fecha_hora,id_tipo,id_ubicacion) VALUES ('Regleta Inteligente Dormitorio',1,NOW(),8,4);
INSERT INTO DISPOSITIVO (nombre,estado,fecha_hora,id_tipo,id_ubicacion) VALUES ('Controlador Consumo Garage',0,NOW(),8,7);
INSERT INTO DISPOSITIVO (nombre,estado,fecha_hora,id_tipo,id_ubicacion) VALUES ('Interruptor General',0,NOW(),8,6);
INSERT INTO DISPOSITIVO (nombre,estado,fecha_hora,id_tipo,id_ubicacion) VALUES ('Medidor Energía Garage',0,NOW(),8,7);
INSERT INTO DISPOSITIVO (nombre,estado,fecha_hora,id_tipo,id_ubicacion) VALUES ('Batería Backup',0,NOW(),8,7);

-- PERSIANAS/CORTINAS (id_tipo = 9)
INSERT INTO DISPOSITIVO (nombre,estado,fecha_hora,id_tipo,id_ubicacion) VALUES ('Persiana Living',1,NOW(),9,6);
INSERT INTO DISPOSITIVO (nombre,estado,fecha_hora,id_tipo,id_ubicacion) VALUES ('Persiana Dormitorio',0,NOW(),9,4);
INSERT INTO DISPOSITIVO (nombre,estado,fecha_hora,id_tipo,id_ubicacion) VALUES ('Persiana Comedor',1,NOW(),9,3);
INSERT INTO DISPOSITIVO (nombre,estado,fecha_hora,id_tipo,id_ubicacion) VALUES ('Persiana Oficina',0,NOW(),9,10);
INSERT INTO DISPOSITIVO (nombre,estado,fecha_hora,id_tipo,id_ubicacion) VALUES ('Cortina Baño',1,NOW(),9,5);
INSERT INTO DISPOSITIVO (nombre,estado,fecha_hora,id_tipo,id_ubicacion) VALUES ('Persiana Cocina',0,NOW(),9,1);
INSERT INTO DISPOSITIVO (nombre,estado,fecha_hora,id_tipo,id_ubicacion) VALUES ('Cortina Living',1,NOW(),9,6);
INSERT INTO DISPOSITIVO (nombre,estado,fecha_hora,id_tipo,id_ubicacion) VALUES ('Cortina Dormitorio',0,NOW(),9,4);
INSERT INTO DISPOSITIVO (nombre,estado,fecha_hora,id_tipo,id_ubicacion) VALUES ('Persiana Garage',0,NOW(),9,7);
INSERT INTO DISPOSITIVO (nombre,estado,fecha_hora,id_tipo,id_ubicacion) VALUES ('Persiana Jardín',0,NOW(),9,8);

-- ASISTENTE DE VOZ (id_tipo = 10)
INSERT INTO DISPOSITIVO (nombre,estado,fecha_hora,id_tipo,id_ubicacion) VALUES ('Alexa Living',1,NOW(),10,6);
INSERT INTO DISPOSITIVO (nombre,estado,fecha_hora,id_tipo,id_ubicacion) VALUES ('Alexa Dormitorio',0,NOW(),10,4);
INSERT INTO DISPOSITIVO (nombre,estado,fecha_hora,id_tipo,id_ubicacion) VALUES ('Google Home Cocina',1,NOW(),10,1);
INSERT INTO DISPOSITIVO (nombre,estado,fecha_hora,id_tipo,id_ubicacion) VALUES ('Google Home Oficina',0,NOW(),10,10);
INSERT INTO DISPOSITIVO (nombre,estado,fecha_hora,id_tipo,id_ubicacion) VALUES ('HomePod Comedor',1,NOW(),10,3);
INSERT INTO DISPOSITIVO (nombre,estado,fecha_hora,id_tipo,id_ubicacion) VALUES ('HomePod Garage',0,NOW(),10,7);
INSERT INTO DISPOSITIVO (nombre,estado,fecha_hora,id_tipo,id_ubicacion) VALUES ('Echo Dot Baño',0,NOW(),10,5);
INSERT INTO DISPOSITIVO (nombre,estado,fecha_hora,id_tipo,id_ubicacion) VALUES ('Echo Show Living',1,NOW(),10,6);
INSERT INTO DISPOSITIVO (nombre,estado,fecha_hora,id_tipo,id_ubicacion) VALUES ('Nest Mini Patio',1,NOW(),10,2);
INSERT INTO DISPOSITIVO (nombre,estado,fecha_hora,id_tipo,id_ubicacion) VALUES ('Google Nest Hub Dormitorio',0,NOW(),10,4);


-- ACCIONES (16)
INSERT INTO ACCION (nombre,id_tipo) VALUES ('Encender',1);
INSERT INTO ACCION (nombre,id_tipo) VALUES ('Apagar',1);
INSERT INTO ACCION (nombre,id_tipo) VALUES ('Activar',2);
INSERT INTO ACCION (nombre,id_tipo) VALUES ('Desactivar',2);
INSERT INTO ACCION (nombre,id_tipo) VALUES ('Subir Temp',3);
INSERT INTO ACCION (nombre,id_tipo) VALUES ('Bajar Temp',3);

-- ILUMINACIÓN (id_tipo = 1)
INSERT INTO ACCION (nombre,id_tipo) VALUES ('Atenuar',1);
-- ELECTRODOMÉSTICO (id_tipo = 2)
INSERT INTO ACCION (nombre,id_tipo) VALUES ('Iniciar Ciclo',2);
-- CLIMATIZACIÓN (id_tipo = 3)
INSERT INTO ACCION (nombre,id_tipo) VALUES ('Programar Termostato',3);
-- SEGURIDAD (id_tipo = 4)
INSERT INTO ACCION (nombre,id_tipo) VALUES ('Armar Alarma',4);
-- CONTROL DE ACCESO (id_tipo = 5)
INSERT INTO ACCION (nombre,id_tipo) VALUES ('Desbloquear',5);
-- MULTIMEDIA (id_tipo = 6)
INSERT INTO ACCION (nombre,id_tipo) VALUES ('Reproducir Música',6);
-- RIEGO (id_tipo = 7)
INSERT INTO ACCION (nombre,id_tipo) VALUES ('Programar Horario',7);
-- ENERGÍA (id_tipo = 8)
INSERT INTO ACCION (nombre,id_tipo) VALUES ('Medir Consumo',8);
-- PERSIANAS/CORTINAS (id_tipo = 9)
INSERT INTO ACCION (nombre,id_tipo) VALUES ('Bajar',9);
-- ASISTENTE DE VOZ (id_tipo = 10)
INSERT INTO ACCION (nombre,id_tipo) VALUES ('Responder Pregunta',10);


-- CONFIGURACIONES (13)
INSERT INTO CONFIGURACION_DISPOSITIVO (id_dispositivo,atributo,valor) VALUES (1,'intensidad','80');
INSERT INTO CONFIGURACION_DISPOSITIVO (id_dispositivo,atributo,valor) VALUES (2,'modo','auto');
INSERT INTO CONFIGURACION_DISPOSITIVO (id_dispositivo,atributo,valor) VALUES (3,'temperatura','24');

-- Ejemplos de configuraciones para distintos dispositivos
INSERT INTO CONFIGURACION_DISPOSITIVO (id_dispositivo,atributo,valor) VALUES (1,'intensidad','60');        -- Luz Patio
INSERT INTO CONFIGURACION_DISPOSITIVO (id_dispositivo,atributo,valor) VALUES (2,'modo','eco');             -- Aspiradora Comedor
INSERT INTO CONFIGURACION_DISPOSITIVO (id_dispositivo,atributo,valor) VALUES (3,'temperatura','22');       -- Aire Dormitorio
INSERT INTO CONFIGURACION_DISPOSITIVO (id_dispositivo,atributo,valor) VALUES (4,'color','blanco cálido');  -- Luz Comedor
INSERT INTO CONFIGURACION_DISPOSITIVO (id_dispositivo,atributo,valor) VALUES (5,'velocidad','media');      -- Ventilador Techo Comedor
INSERT INTO CONFIGURACION_DISPOSITIVO (id_dispositivo,atributo,valor) VALUES (6,'sensibilidad','alta');    -- Sensor Movimiento Living
INSERT INTO CONFIGURACION_DISPOSITIVO (id_dispositivo,atributo,valor) VALUES (7,'volumen','30');           -- Smart TV Living
INSERT INTO CONFIGURACION_DISPOSITIVO (id_dispositivo,atributo,valor) VALUES (8,'programa','delicado');    -- Lavarropas
INSERT INTO CONFIGURACION_DISPOSITIVO (id_dispositivo,atributo,valor) VALUES (9,'apertura','50');          -- Persiana Dormitorio
INSERT INTO CONFIGURACION_DISPOSITIVO (id_dispositivo,atributo,valor) VALUES (10,'idioma','español');      -- Alexa Living


-- AUTOMATIZACIONES (2)
INSERT INTO AUTOMATIZACIONES (nombre,id_vivienda,hora_inicio,hora_fin,activa) VALUES ('Activar luces del Patio',1,'19:00:00','23:59:59',1);
INSERT INTO AUTOMATIZACIONES (nombre,id_vivienda,hora_inicio,hora_fin,activa) VALUES ('activador/desactivador aspiradora',1,'09:00:00','11:00:00',1);

-- ILUMINACIÓN
INSERT INTO AUTOMATIZACIONES (nombre,id_vivienda,hora_inicio,hora_fin,activa) 
VALUES ('Encender luces del jardín al anochecer',1,'18:30:00','23:00:00',1);
-- ELECTRODOMÉSTICO
INSERT INTO AUTOMATIZACIONES (nombre,id_vivienda,hora_inicio,hora_fin,activa) 
VALUES ('Iniciar cafetera por la mañana',1,'07:00:00','07:30:00',1);
-- CLIMATIZACIÓN
INSERT INTO AUTOMATIZACIONES (nombre,id_vivienda,hora_inicio,hora_fin,activa) 
VALUES ('Encender aire acondicionado en dormitorio',1,'21:30:00','23:00:00',1);
-- SEGURIDAD
INSERT INTO AUTOMATIZACIONES (nombre,id_vivienda,hora_inicio,hora_fin,activa) 
VALUES ('Activar alarma de seguridad nocturna',1,'23:00:00','06:00:00',1);
-- CONTROL DE ACCESO
INSERT INTO AUTOMATIZACIONES (nombre,id_vivienda,hora_inicio,hora_fin,activa) 
VALUES ('Desbloquear puerta principal al llegar a casa',1,'18:00:00','18:15:00',1);
-- MULTIMEDIA
INSERT INTO AUTOMATIZACIONES (nombre,id_vivienda,hora_inicio,hora_fin,activa) 
VALUES ('Reproducir música ambiente en el living los sábados',1,'19:00:00','21:00:00',1);
-- RIEGO
INSERT INTO AUTOMATIZACIONES (nombre,id_vivienda,hora_inicio,hora_fin,activa) 
VALUES ('Regar jardín por la mañana',1,'06:00:00','06:30:00',1);
-- ENERGÍA
INSERT INTO AUTOMATIZACIONES (nombre,id_vivienda,hora_inicio,hora_fin,activa) 
VALUES ('Apagar enchufes inteligentes durante la noche',1,'00:00:00','06:00:00',1);
-- PERSIANAS/CORTINAS
INSERT INTO AUTOMATIZACIONES (nombre,id_vivienda,hora_inicio,hora_fin,activa) 
VALUES ('Subir persianas al amanecer',1,'07:00:00','07:15:00',1);
-- ASISTENTE DE VOZ
INSERT INTO AUTOMATIZACIONES (nombre,id_vivienda,hora_inicio,hora_fin,activa) 
VALUES ('Leer agenda diaria al despertar',1,'07:30:00','07:35:00',1);



-- AUTOMATIZACION_OBJETIVO (2)
INSERT INTO AUTOMATIZACION_OBJETIVO (id_automatizacion,id_tipo,id_ubicacion) VALUES (1,1,2); -- luces del patio
INSERT INTO AUTOMATIZACION_OBJETIVO (id_automatizacion,id_tipo,id_ubicacion) VALUES (2,2,3); -- aspiradora comedor
INSERT INTO AUTOMATIZACION_OBJETIVO (id_automatizacion,id_tipo,id_ubicacion) VALUES (3,1,8);  -- Encender luces del jardín (iluminación, jardín)
INSERT INTO AUTOMATIZACION_OBJETIVO (id_automatizacion,id_tipo,id_ubicacion) VALUES (4,2,1);  -- Iniciar cafetera por la mañana (electrodoméstico, cocina)
INSERT INTO AUTOMATIZACION_OBJETIVO (id_automatizacion,id_tipo,id_ubicacion) VALUES (5,3,4);  -- Encender aire acondicionado en dormitorio (climatización, dormitorio)
INSERT INTO AUTOMATIZACION_OBJETIVO (id_automatizacion,id_tipo,id_ubicacion) VALUES (6,4,6);  -- Activar alarma de seguridad nocturna (seguridad, living)
INSERT INTO AUTOMATIZACION_OBJETIVO (id_automatizacion,id_tipo,id_ubicacion) VALUES (7,5,9);  -- Desbloquear puerta principal (control de acceso, pasillo/entrada)
INSERT INTO AUTOMATIZACION_OBJETIVO (id_automatizacion,id_tipo,id_ubicacion) VALUES (8,6,6);  -- Reproducir música ambiente en el living (multimedia, living)
INSERT INTO AUTOMATIZACION_OBJETIVO (id_automatizacion,id_tipo,id_ubicacion) VALUES (9,7,8);  -- Regar jardín por la mañana (riego, jardín)
INSERT INTO AUTOMATIZACION_OBJETIVO (id_automatizacion,id_tipo,id_ubicacion) VALUES (10,8,6); -- Apagar enchufes inteligentes durante la noche (energía, living)
INSERT INTO AUTOMATIZACION_OBJETIVO (id_automatizacion,id_tipo,id_ubicacion) VALUES (11,9,4); -- Subir persianas al amanecer (persianas/cortinas, dormitorio)
INSERT INTO AUTOMATIZACION_OBJETIVO (id_automatizacion,id_tipo,id_ubicacion) VALUES (12,10,6);-- Leer agenda diaria al despertar (asistente de voz, living)




-- Consultas simples
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


-- Consultas  Avanzadas

-- 1. Multitabla: Listar todos los dispositivos, mostrando su nombre, estado, ubicación, tipo y la vivienda a la que pertenecen.
SELECT 
    d.nombre AS dispositivo,
    d.estado,
    td.nombre AS tipo_dispositivo,
    u.nombre AS ubicacion,
    v.direccion AS vivienda
FROM 
    DISPOSITIVO d
    INNER JOIN TIPO_DISPOSITIVO td ON d.id_tipo = td.id_tipo
    INNER JOIN UBICACION u ON d.id_ubicacion = u.id_ubicacion
    INNER JOIN VIVIENDA v ON u.id_vivienda = v.id_vivienda;
-- Muestra el inventario de dispositivos, fundamental para gestión y soporte.

-- 2. Multitabla: Mostrar qué usuarios tienen acceso a cada vivienda y sus roles.
SELECT 
    uv.correo,
    us.nombres,
    us.apellidos,
    v.direccion,
    uv.rol
FROM 
    USUARIO_VIVIENDA uv
    INNER JOIN USUARIO us ON uv.correo = us.correo
    INNER JOIN VIVIENDA v ON uv.id_vivienda = v.id_vivienda;
-- Ayuda a saber la relación usuario-vivienda y los permisos asignados.

-- 3. Multitabla: Listar todas las automatizaciones activas, con su rango horario y dirección de la vivienda.
SELECT 
    a.nombre AS automatizacion,
    v.direccion AS vivienda,
    a.hora_inicio,
    a.hora_fin
FROM 
    AUTOMATIZACIONES a
    INNER JOIN VIVIENDA v ON a.id_vivienda = v.id_vivienda
WHERE
    a.activa = 1;
-- Permite monitorear qué automatizaciones están funcionando actualmente.

-- 4. Multitabla: Mostrar para cada automatización sus objetivos (tipos de dispositivos y ubicaciones involucradas).
SELECT 
    aut.nombre AS automatizacion,
    td.nombre AS tipo_dispositivo,
    ub.nombre AS ubicacion
FROM 
    AUTOMATIZACIONES aut
    INNER JOIN AUTOMATIZACION_OBJETIVO ao ON aut.id_automatizacion = ao.id_automatizacion
    INNER JOIN TIPO_DISPOSITIVO td ON ao.id_tipo = td.id_tipo
    INNER JOIN UBICACION ub ON ao.id_ubicacion = ub.id_ubicacion;
-- Es útil para entender el alcance y objetivo de cada automatización.

-- 5. Multitabla: Listar todas las configuraciones actuales de los dispositivos, mostrando nombre del dispositivo, atributo y valor.
SELECT
    d.nombre AS dispositivo,
    c.atributo,
    c.valor
FROM
    CONFIGURACION_DISPOSITIVO c
    INNER JOIN DISPOSITIVO d ON c.id_dispositivo = d.id_dispositivo;
-- Fundamental para auditoría y diagnósticos de funcionamiento de dispositivos.

-- ---------------------------------
-- SUBCONSULTAS
-- ---------------------------------

-- 6. Subconsulta: Dispositivos que están apagados (estado=0), mostrando su ubicación y vivienda.
SELECT 
    d.nombre AS dispositivo,
    u.nombre AS ubicacion,
    (SELECT direccion FROM VIVIENDA v WHERE v.id_vivienda = u.id_vivienda) AS vivienda
FROM 
    DISPOSITIVO d
    INNER JOIN UBICACION u ON d.id_ubicacion = u.id_ubicacion
WHERE
    d.estado = 0;
-- Permite identificar rápidamente los dispositivos apagados y dónde están.

-- 7. Subconsulta: Para cada vivienda, cuántos usuarios están registrados.
SELECT 
    v.direccion,
    (SELECT COUNT(*) FROM USUARIO_VIVIENDA uv WHERE uv.id_vivienda = v.id_vivienda) AS cantidad_usuarios
FROM 
    VIVIENDA v;
-- Útil para análisis de uso y dimensionamiento de soporte.

-- 8. Subconsulta: Listar usuarios que tienen al menos un dispositivo en alguna vivienda (usando subconsulta EXISTS).
SELECT 
    u.correo,
    u.nombres,
    u.apellidos
FROM 
    USUARIO u
WHERE 
    EXISTS (
        SELECT 1
        FROM USUARIO_VIVIENDA uv
        INNER JOIN VIVIENDA v ON uv.id_vivienda = v.id_vivienda
        INNER JOIN UBICACION ub ON v.id_vivienda = ub.id_vivienda
        INNER JOIN DISPOSITIVO d ON ub.id_ubicacion = d.id_ubicacion
        WHERE uv.correo = u.correo
    );
-- Permite identificar usuarios con dispositivos asociados, útil para segmentación y comunicación.
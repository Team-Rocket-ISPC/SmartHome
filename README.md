# 🏠 SmartHome Solutions  
**Sistema de Gestión de Dispositivos Inteligentes para el Hogar**

---

## 📘 Propósito  
El propósito de este proyecto es desarrollar una aplicación que permita la gestión integral de dispositivos inteligentes dentro de un entorno doméstico.  
El sistema busca facilitar al usuario la administración, control y automatización de distintos dispositivos (luces, cámaras, termostatos, electrodomésticos, etc.) desde una interfaz centralizada, priorizando la **seguridad**, **eficiencia**, **privacidad** y **usabilidad**.

---

## 🌍 Contexto  
**SmartHome Solutions** es una empresa ficticia que promueve el desarrollo de tecnologías de automatización ética y responsable.  
El proyecto se enmarca en el **AWS Well-Architected Framework**, adoptando al menos cuatro de sus pilares:  
- Excelencia Operativa  
- Seguridad  
- Fiabilidad  
- Eficiencia del Rendimiento  
- Optimización de Costos  
- Sostenibilidad  

Además, el sistema considera los aspectos éticos asociados al tratamiento de datos personales en entornos privados, y promueve prácticas de programación profesional y responsable.

---

## 🎯 Alcance  
El programa permite:

- Registro e inicio de sesión de usuarios (estándar y administrador).  
- Registro, consulta, modificación y eliminación de dispositivos inteligentes.  
- Ejecución y consulta de automatizaciones.  
- Visualización del estado actual de los dispositivos.  
- Aplicación del patrón de diseño **DAO** para separar la lógica de negocio del acceso a datos.  
- Conexión con una **base de datos relacional (MySQL)** para persistencia de la información.  

Incluye además:
- Scripts SQL (DDL/DML) para crear e inicializar la base de datos.  
- Consultas multitabla y subconsultas justificadas según el contexto del negocio.  
- Pruebas unitarias en verde (manteniendo las desarrolladas en evidencias previas).  
- Cumplimiento de requerimientos no funcionales: **modularidad, legibilidad, eficiencia y usabilidad.**

---

## ⚙️ Tecnologías Utilizadas  
- **Lenguaje:** Python  
- **Paradigma:** Programación Orientada a Objetos  
- **Patrón de Diseño:** DAO (Data Access Object)  
- **Base de Datos:** MySQL  
- **Control de Versiones:** Git / GitHub  
- **Diagramas:** Draw.io / Lucidchart  
- **Normas de Estilo:** Nomenclatura estándar de la comunidad Python (PEP8)

---

## 🧩 Estructura del Proyecto  
```
POO-SmartHome/
│
├── main.py                     # Punto de entrada del programa
├── dominio/
│   ├── usuario.py              # Clase Usuario
│   ├── dispositivo.py          # Clase Dispositivo
│   └── automatizacion.py       # Clase Automatizacion
│
├── dao/
│   ├── usuario_dao.py          # Acceso a datos del usuario
│   ├── dispositivo_dao.py      # Acceso a datos de dispositivos
│   └── automatizacion_dao.py   # Acceso a datos de automatizaciones
│
├── conn/
│   └── db_conn.py              # Manejador de conexión a la base de datos
│
└── tests/
    └── test_*.py               # Pruebas unitarias
```

---

## 💾 Base de Datos  
La base de datos fue diseñada bajo modelo relacional, asegurando integridad referencial y normalización.  
Incluye scripts **DDL** y **DML** para crear e inicializar las tablas en **MySQL**.  

Ejemplo de ejecución:
```sql
-- Crear base de datos
CREATE DATABASE smarthome_db;
USE smarthome_db;

-- Crear tablas
SOURCE ./BD-Evidencia-6/ddl_script.sql;

-- Insertar datos iniciales y ejecutar consultas
SOURCE ./BD-Evidencia-6/dml_script.sql;
```

Recomendado ejecutarlo en un entorno online como [OneCompiler](https://onecompiler.com/mysql).

---

## 👥 Autores  
**Equipo de Desarrollo - Módulo Programador**  
1. Nahuel Gastón Maclay, 41846200, nahuelmaclay18@gmail.com
2. Christian José Murua Ayosa, 35674639, cristianmurua.18@gmail.com
3. Jeremías Ezequiel Ayala, 42985088, jere4298@gmail.com
4. Mariano Ivan Battista, 38002217, battista.mariano.i@gmail.com

**Institución:** ISPC
**Carrera:** Tecnicatura en Desarrollo de Software  
**Módulo:** Programador I
**Año:** 2025  

---

## 🧭 Referencias Éticas y Profesionales  
Este proyecto incluye un enfoque ético en la protección de datos personales y el uso responsable de la automatización, considerando:
- Transparencia en el funcionamiento de algoritmos.  
- Consentimiento informado del usuario.  
- Seguridad en el almacenamiento y transmisión de información.  
- Impacto social, económico y ambiental de la tecnología.  

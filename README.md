# Proyecto Sistemas Operacionales  
## Simulación de un Sistema de Archivos usando Docker

### 📌 Descripción general
Este proyecto consiste en la simulación de un sistema de archivos utilizando contenedores Docker.  
El objetivo es comprender, de forma práctica, conceptos fundamentales de los Sistemas Operacionales como:
- gestión de archivos
- persistencia de datos
- aislamiento de procesos
Cada contenedor representa un entorno aislado que interactúa con un sistema de archivos simulado mediante volúmenes de Docker.
---

### 🎯 Objetivo del proyecto
Simular el funcionamiento básico de un sistema de archivos, permitiendo realizar operaciones como creación, lectura, escritura y eliminación de archivos, y analizar su persistencia y aislamiento utilizando Docker.
---

### 🧱 Estructura del proyecto
La estructura base del proyecto es la siguiente:
ProyectoOperacionales/
│
├── app/ # Código de la aplicación (Python / C++ / Java)
│ └── main.py
│
├── docker/ # Configuración de Docker
│ └── Dockerfile
│
├── volumes/
│ └── data/ # Sistema de archivos simulado (volumen)
│
├── docker-compose.yml # Orquestación de contenedores
├── README.md # Documentación del proyecto
└── .gitignore

### 1. ▶️ Clonar el repositorio
```terminal bash
git clone https://github.com/alalo10/ProyectoOperacionales.git
cd ProyectoOperacionales
```

### ¿Qué es un Dockerfile?
Un Dockerfile es un archivo de texto que contiene las instrucciones para construir una imagen Docker.

Dicho de forma sencilla:

📦 Dockerfile = receta
🧁 Imagen Docker = torta ya horneada
▶️ Contenedor = torta servida y en uso

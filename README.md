# Proyecto Sistemas Operacionales  
## Simulación de un Sistema de Archivos usando Docker

---

## 📌 Descripción general
Este proyecto consiste en la simulación de un sistema de archivos utilizando contenedores Docker.  
El objetivo es comprender, de forma práctica, conceptos fundamentales de los Sistemas Operacionales como:

- gestión de archivos  
- persistencia de datos  
- aislamiento de procesos  

Cada contenedor representa un entorno aislado que interactúa con un sistema de archivos simulado mediante volúmenes de Docker.

---

## 🎯 Objetivo del proyecto
Simular el funcionamiento básico de un sistema de archivos, permitiendo realizar operaciones como creación, lectura, escritura y eliminación de archivos, y analizar su persistencia y aislamiento utilizando Docker.

---

## 🧱 Estructura del proyecto

La estructura base del proyecto es la siguiente:

```
ProyectoOperacionales/
│
├── app/                  # Código de la aplicación (Python / C++ / Java)
│   └── main.py
│
├── docker/               # Configuración de Docker
│   └── Dockerfile
│
├── volumes/
│   └── data/             # Sistema de archivos simulado (volumen)
│
├── docker-compose.yml    # Orquestación de contenedores
├── README.md             # Documentacion del proyecto
└── .gitignore
```

---

## ▶️ Clonar el repositorio

```bash
git clone https://github.com/alalo10/ProyectoOperacionales.git
cd ProyectoOperacionales
```

---

## 🐳 ¿Qué es un Dockerfile?

Un **Dockerfile** es un archivo de texto que contiene las instrucciones necesarias para construir una imagen Docker.

Los contenedores Docker se ejecutan sobre el kernel de Linux. En sistemas Windows, tecnologías como **WSL (Windows Subsystem for Linux)** permiten ejecutar contenedores Linux de forma eficiente.

Dicho de forma sencilla:

- 📦 Dockerfile = receta  
- 🧁 Imagen Docker = aplicación construida  
- ▶️ Contenedor = aplicación en ejecución  

---

## 📁 ¿Qué vamos a construir realmente?

Un **sistema de archivos simulado con Docker**, diseñado con fines académicos para comprender cómo funcionan los Sistemas Operacionales.

Este proyecto no busca crear un sistema operativo completo, sino simular su comportamiento básico.

---

## 🖥️ Interfaz del sistema

### 1️⃣ ¿Interfaz, funcionalidad o ambos?
Se implementan ambas, pero de forma minimalista.

### ❌ Lo que NO se implementa
- Interfaz gráfica (GUI)  
- Exploradores visuales o ventanas  
- Interpretación interna de PDFs, Word o Excel  

Estas funciones no forman parte del objetivo académico y aumentarían innecesariamente la complejidad.

### ✅ Lo que SÍ se implementa
🖥️ Interfaz por consola (CLI), similar a Unix/Linux:

```
ls
cd
mkdir
touch
```

Esto representa cómo los sistemas operativos gestionan archivos internamente.

---

## 📂 ¿Qué es un archivo en nuestro sistema?

Para un sistema operativo:

- `.txt`
- `.pdf`
- `.xlsx`
- `.docx`

todos son simplemente datos organizados en bytes.

El sistema no interpreta formatos; únicamente permite:

- crear archivos  
- borrar archivos  
- mover archivos  
- listar contenido  
- leer texto (solo archivos `.txt`)  

Esto es coherente con el funcionamiento real de un sistema operativo.

---

## ⚙️ Funcionalidades del sistema (MVP académico)

### 📁 Gestión de directorios

Permite:

- crear directorios  
- listar contenido  
- navegar entre carpetas  
- eliminar directorios vacíos  

**Comandos simulados:**

```bash
mkdir docs
cd docs
ls
rmdir docs
```

---

### 📄 Gestión de archivos

Permite:

- crear archivos vacíos  
- eliminar archivos  
- mover archivos  
- renombrar archivos  
- mostrar contenido de archivos `.txt`  

**Ejemplos:**

```bash
touch notas.txt
rm notas.txt
mv notas.txt backup.txt
cat notas.txt
```

---

### 🔐 Metadatos (importante en Sistemas Operacionales)

Cada archivo posee:

- nombre  
- tamaño  
- tipo  
- fecha de creación  
- fecha de modificación  

Estos metadatos pueden obtenerse del sistema Linux del contenedor o simularse mediante estructuras en memoria.

---

## 🐳 Rol de Docker en el proyecto

Docker garantiza que:

- todos los integrantes usan el mismo entorno  
- no importa si se utiliza Windows, Linux o Mac  
- el sistema funciona igual en cualquier computadora  
- los procesos se ejecutan de forma aislada  
- los datos pueden persistir mediante volúmenes  

El contenedor representa:

> Un sistema Linux que ejecuta un gestor de archivos simulado por consola.

---

## 💾 Persistencia de datos

El volumen Docker permite que los archivos creados:

- permanezcan aunque el contenedor se detenga  
- no se pierdan al reiniciar el sistema  
- simulen el almacenamiento real de un sistema operativo  

---

## 📚 Conclusión

Este proyecto permite comprender de forma práctica cómo un sistema operativo gestiona archivos, mantiene la persistencia de datos y proporciona aislamiento de procesos, utilizando Docker como herramienta para simular estos comportamientos en un entorno controlado y portable.

---

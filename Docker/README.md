# Gestor de archivos con Docker y Flask

Proyecto universitario sencillo para practicar Docker, Docker Compose, Flask y volumenes persistentes.

## Estructura

```text
.
├── backend/
│   ├── app.py
│   └── requirements.txt
├── frontend/
│   └── index.html
├── Dockerfile
├── docker-compose.yml
└── README.md
```

## Que hace

- Crear archivos de texto.
- Listar archivos guardados.
- Eliminar archivos.
- Guardar los archivos en un volumen Docker para conservarlos aunque el contenedor se reinicie.

## Ejecutar

1. Construir y levantar el proyecto:

```bash
docker compose up --build
```

2. Abrir en el navegador:

```text
http://localhost:5000
```

3. Detener el proyecto:

```bash
docker compose down
```

## Probar la persistencia

1. Crea un archivo desde la pagina web.
2. Deten el contenedor:

```bash
docker compose down
```

3. Vuelve a levantarlo:

```bash
docker compose up
```

El archivo seguira apareciendo porque se guarda en el volumen `archivos_data`.

## Endpoints del backend

- `GET /api/files`: lista los archivos.
- `POST /api/files`: crea un archivo.
- `DELETE /api/files/<nombre>`: elimina un archivo.

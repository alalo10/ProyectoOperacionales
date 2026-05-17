import os
import re
from pathlib import Path

from flask import Flask, jsonify, request, send_from_directory


BASE_DIR = Path(__file__).resolve().parent.parent
FRONTEND_DIR = BASE_DIR / "frontend"
FILES_DIR = Path(os.environ.get("FILES_DIR", "/data/files"))

app = Flask(__name__)
FILES_DIR.mkdir(parents=True, exist_ok=True)


def safe_file_path(filename):
    if not filename or "/" in filename or "\\" in filename:
        return None

    if not re.match(r"^[a-zA-Z0-9_. -]+$", filename):
        return None

    file_path = FILES_DIR / filename
    if file_path.resolve().parent != FILES_DIR.resolve():
        return None

    return file_path


@app.get("/")
def index():
    return send_from_directory(FRONTEND_DIR, "index.html")


@app.get("/api/files")
def list_files():
    files = []

    for file_path in sorted(FILES_DIR.iterdir()):
        if file_path.is_file():
            files.append(
                {
                    "name": file_path.name,
                    "size": file_path.stat().st_size,
                }
            )

    return jsonify(files)


@app.post("/api/files")
def create_file():
    data = request.get_json(silent=True) or {}
    filename = data.get("filename", "").strip()
    content = data.get("content", "")
    file_path = safe_file_path(filename)

    if file_path is None:
        return jsonify({"error": "Nombre de archivo invalido"}), 400

    file_path.write_text(content, encoding="utf-8")
    return jsonify({"message": "Archivo creado", "filename": filename}), 201


@app.delete("/api/files/<filename>")
def delete_file(filename):
    file_path = safe_file_path(filename)

    if file_path is None:
        return jsonify({"error": "Nombre de archivo invalido"}), 400

    if not file_path.exists():
        return jsonify({"error": "Archivo no encontrado"}), 404

    file_path.unlink()
    return jsonify({"message": "Archivo eliminado", "filename": filename})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

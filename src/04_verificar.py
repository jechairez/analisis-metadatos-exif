from pathlib import Path
from PIL import Image

RAIZ = Path(__file__).resolve().parent.parent
ARCHIVOS = [
    RAIZ / "data" / "DSCN0010.jpg",
    RAIZ / "data" / "DSCN0010_sanitizada.jpg",
]

print("=== VERIFICACIÓN ===\n")

for ruta in ARCHIVOS:
    if not ruta.exists():
        print(f"{ruta.name:28}: archivo no encontrado")
        continue

    with Image.open(ruta) as imagen:
        exif = imagen.getexif()
        print(f"{ruta.name:28}: {len(exif)} entradas EXIF en el IFD principal")

print("\nLa versión sanitizada debería reportar 0 entradas EXIF.")

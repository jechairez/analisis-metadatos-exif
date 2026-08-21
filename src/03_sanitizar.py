from pathlib import Path
from PIL import Image

RAIZ = Path(__file__).resolve().parent.parent
ORIGINAL = RAIZ / "data" / "DSCN0010.jpg"
SALIDA = RAIZ / "data" / "DSCN0010_sanitizada.jpg"

with Image.open(ORIGINAL) as imagen:
    copia = imagen.copy()
    copia.save(SALIDA, format="JPEG", quality=95)

print(f"Imagen sanitizada guardada en: {SALIDA}")
print("Se generó una nueva copia sin conservar el bloque EXIF original.")

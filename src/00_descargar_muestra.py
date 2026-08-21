from pathlib import Path
from urllib.request import urlretrieve

URL = "https://raw.githubusercontent.com/ianare/exif-samples/master/jpg/gps/DSCN0010.jpg"
DESTINO = Path(__file__).resolve().parent.parent / "data" / "DSCN0010.jpg"

DESTINO.parent.mkdir(parents=True, exist_ok=True)

print("Descargando imagen de muestra...")
urlretrieve(URL, DESTINO)
print(f"Imagen guardada en: {DESTINO}")

from pathlib import Path
from PIL import Image, ExifTags

RUTA = Path(__file__).resolve().parent.parent / "data" / "DSCN0010.jpg"


def convertir_gps(coordenada, referencia):
    grados = float(coordenada[0])
    minutos = float(coordenada[1])
    segundos = float(coordenada[2])

    decimal = grados + minutos / 60 + segundos / 3600

    if isinstance(referencia, bytes):
        referencia = referencia.decode(errors="ignore")

    if referencia in {"S", "W"}:
        decimal *= -1

    return decimal


def cargar_exif(ruta):
    imagen = Image.open(ruta)
    exif = imagen.getexif()

    datos = {}

    for clave, valor in exif.items():
        etiqueta = ExifTags.TAGS.get(clave, clave)
        datos[etiqueta] = valor

    exif_ifd = exif.get_ifd(ExifTags.IFD.Exif)
    for clave, valor in exif_ifd.items():
        etiqueta = ExifTags.TAGS.get(clave, clave)
        if etiqueta != "MakerNote":
            datos[etiqueta] = valor

    gps_ifd = exif.get_ifd(ExifTags.IFD.GPSInfo)
    gps = {
        ExifTags.GPSTAGS.get(clave, clave): valor
        for clave, valor in gps_ifd.items()
    }

    return imagen, datos, gps


imagen, datos, gps = cargar_exif(RUTA)

print("=" * 58)
print("          ANÁLISIS DE METADATOS EXIF")
print("=" * 58)
print(f"\nArchivo    : {RUTA.name}")
print(f"Formato    : {imagen.format}")
print(f"Resolución : {imagen.width} x {imagen.height}")

print("\n--- DISPOSITIVO ---")
print(f"Fabricante : {datos.get('Make', 'No disponible')}")
print(f"Modelo     : {datos.get('Model', 'No disponible')}")
print(f"Software   : {datos.get('Software', 'No disponible')}")

print("\n--- FECHA Y CAPTURA ---")
fecha = datos.get("DateTimeOriginal", datos.get("DateTime", "No disponible"))
print(f"Fecha      : {fecha}")
print(f"ISO        : {datos.get('ISOSpeedRatings', 'No disponible')}")

exposicion = datos.get("ExposureTime")
if exposicion is not None:
    valor = float(exposicion)
    if 0 < valor < 1:
        print(f"Exposición : 1/{round(1 / valor)} s")
    else:
        print(f"Exposición : {valor} s")
else:
    print("Exposición : No disponible")

print("\n--- GPS ---")
latitud = None
longitud = None

if all(campo in gps for campo in [
    "GPSLatitude",
    "GPSLatitudeRef",
    "GPSLongitude",
    "GPSLongitudeRef",
]):
    latitud = convertir_gps(gps["GPSLatitude"], gps["GPSLatitudeRef"])
    longitud = convertir_gps(gps["GPSLongitude"], gps["GPSLongitudeRef"])
    print(f"Latitud    : {latitud:.6f}")
    print(f"Longitud   : {longitud:.6f}")
else:
    print("No se encontraron coordenadas GPS.")

print("\n--- EVALUACIÓN DIDÁCTICA ---")

hallazgos = []

if datos.get("Make") or datos.get("Model"):
    hallazgos.append(("MEDIA", "El dispositivo utilizado puede identificarse."))

if datos.get("DateTimeOriginal") or datos.get("DateTime"):
    hallazgos.append(("MEDIA", "La fecha y hora de captura están disponibles."))

if latitud is not None and longitud is not None:
    hallazgos.append(("ALTA", "La ubicación geográfica está expuesta en el archivo."))

if hallazgos:
    for nivel, texto in hallazgos:
        print(f"[{nivel:5}] {texto}")
else:
    print("No se identificaron campos relevantes en esta revisión.")

print("\nNota: la criticidad real depende del contexto de publicación.")

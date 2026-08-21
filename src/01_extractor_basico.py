from pathlib import Path
from PIL import Image, ExifTags

RUTA = Path(__file__).resolve().parent.parent / "data" / "DSCN0010.jpg"

imagen = Image.open(RUTA)
exif = imagen.getexif()

campos_interes = {
    "Make",
    "Model",
    "Software",
    "DateTime",
    "DateTimeOriginal",
    "ISOSpeedRatings",
    "ExposureTime",
}

print("=== INFORMACIÓN ENCONTRADA ===\n")

# IFD principal
for clave, valor in exif.items():
    etiqueta = ExifTags.TAGS.get(clave, clave)
    if etiqueta in campos_interes:
        print(f"{etiqueta:20}: {valor}")

# EXIF IFD
exif_ifd = exif.get_ifd(ExifTags.IFD.Exif)
for clave, valor in exif_ifd.items():
    etiqueta = ExifTags.TAGS.get(clave, clave)
    if etiqueta in campos_interes:
        print(f"{etiqueta:20}: {valor}")

# GPS IFD
print("\n=== GPS ===")
gps_ifd = exif.get_ifd(ExifTags.IFD.GPSInfo)

for clave, valor in gps_ifd.items():
    etiqueta = ExifTags.GPSTAGS.get(clave, clave)
    print(f"{etiqueta:20}: {valor}")

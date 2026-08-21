# Análisis de metadatos EXIF

Repositorio didáctico para una clase de **Análisis de Información en el Ciberespacio**.

El objetivo es extraer metadatos EXIF de una imagen, interpretar qué información puede representar una exposición y aplicar una sanitización básica antes de publicar el archivo.

## Estructura

```text
analisis-metadatos-exif/
├── README.md
├── requirements.txt
├── .gitignore
├── data/
│   └── README.md
├── src/
│   ├── 00_descargar_muestra.py
│   ├── 01_extractor_basico.py
│   ├── 02_analisis_completo.py
│   ├── 03_sanitizar.py
│   └── 04_verificar.py
└── ejercicios/
    ├── ejercicio_resuelto.md
    └── reto.md
```

## Preparación

```bash
python -m venv .venv
```

En Windows:

```bash
.venv\Scripts\activate
```

Instala la dependencia:

```bash
python -m pip install -r requirements.txt
```

## Imagen de muestra

La práctica utiliza `DSCN0010.jpg`, una imagen pública del repositorio `ianare/exif-samples` que conserva metadatos EXIF y GPS.

Descárgala con:

```bash
python src/00_descargar_muestra.py
```

El archivo se guardará en `data/DSCN0010.jpg`.

## Ejecución

Extractor sencillo para explicar en clase:

```bash
python src/01_extractor_basico.py
```

Análisis completo:

```bash
python src/02_analisis_completo.py
```

Sanitización:

```bash
python src/03_sanitizar.py
```

Verificación:

```bash
python src/04_verificar.py
```

## Flujo de análisis

```text
Archivo → extracción → selección → contextualización → evaluación → mitigación → verificación
```

La herramienta recupera datos; el análisis ocurre cuando esos datos se relacionan con un contexto y un posible riesgo.

## Uso responsable

Trabaja únicamente con archivos propios, material público destinado a análisis o archivos para los que tengas autorización. La presencia de metadatos no constituye por sí misma una vulnerabilidad; su relevancia depende del contexto de publicación.

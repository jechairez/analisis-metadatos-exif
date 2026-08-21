# Ejercicio resuelto: análisis de metadatos EXIF

## Objetivo

Extraer información asociada a una fotografía, identificar datos potencialmente sensibles y comprobar el efecto de una sanitización básica.

## Paso 1. Preparar la imagen

```bash
python src/00_descargar_muestra.py
```

## Paso 2. Ejecutar el extractor básico

```bash
python src/01_extractor_basico.py
```

Identifica al menos estos tipos de información:

- fabricante y modelo del dispositivo;
- software utilizado;
- fecha y hora de captura;
- información GPS.

## Paso 3. Interpretar

No todos los metadatos tienen la misma relevancia. Por ejemplo:

| Metadato | Posible interpretación |
|---|---|
| Modelo de cámara | contexto técnico del dispositivo |
| Fecha/hora | temporalidad del evento |
| GPS | ubicación de captura |

La importancia real depende del contexto. Una ubicación puede ser irrelevante en una fotografía turística y sensible en una fotografía de una instalación restringida.

## Paso 4. Ejecutar el análisis completo

```bash
python src/02_analisis_completo.py
```

Observa cómo el programa transforma las coordenadas GPS a grados decimales y realiza una clasificación didáctica inicial.

## Paso 5. Sanitizar

```bash
python src/03_sanitizar.py
```

Se generará `data/DSCN0010_sanitizada.jpg`.

## Paso 6. Verificar

```bash
python src/04_verificar.py
```

Compara la imagen original con la copia sanitizada.

## Conclusión

El flujo no termina al extraer datos. Un análisis útil requiere seleccionar, contextualizar, evaluar, mitigar y verificar.

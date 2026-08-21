# Reto: clasificador de exposición

Extiende el análisis para que el programa no se limite a listar metadatos, sino que los clasifique de acuerdo con su posible nivel de exposición.

## Requerimiento

El programa debe producir una salida semejante a:

```text
=== EVALUACIÓN DE METADATOS ===

[BAJA ] Model            -> contexto técnico
[MEDIA] DateTimeOriginal -> información temporal
[ALTA ] GPS              -> ubicación geográfica
```

## Condiciones

1. Define al menos tres niveles: `BAJA`, `MEDIA` y `ALTA`.
2. Incluye como mínimo fabricante/modelo, fecha/hora y GPS.
3. Justifica en comentarios por qué asignaste cada nivel.
4. No asumas que un campo es siempre crítico: explica qué papel juega el contexto.
5. Añade una recomendación final sobre si la imagen debería publicarse tal como está.

## Pregunta de cierre

**¿Eliminar todos los metadatos antes de publicar un archivo es siempre la mejor decisión? Responde sí, no o depende, y argumenta tu respuesta.**

Pista: considera trazabilidad, archivo histórico, gestión documental y publicación externa.

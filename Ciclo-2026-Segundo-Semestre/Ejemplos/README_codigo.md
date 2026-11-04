# Código ejecutable

El script [`ejecutar_ejemplos.py`](./ejecutar_ejemplos.py) ejecuta las partes cuantitativas que requieren procesamiento y guarda cada salida en su semana:

- **S3:** total y participación de ventas por región y diagnóstico de Occidente contra su inventario.
- **S4:** media móvil, tendencia lineal y estimación estacional para enero de 2027.
- **S10:** agregación por segmento y conversión del CRM a GeoJSON para cargarlo en herramientas GIS.

Solo requiere Python 3.9 o posterior y la biblioteca estándar. Desde esta carpeta:

```powershell
python .\ejecutar_ejemplos.py
```

Los archivos generados aparecen en `S3`, `S4` y `S10`. S2, S5, S6, S8, S9, S11 y S12 son ejercicios de diseño, documentación o configuración de plataformas externas; sus resultados están en `S#\resultado.md`. S7 y S10 incluyen además diagramas editables `.drawio`.

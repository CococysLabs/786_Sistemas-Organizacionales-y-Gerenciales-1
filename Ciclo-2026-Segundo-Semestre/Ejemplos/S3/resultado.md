# S3 — Análisis descriptivo y diagnóstico de ventas

## KPI del semestre

- **Ventas totales:** Q2,318,200.
- **Región líder:** Central, Q957,600 (41.3 % del total).
- **Región con caída:** Occidente, de Q103,900 en abril a Q65,800 en junio.

## Ventas por región

| Región | Ventas semestre | Observación |
|---|---:|---|
| Central | Q957,600 | Crecimiento estable |
| Occidente | Q541,600 | Caída en mayo-junio |
| Oriente | Q478,800 | Crecimiento estable |
| Norte | Q340,200 | Crecimiento estable |

## Diagnóstico de Occidente

| Mes | Ventas | Inventario final |
|---|---:|---:|
| Abr | Q103,900 | 1,680 |
| May | Q72,000 | 210 |
| Jun | Q65,800 | 150 |

La caída de abril a junio es **Q38,100 (36.67 %)** y coincide con el desplome del inventario de 1,680 a 150 unidades. El diagnóstico es quiebre de inventario, no una menor capacidad comercial de la región.

## Decisión y seguimiento

1. Reubicar inventario disponible desde Central hacia Occidente antes del siguiente ciclo de reposición.
2. Definir un punto de reorden regional y alerta cuando el inventario sea menor al mínimo.
3. Revisar semanalmente ventas, inventario final y días de cobertura por región.

El detalle calculado queda en `S3_resumen.csv`.

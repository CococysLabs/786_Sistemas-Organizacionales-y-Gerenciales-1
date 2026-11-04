# S10 — Integración CRM-GIS

## Resumen calculado del CRM

| Segmento | Clientes | Ventas trimestre |
|---|---:|---:|
| Mayorista | 3 | Q149,100 |
| Horeca | 3 | Q46,500 |
| Minorista | 4 | Q23,500 |
| **Total** | **10** | **Q219,100** |

## Resultado del mapa

- Marcadores: los 10 clientes del CSV, coloreados por `Segmento`.
- Mayoristas prioritarios para la ruta: Supermercado La Económica (Zona 1), Comercial San Cristóbal (Mixco) y Distribuidora del Sur (Villa Nueva).
- Ruta propuesta: **Zona 1 → Mixco → Villa Nueva**; después se atienden los puntos Horeca y Minorista según capacidad.
- Ventas de mayoristas: **Q149,100**, equivalentes al 68.05 % del trimestre.

El diagrama de integración está en [`integracion.drawio`](./integracion.drawio). El mapa se puede reproducir importando `clientes_crm.csv` en Google My Maps, usando Latitud/Longitud para posición y Nombre para título.

## Integración automatizada

`CRM — API/iPaaS — normalización y validación — GIS — SCM (rutas, entregas e inventario)`. Una exportación CSV es una importación manual; un cliente nuevo solo llega automáticamente mediante API o iPaaS.

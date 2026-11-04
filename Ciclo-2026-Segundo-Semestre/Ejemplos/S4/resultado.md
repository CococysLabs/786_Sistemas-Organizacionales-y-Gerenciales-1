# S4 — Proyección de demanda y conocimiento explícito

## Serie preparada

Se agreg— `Periodo` de 1 a 24 a `demanda_historica.csv`. Enero de 2026 corresponde al periodo 13 y enero de 2027 al periodo 25.

## Pronósticos para enero de 2027

| Método | Fórmula equivalente | Resultado |
|---|---|---:|
| Media móvil de 3 meses | PROMEDIO(1164, 1279, 1414) | **1,286 unidades** |
| Tendencia lineal | PRONOSTICO.LINEAL(25; periodos 1:24; unidades 1:24) | **1,247 unidades** |
| Estacional | 891 — (ventas 2026 / ventas 2025) | **1,056 unidades** |

El crecimiento anual calculado es **18.54 %**. La media móvil arrastra el pico de noviembre-diciembre y la tendencia lineal tampoco modela la caída de enero. Se selecciona la estimación estacional de **1,056 unidades**, validándola contra capacidad, inventario y costo de sobrantes.

## Ficha de lección aprendida

- **Problema:** los pronósticos basados solo en experiencia provocaron faltantes en diciembre de 2025 y sobrantes en enero.
- **Datos:** 24 meses de ventas del ERP, con periodos 1-24.
- **Métodos:** media móvil, tendencia lineal y comparación estacional interanual.
- **Resultado:** 1,286, 1,247 y 1,056 unidades, respectivamente.
- **Método elegido:** estacional, porque conserva el patrón de enero y ajusta el crecimiento anual.
- **Recomendación:** usar 1,056 como base, revisar semanalmente pedidos e inventario y recalcular con cada cierre mensual.

El detalle queda en `S4_pronoséticos.csv`.

# S7 — Mapa de sistemas para expansión internacional

## Arquitectura resultante

- **Nube central:** ERP global (finanzas, inventario, producción), CRM global (clientes) y plataforma colaborativa.
- **Canal global e-business:** tienda en línea con pagos internacionales conectada al CRM y ERP.
- **Países:** Guatemala, México y El Salvador; cada uno contiene ventas, bodega y finanzas conectadas al ERP/CRM.
- **Flujos:** pedidos, clientes, inventario, facturas y reportes consolidados.

El diagrama editable está en [`mapa.drawio`](./mapa.drawio).

## Matriz de desafíos

| Desafío | Ejemplo | Mitigación |
|---|---|---|
| Normativas fiscales | FEL en Guatemala y CFDI en México | Localización fiscal del ERP por país |
| Interoperabilidad | Sistemas locales distintos | APIs, catálogo común y pruebas de integración |
| Cultura e idioma | Procedimientos diferentes | Capacitación, responsables locales y gestión del cambio |
| Seguridad de datos | Accesos desde varios países | MFA, mínimo privilegio, cifrado y auditoría |

**Impacto cultural esperado:** pasar de áreas y países aislados a procesos compartidos, con autonomía local para la normativa y visibilidad global para la gerencia.

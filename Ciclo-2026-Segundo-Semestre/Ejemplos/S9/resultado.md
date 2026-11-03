# S9 — Riesgos éticos y accesos del ERP

## Matriz de riesgos

| Dato | Sistema actual | Acceso hoy | Acceso ERP | Riesgo ético | Protección |
|---|---|---|---|---|---|
| Salario | Nomina | RR. HH. | RR. HH. y Gerencia | Violación de privacidad | RBAC, MFA, auditoría |
| Cuenta bancaria del empleado | Nomina | RR. HH. y pagos | RR. HH. y tesorería autorizada | Fraude o exposición financiera | Cifrado, enmascaramiento y doble aprobación |
| Historial de compras del cliente | Facturación | Facturación | Ventas; solo agregados para gerencia | Uso sin consentimiento y perfilamiento | Finalidad limitada, consentimiento y auditoría |
| NIT del cliente | Facturación | Facturación | Ventas y contabilidad | Exposición de identificador fiscal | Validación de finalidad y acceso por rol |
| Existencias | Inventario | Bodega | Bodega, compras y gerencia | Manipulación o decisiones erróneas | Segregación, bitácora y conciliación |
| Precios de costo | Inventario | Compras y gerencia | Compras y Gerencia | Revelación de secreto comercial | Campo restringido y reportes agregados |

## Matriz de accesos (mínimo privilegio)

| Dato | RR. HH. | Ventas | Bodega | Gerencia |
|---|---|---|---|---|
| Salario | Sí | No | No | Sí, solo autorizado |
| Cuenta bancaria | Sí | No | No | No, salvo tesorería autorizada |
| Historial de compras | No | Sí | No | Sí, agregado |
| NIT del cliente | No | Sí | No | Sí |
| Existencias | No | Consulta | Sí | Sí |
| Precios de costo | No | No | No | Sí |

## Reglas antes de migrar

1. Todo acceso se asigna por rol, con mínimo privilegio, MFA y revisión trimestral.
2. Cada consulta o exportación de datos sensibles se registra con usuario, fecha, finalidad y resultado de la revisión.
3. No se crean algoritmos o campañas con historial de clientes sin validar finalidad, consentimiento, sesgo y aprobación de privacidad.

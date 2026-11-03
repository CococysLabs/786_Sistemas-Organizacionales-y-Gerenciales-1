# S11 — Arquitectura en tres capas y ciclo de vida

## Arquitectura elegida

Se elige **tres capas** sobre microservicios: pocos usuarios, equipo pequeño, requerimientos estables, complejidad baja y escalabilidad suficiente para una facultad. El diagrama editable está en [`arquitectura.drawio`](./arquitectura.drawio).

| Capa | Componentes | Responsabilidad |
|---|---|---|
| Presentación | Web adaptable para estudiantes; panel del personal | Reservar, consultar disponibilidad y operar desde navegador |
| Lógica | Servicios de reservas, préstamos y notificaciones | Reglas, máximo tres libros por estudiante y recordatorios |
| Datos | PostgreSQL/MySQL con libros, usuarios y préstamos | Persistencia, integridad y respaldos |

## Plan del ciclo de vida

| Etapa | Entregable | Herramienta |
|---|---|---|
| Planeación | Alcance, presupuesto y riesgos | Documento de proyecto |
| Análisis | Requisitos y casos de uso | Historias/casos de uso |
| Diseño | Arquitectura, modelo de datos y prototipo | Draw.io, UML |
| Desarrollo | Código por capas y migración inicial | Git, IDE, framework web |
| Pruebas | Casos funcionales, integración y seguridad | PHPUnit/Jest, Postman |
| Implementación | Despliegue, capacitación y manual | CI/CD, servidor cloud |
| Mantenimiento | Correcciones, métricas y respaldos | Monitorización y mesa de ayuda |
| Retiro | Exportación/archivo de datos y apagado seguro | Plan de retiro y respaldo |

Metodología: **cascada**, porque los requisitos son estables y se necesita documentación formal; cada fase se aprueba antes de pasar a la siguiente.

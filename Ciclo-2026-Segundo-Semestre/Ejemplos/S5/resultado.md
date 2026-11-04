# S5 — Base de conocimiento para soporte técnico

## Configuración de la base

Base: **Base de Conocimiento - Soporte**. Propiedades: `Problema` (título), `Categoría` (Accesos/Red/Hardware/Software), `Etiquetas`, `Autor`, `Última revisión` y `Estado` (Borrador/Validado). Vista creada: **Por categoría**, con búsqueda por título y etiquetas.

## Artículos validados

### Usuario no puede conectarse a la VPN
- **Categoría:** Red | **Etiquetas:** VPN, autenticación, acceso | **Autor:** Ana López | **Revisión:** 2026-11-02 | **Estado:** Validado
- **Síntoma:** error de autenticación al conectar la VPN.
- **Causa:** contraseña expirada o perfil VPN desactualizado.
- **Solución:** 1) confirmar identidad; 2) restablecer contraseña; 3) volver a importar el perfil; 4) probar conexión; 5) registrar el cierre.
- **Cómo evitarlo:** alertar antes del vencimiento y mantener el perfil publicado en una ubicación controlada.

### Usuario bloqueado por intentos fallidos
- **Categoría:** Red | **Etiquetas:** VPN, autenticación, acceso | **Autor:** Ana López | **Revisión:** 2026-11-02 | **Estado:** Validado
- **Síntoma:** error de autenticación al conectar la VPN.
- **Causa:** bloqueo por intentos fallidos.
- **Solución:** validar identidad, desbloquear desde el directorio, forzar cambio de contraseña y documentar el ticket.
- **Cómo evitarlo:** activar MFA, política de contraseñas y capacitación contra reutilización.

### Impresora de red no imprime
- **Categoría:** Red | **Etiquetas:** VPN, énticación, acceso | **Autor:** Ana López | **Revisión:** 2026-11-02 | **Estado:** Validado
- **Síntoma:** error de énticación al conectar la VPN.
- **Causa:** cola detenida o conexión al servidor de impresión.
- **Solución:** comprobar conectividad, reiniciar cola, validar controlador y enviar página de prueba.
- **Cómo evitarlo:** mantener controlador aprobado y revisar consumibles preventivamente.

## Indicadores

- Tiempo promedio de resolución = minutos totales de tickets recurrentes / tickets recurrentes cerrados.
- Porcentaje resuelto con artículo = tickets resueltos usando artículo / tickets recurrentes cerrados — 100.
- Objetivo inicial: reducir 40 % el tiempo promedio en 30 días.

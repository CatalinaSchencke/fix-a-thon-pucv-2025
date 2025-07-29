# Notas de Deployment

- Usar Python 3.8+
- Base de datos: MySQL o SQLite
- Puerto por defecto: 5000
- Memoria recomendada: 512MB

## Problemas conocidos
- A veces falla el login
- Los precios se calculan mal con descuentos mayores al 50%
- No usar DELETE en producción (borra todo)
# ShopManager Pro v2.3.1

## 📋 Descripción del Proyecto

ShopManager Pro es nuestro sistema de gestión de inventario para nuestra tienda online. Maneja aproximadamente 500 productos y ha sido el corazón de nuestras operaciones durante los últimos 2 años.

## 🎯 Solicitud de Mejoras

Hemos estado experimentando algunos desafíos operacionales y necesitamos ayuda para mejorar nuestro sistema. Como empresa en crecimiento, queremos asegurar que nuestro código esté preparado para el futuro y sea más fácil de mantener.

### Situación Actual

Nuestro equipo ha reportado algunos inconvenientes durante el uso diario:

- **Rendimiento**: El sistema se vuelve lento cuando hay varios usuarios trabajando simultáneamente
- **Confiabilidad**: Ocasionalmente perdemos información de productos durante las actualizaciones
- **Mantenimiento**: Agregar nuevas funcionalidades toma más tiempo del esperado
- **Escalabilidad**: Nos preocupa cómo se comportará el sistema cuando crezcamos más

### Lo que Funciona Bien

- ✅ El sistema está operativo y cumple su función básica
- ✅ Tenemos datos históricos valiosos
- ✅ Los usuarios conocen la interfaz actual
- ✅ Procesa las transacciones diarias sin problemas mayores

## 🚀 Instalación y Configuración

### Requisitos
- Python 3.8+
- Dependencias listadas en `requirements.txt`

### Pasos para Ejecutar

1. **Clonar el repositorio**
   ```bash
   git clone https://github.com/CatalinaSchencke/fix-a-thon-pucv-2025.git
   cd shop_manager_v2.3.1
   ```

2. **Instalar dependencias**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configurar variables de entorno**
   ```bash
   cp .env.example .env
   # Editar .env con tus configuraciones
   ```

4. **Ejecutar el sistema**
   ```bash
   ./run.sh
   # o alternativamente:
   python src/main.py
   ```

5. **Acceder al sistema**
   - URL: `http://localhost:5000`
   - Usuario admin: `admin` / `admin123`

## 📁 Estructura del Proyecto

```
shop_manager_v2.3.1/
├── config/          # Configuraciones del sistema
├── docs/            # Documentación disponible
├── src/             # Código fuente principal
├── data/            # Archivos de datos y logs
├── tests/           # Tests unitarios
├── requirements.txt # Dependencias Python
├── .env.example     # Plantilla de configuración
└── run.sh          # Script de inicio
```

## 🔧 Funcionalidades Actuales

### API Endpoints Disponibles

- **GET /products** - Listar todos los productos
- **POST /products** - Crear nuevo producto
- **PUT /products/<id>** - Actualizar producto existente
- **DELETE /products/<id>** - Eliminar producto
- **POST /login** - Autenticación de usuarios
- **POST /calculate** - Cálculo de precios con descuentos

### Características del Sistema

- **Gestión de Inventario**: CRUD completo de productos
- **Autenticación**: Sistema básico de usuarios y roles
- **Cálculo de Precios**: Manejo de descuentos y precios finales
- **Persistencia de Datos**: Almacenamiento en archivos JSON/CSV y base de datos
- **Logging**: Registro de transacciones importantes

## 🎯 Objetivos de Mejora

Buscamos que profesionales revisen nuestro código y nos ayuden a:

1. **Optimizar el rendimiento** general del sistema
2. **Mejorar la confiabilidad** de las operaciones
3. **Facilitar el mantenimiento** futuro del código
4. **Preparar el sistema** para mayor carga de usuarios
5. **Implementar mejores prácticas** de desarrollo

## 📊 Datos de Prueba

El sistema incluye datos de ejemplo para facilitar las pruebas:

- **Productos**: Variedad de artículos con diferentes categorías y precios
- **Usuarios**: Cuentas de prueba con diferentes roles
- **Logs**: Registro de transacciones históricas

## 🔍 Áreas de Enfoque Sugeridas

Sin entrar en detalles técnicos específicos, creemos que estas áreas podrían beneficiarse de atención:

- **Organización del código** y estructura de archivos
- **Validación de datos** de entrada y salida
- **Gestión de errores** y casos excepcionales
- **Documentación** del código y APIs
- **Configuración** del entorno y despliegue
- **Testing** y cobertura de pruebas

## 📝 Entregables Esperados

Al final del proceso, esperaríamos recibir:

1. **Código mejorado** con las optimizaciones implementadas
2. **Documentación actualizada** de los cambios realizados
3. **Recomendaciones** para futuras mejoras
4. **Explicación** de las decisiones técnicas tomadas

## 🤝 Cómo Contribuir

1. Revisar el código existente y identificar oportunidades de mejora
2. Implementar las mejoras manteniendo la funcionalidad actual
3. Asegurar que el sistema siga funcionando correctamente
4. Documentar los cambios realizados

## 📞 Contacto

Para dudas sobre el funcionamiento del sistema o clarificaciones sobre los requerimientos, contactar al equipo organizador del evento.

---

**Nota**: Este sistema está en uso productivo, por lo que cualquier mejora debe mantener la compatibilidad con las funcionalidades existentes. El objetivo es evolucionar el código, no reescribirlo completamente.
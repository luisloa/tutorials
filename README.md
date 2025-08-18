# Prueba Técnica 

- Sistema Operativo
El proyecto se montó sobre un sistema operativo basado en Unix, específicamente la distribución Debian 12 con entorno de escritorio Xfce. Esta elección garantiza estabilidad, seguridad y un entorno ampliamente compatible con Odoo.

# Entorno
 
El proyecto se desplegó en un entorno basado en Docker, utilizando dos contenedores principales:

- Contenedor de aplicación: encargado de alojar todos los recursos necesarios para ejecutar Odoo.

- Contenedor de base de datos: dedicado a PostgreSQL, gestor recomendado oficialmente por Odoo.

Implementar contenedores desde la fase de desarrollo aporta varias ventajas:

- Similitud con producción: en muchos casos, Odoo también se implementa en entornos contenerizados en producción.

- Portabilidad: al estar encapsulado en Docker, el proyecto puede ejecutarse en cualquier host, independientemente del sistema operativo, simplemente clonando el código y levantando los contenedores.

- Seguridad: la comunicación entre contenedores se realiza mediante la red interna de Docker utilizando DNS, lo cual reduce la superficie de exposición y posibles filtraciones externas.

# Tiempo de Desarrollo
En la primera etapa se invirtieron aproximadamente 3.5 horas, durante las cuales se realizaron las siguientes actividades:

- Lectura y análisis de los requisitos de la prueba técnica.

- Revisión de la documentación oficial de Docker y Odoo.

- Descarga de los repositorios necesarios.

- Preparación del entorno de desarrollo.

- Pruebas de ejecución de los contenedores, validando que Odoo y la base de datos funcionaran correctamente.

# Problemas enfrentados y solución

- Problema

La documentación de Docker describe de forma clara cómo crear imágenes, contenedores y volúmenes. Sin embargo, al trabajar directamente con el repositorio oficial de Odoo clonado desde GitHub, la documentación no especifica cómo debe adaptarse el archivo docker-compose.yml a esa estructura particular.

En consecuencia, los volúmenes definidos en el docker-compose.yml de ejemplo presentan limitaciones:

- El código fuente de Odoo se encuentra en /odoo dentro del contenedor, y no en ./addons.

- Los módulos personalizados, en este caso, se ubican en /tutorials, y no en odoo-web-data.

- Esto provoca que los volúmenes apunten a directorios incorrectos, impidiendo que Odoo detecte los módulos y configuraciones personalizadas.

- Solución

La solución consistió en redefinir los volúmenes dentro del docker-compose.yml, apuntando a las rutas correctas del repositorio clonado:
        
     volumes:
      - ./odoo:/odoo
      - ./tutorials:/tutorials
      - ./odoo/odoo.conf:/etc/odoo/odoo.conf

Con este ajuste, Odoo logró reconocer tanto su código fuente como los módulos personalizados y la configuración.
La principal dificultad fue detectar la causa inicial del problema, ya que en un inicio Odoo simplemente no arrancaba, lo que requirió un proceso de depuración para identificar que la raíz del error estaba en la definición de los volúmenes.

# Enlace al video de demostración

En el siguiente enlace se puede visualizar un video donde se expone el entorno en funcionamiento, ejecutándose correctamente en el puerto 70.

Nota: Debido a que el proyecto está desplegado en un entorno contenerizado con Docker, es necesario acceder utilizando la dirección 0.0.0.0 para visualizar la aplicación desde el host.

https://www.youtube.com/watch?v=5nvOuuUlBzw&ab_channel=LuisLoa

# Nota
Debido al tamaño del entorno completo de Odoo, en el repositorio únicamente se incluye el directorio tutorial, dentro del cual se encuentra tutorial/estate.
Este directorio contiene el proyecto desarrollado en cumplimiento con los requerimientos establecidos en la prueba técnica.
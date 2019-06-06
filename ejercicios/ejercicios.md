

## Ejercicio 1

- Ir a https://elpais.com
- Seleccionar un artículo
  - https://elpais.com/politica/2019/06/03/actualidad/1559578563_330390.html
- Extraer el titular y mostrarlo por pantalla
  - Podemos usar el atributo: articulo-titulo
- Siguiente paso:
  - Extraer el cuerpo
  - Eliminar la publicidad



## Ejercicio 2

- Sobre esa página de artículo del país,
  - Extraer todos los links y mostrarlos por pantalla



## Ejercicio 3

- Sobre esa página de artículo del país
  - Extraer todas las imágenes y guardarlas en disco duro



## Ejercicio 4

- Sobre esa página de artículo del país
  - En vez de usando requests, usando **urllib**
  - Descargar algo, por ejemplo todos los párrafos y mostrarlos por pantalla



## Ejercicio 5

- Sobre la página https://www.jotdown.es buscar un artículo
  - Descargar un par de artículos



## Ejercicio 6

- Ir a una página de un artículo de jotdown, por ejemplo: https://www.jotdown.es/2019/05/la-ultima-palabra/
  - De esa coger todos los artículos relacionados e ir saltando a cada uno
    - Desa coger todos los artículos relacionados e ir saltando a cada uno
      - ...etc
      - (Si ya he estado antes en un artículo, no volver a él, pasar al siguiente)



## Libre

Ir a la página de thomann: https://www.thomann.de/es/sets_de_bateria.html

Y extraer todos los artículos de batería, almacenarlos en un diccionario con:

- Nombre del artículo
- Precio

- Los enlaces de las baterías están el div con la clase results
- La última página está descrita en la página
- Puedo usar requests para mandar los parámetros de la página, que las páginas se mandan como parámetros en el header. requests me escapa los ampersands
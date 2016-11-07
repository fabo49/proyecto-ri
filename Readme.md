# Proyecto de Recuperación de la Información

Este repositorio contiene el proyecto del curso CI-2414 de la Universidad de Costa Rica.

El proyecto consta de 3 secciones que se iran trabajando a lo largo del curso.

## Requerimientos

Para el correcto funcionamiento del sistema es necesario que instale los siguientes módulos de Python:

```bash
    $ sudo pip install stop-words
    $ sudo pip install -U nltk
    $ sudo pip install beautifulsoup4
    $ sudo pip install lxml
    $ sudo pip install scrapy
    $ sudo pip install Flask
```

## Primera parte

El objetivo de esta tarea es desarrollar y configurar los elementos básicos para la construcción de índices en
un motor de búsqueda para la Web.

El sistema a desarrollar consta de tres módulos:

1. Araña. Un bot de Internet que navega por la WWW para descargar documentos con el propósito de
indexarlos.
2. Preprocesamiento lingüístico. Incluye tokenizar, parsear y normalizar los términos de los documentos a
indexar.
3. Desarrollo y construcción de índices. Desarrollo tanto de las estructuras de datos para contener el
diccionario y las listas de postings, como los algoritmos para la construcción de los índices (por
ejemplo, BSBI y SPIMI). Además, estos índices deben ser dinámicos, es decir, permitir la inserción de
nuevos registros en el diccionario y las listas de postings de forma dinámica. Los estudiantes deben
priorizar (y demostrar) la escalabilidad del modelo, estructuras y algoritmos, aunque las colecciones
utilizadas sean de tamaño relativamente pequeño.

### Experimentos

Cada grupo debe preparar, implementar y documentar al menos cuatro experimentos (mínimo uno para el
módulo 1, uno para el módulo 2 y dos para el módulo 3). Estos experimentos consisten en evaluar resultados
haciendo cambios en las propiedades o configuración del sistema. Ejemplos de experimentos: evaluar
diferencias en tiempo de indexación y tamaño de los índices cuando se eliminan stopwords, comparar la
eficiencia del sistema cuando se usa BSBI o cuando se usa SPIMI, usar árboles o tablas hash para construir el
diccionario, comparar diferentes políticas de crawling para las arañas, entre otros.
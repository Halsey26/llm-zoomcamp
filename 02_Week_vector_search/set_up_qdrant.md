# Set up - Qdrant

Vamos a corre Qdrant dentro de un contenedor de Docker:

## Pasos 

### Docker

Terminal en la dirección de la carpeta donde estes trabajando:
1. Hacemos pull de la imagen de qdrant y corremos el contenedor:

```
docker pull qdrant/qdrant
```
```
docker run -p 6333:6333 -p 6334:6334 \
   -v "$(pwd)/qdrant_storage:/qdrant/storage:z" \
   qdrant/qdrant
```
La línea de ``` -v "$(pwd)...``` permite que la data sea persistente. Si se reinicia o se elimina el contenedor, seguirá almacenada localmente.

2. Después estará habilitada en http://127.0.0.1:6333/dashboard

### Instalación de librerías

```
pip install -q "qdrant-client[fastembed]>=1.14.2"
```
O si lo ejecutas dentro de un jupyter notebook:
```
!python -m pip install -q "qdrant-client[fastembed]>=1.14.2"
```

- El paquete `qdrant-client`: es para usar el cliente oficial de Python, también se puede usar con otros clientes oficiales(JavaScript/TypeScript, Go y Rust).  
- El paquete `fastembed`: permite realizar los embeddings (representaciones vectoriales de data) 
---
Listo! Ya tienes instalado todo lo necesario para empezar a usar Qdrant.


En este notebook usaremos VectorSearch con Qdrant [vector_search_qdrant.ipynb]()

--- 

## Conceptos Previos para empezar con Qdrant

1. Points (puntos)
   - Definición: entidad fundamental de Qdrant.
   Se podría pensar que cada punto es un registro de un dato que se va a **indexar** y **buscar**
   - Componentes:
      - ID: es el identificador único de cada punto.

      - Vector: componente principal de un punto. Es la representación numérica (generada por el modelo de embeddings entonces es una representación vectorial) que permite capturar la semántica de los datos.

      - Payload(opcional): Es un objeto que permite almacenar los metadatos o info estructurada. Su uso principal es para filtros o para ordenar resultados de la búsqueda. 
      Tipo de datos que puede almacenar: boolean, fechas, ubicaciones geográficas o objetos anidados.

   Entonces para resumir un punto se define como P(ID, Vector, Payload)

2. Collection ( Colección) 
   - Definición: Una colección es un conjunto de puntos que pertenecen a un dominio, problema o contexto de un negocio (sistema de recomendación de películas).


      Piensa en una colección como un contenedor donde se almacenan y gestionan varios puntos y dentro de este contenedor puedes realizar las búsquedas semánticas.

   - Ventaja: permite segmentar la información. Se puede crear colecciones diferentes para productos, usuarios, documentos, etc. Facilitando las búsquedas.


3. Tipo de vectores en Qdrant

   Qdrant soporta diferente tipo de vectores, según la naturaleza de los datos y los requerimientos para búsqueda y exploración.
   - Dense Vector (vectores densos): son los más comunes, vectores de alta dimensionalidad generados por embeddings. 

   - Sparse Vector (vectores disperos): se caracterizan por tener valores 0 en mayoría de posiciones del vector. Solo algunos índices tienen valor significativo. <p>
   Ej de uso: cuando se tiene una alta dimensionalidad pero muy pocos elementos aportan valor.

   - Multivectors: permite almacenar y trabajar con múltiples vectores para un solo puno.

   - Named vectors: tienen un nombre asignado.   

|
Para más información, consultar: [Documentación Qdrant](https://qdrant.tech/documentation/concepts/)
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




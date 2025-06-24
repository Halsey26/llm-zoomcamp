# 📘 Apuntes – Semana 2

## 0. Conceptos claves

### Indexar
Indexar los documentos **significa** almacenar los embeddings junto con metadatos 
Permite realizar la búsqueda más rápida.

## 1. ¿Qué son los Embeddings?

- Son representaciones vectoriales de datos (texto, imagen, video, etc)
- Se utiliza técnicas de aprendizaje automático.
- Capturan las características semánticas (el significado de un texto)

## 2. Vector Search
Mide la distancia entre el vector del query y los vectores de los documentos.
A diferencia de la técnica TF-IDF que buscaba por coincidencia de palabras. 
Modulo 1, se especificaba los campos claves.
Por vector search se busca por **proximidad de vectores**.

Ventaja sobre **TF-IDF**
En vez de realizar búsqueda indicando las palabras exactas, Vector search permite comprender el 
significado de los documentos sin importan si son entre mismo tipo(imagen, video, texto) o ente diferentes.

Hablar: sobre las dificultades de los vectores
La alta dimensionalidad, hace que los vectores sean pesados 

## 3. Qdrant
Qdrant es una base de datos vectorial open-source especializada en almacenamiento y búsqueda de vectores.
Está diseñada para ser escalable, que siempre esté disponible y que devuelva resultados de manera rápida aunque las búsquedas
sean pesadas.

Ventajas como Vector Database:
- Rápida
- Precisa
- Fácil de integrar

### FLujo 
El flujo típico es:
1. Generar embeddings
2. Crear un índice en Qdrant
3. Insertar vectores + metadatos
4. Hacer consultas de similaridad


Notas:
- realizar comparación con tf-idf
- 

### Pasos realizados en este módulo
1. Setup de Qdrant en un contenedor docker e instalación de librerías en el enviorement [set_up_qdrant.md]()

2. Primeros pasos para utilizar Vector Search con Qdrant [vector_search_qdrant.ipynb]()
    - Importanción de librerias
    - Almacenamiento del dataset a trabajar
    - Análisis de dataset: estructura, tipo de data, etc
    - Se definen los campos para semantic search y para almacenar en la metadata
    - 

3. 

## Recursos

- [Ventajas vector_search]()
- [Modulo 2 - LLM Zoomcamp](https://github.com/DataTalksClub/llm-zoomcamp/tree/main/02-vector-search)
- [Notebook sematic_search](https://github.com/DataTalksClub/llm-zoomcamp/blob/main/02-vector-search/sematic_search.ipynb)
- [¿Porqué Qdrant?](https://qdrant.tech/articles/dedicated-vector-search/)
- [Documentación Qdrant](https://qdrant.tech/documentation/concepts/)
- [Documentación FastEmbed](https://github.com/qdrant/fastembed)
- [Documentación del modelo usado para embedding](https://huggingface.co/jinaai/jina-embeddings-v2-small-en)
# 📘 Apuntes – Semana 2

## 0. Conceptos claves

### Indexar
Indexar los documentos **significa** almacenar los embeddings junto con metadatos 
Permite realizar la búsqueda más rápida.

## 1. ¿Qué son los Embeddings?

- Son representaciones vectoriales de datos (texto, imagen, video, etc)
- Capturan las características semánticas 

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
1. Setup de Qdrant en un contenedor docker [set_up_qdrant.md]()

## Recursos

- [Ventajas vector_search]()
- [Modulo 2 - LLM Zoomcamp](https://github.com/DataTalksClub/llm-zoomcamp/tree/main/02-vector-search)
- [Notebook sematic_search](https://github.com/DataTalksClub/llm-zoomcamp/blob/main/02-vector-search/sematic_search.ipynb)
- [Porqué Qdrant?](https://qdrant.tech/articles/dedicated-vector-search/)
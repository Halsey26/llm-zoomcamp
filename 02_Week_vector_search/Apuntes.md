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
significado de los documentos.

## 3. Qdrant
Qdrant es una base de datos vectorial open-source especializada en almacenamiento y búsqueda de vectores.
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

## Recursos

- [Ventajas vector_search]()
- [Modulo 2 - LLM Zoomcamp]()
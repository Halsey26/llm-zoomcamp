# 📘 Apuntes – Módulo 2

## 0. Conceptos claves

### Indexar
Indexar los documentos **significa** almacenar los embeddings junto con metadatos 
Permite realizar la búsqueda más rápida.

## 1. ¿Qué son los Embeddings?

- Son representaciones vectoriales de datos (texto, imagen, video, etc)
- Se utiliza técnicas de aprendizaje automático.
- Capturan las características semánticas (el significado de un texto)

## 2. Vector Search
Técnica de búsqueda que mide la distancia entre el vector del query y los vectores de los documentos.
A diferencia de la técnica TF-IDF que buscaba por coincidencia de palabras. 
Modulo 1, se especificaba los campos claves.
Por vector search se busca por **proximidad de vectores**.

Ventaja sobre **TF-IDF** <p>
En vez de realizar búsqueda indicando las palabras exactas, Vector search permite comprender el significado de los documentos sin importan si son del mismo tipo de data(imagen, video, texto) o ente diferentes tipos de datos.

Tip: sobre las dificultades de los vectores
La alta dimensionalidad, hace que los vectores sean pesados y por ello es necesario un sistema de almacenamiento => *Qdrant*

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
Previo:
1. Entender la naturaleza de la data
2. Seleccionar el modelo más adecuado de embedding

Con Qdrant:
1. Generar embeddings
2. Crear un **índice** en Qdrant
3. Insertar vectores + metadatos
4. Hacer consultas de similaridad

Notas:
- realizar comparación con tf-idf

---
## Pasos realizados en este módulo
0. Conceptos Claves (embedding, vector search)
1. Setup de Qdrant en un contenedor docker e instalación de librerías en el enviorement. Con un resumen de conceptos previos. [set_up_qdrant.md](https://github.com/Halsey26/llm-zoomcamp/blob/main/02_Week_vector_search/set_up_qdrant.md)

2. Primeros pasos para utilizar Vector Search con Qdrant [vector_search_qdrant.ipynb](https://github.com/Halsey26/llm-zoomcamp/blob/main/02_Mod_vector_search/vector_search_qdrant.ipynb)
    - Importanción de librerias.
    - Creación del cliente con qdrant.
    - Almacenamiento del dataset a trabajar.
    - Análisis de dataset: estructura, tipo de data, etc
    - Se definen los campos para semantic search y para almacenar en la metadata.
    - Evaluación y selección de modelo de embedding en base a los campos definidos.
    - Configuración con Qdrant
        * Se crea la colección
        * Creación e inserción de puntos en la colección
        * Visualizamos la colección actualizada en Qdrant http://127.0.0.1:6333/dashboard
    - Búsqueda por similitud Qdrant.
    - Búsqueda por similitud usando filtros.
3. RAG con Vector Search [rag_vector_search](https://github.com/Halsey26/llm-zoomcamp/blob/main/02_Mod_vector_search/rag_vector_search.ipynb)

[Homework](https://github.com/Halsey26/llm-zoomcamp/blob/main/02_Mod_vector_search/Homework2.ipynb)

## Recursos

- [Modulo 2 - LLM Zoomcamp](https://github.com/DataTalksClub/llm-zoomcamp/tree/main/02-vector-search)
    - [Notebook sematic_search](https://github.com/DataTalksClub/llm-zoomcamp/blob/main/02-vector-search/sematic_search.ipynb)
    - [Notebook rag](https://github.com/DataTalksClub/llm-zoomcamp/blob/main/02-vector-search/rag.ipynb)
    - [Notebook hybrid_search](https://github.com/DataTalksClub/llm-zoomcamp/blob/main/02-vector-search/hybrid_search.ipynb)


- [¿Porqué Qdrant?](https://qdrant.tech/articles/dedicated-vector-search/)
- [Documentación Qdrant](https://qdrant.tech/documentation/concepts/)
- [Documentación FastEmbed](https://github.com/qdrant/fastembed)
- [Documentación del modelo usado para embedding](https://huggingface.co/jinaai/jina-embeddings-v2-small-en)
- [What is a vector database?](https://qdrant.tech/articles/what-is-a-vector-database/)
- [Filtros Qdrant](https://qdrant.tech/articles/vector-search-filtering/)
- [Vector Search manuals](https://qdrant.tech/articles/vector-search-manuals/)
- [Building a RAG System with GPT-4: A Step-by-Step Guide](https://medium.com/@mayssamayel4/building-a-rag-system-with-gpt-4-a-step-by-step-guide-291711342f0d)
- [Vector Search](https://lancedb.github.io/lancedb/concepts/vector_search/)
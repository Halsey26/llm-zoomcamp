# 📘 Apuntes – Semana 1

## 1. ¿Qué es un LLM?

Los LLM (Large Language Models) son modelos entrenados con grandes cantidades de texto para generar y comprender lenguaje natural. Voy usar el llm GPT de OpenAI.

## 2. ¿Qué es RAG (Retrieval-Augmented Generation)?

Un sistema RAG se basa en buscar información relevante para dársela al modelo antes de que genere la respuesta. Esto permite respuestas más precisas y actualizadas.

### 🔁 Flujo de un sistema RAG:
1. El usuario hace una pregunta
2. El sistema busca en una base de datos/documentos
3. Se selecciona el texto más relevante
4. Se construye un prompt: contexto + pregunta
5. Se envía al LLM y se genera la respuesta

## 3. Implementación del motor de búsqueda (`minsearch.py`)

Esta archivo implementa un motor de búsqueda usado en las primeras clases. Se detalla de manera general como usarlo:
- Se define una clase **Index** y se inicializa con
    - text_fields, keyword_fields
- Funciones que se pueden aplicar a un objecto de la clase ```Index```
    - fit(), 



Si deseas conocer 
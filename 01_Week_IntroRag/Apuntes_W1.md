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

Esta archivo implementa un motor de búsqueda usado en las primeras clases. 
Se utiliza la búsqueda tradicional o Minsearch, se basa en:
- TF-IDF: 
Técnica de *NLP* donde se evalúa el `peso` de cada palabra que pertenece a un documento.

- Similitud de coseno: Evalúa similitud de vectores a través del ángulo entre ellos.

Archivo [minsearch.py]() 

## 4. Prompt Engineering básico

Un LLM necesita contexto, en este caso se desarrolla un prompt con la instrucción, pregunta o query y contexto(o información).

```
INTRUCCIÓN: Eres un asistente ...

QUERY: {query}
CONTEXT: {context}
```

## 5. Modularización

Se modularizó por las siguientes funciones:
- Busqueda por index `busqueda`
- Ordena documentos (section, question, text) y generación del prompt `build_prompt`
- Generación del ouput `chat_llm`

Finalmente, todo se construyó en una función final `rag`:
- Parámetros de entrada: query, course
- Retorna: La respuesta del llm



---
**Recursos Adicionales:**
- [ Apuntes TF-IDF]() 
- [Método TF-IDF - Youtube](https://www.youtube.com/watch?v=CBKT-dVnrQo&ab_channel=C%C3%B3digoEspinoza-AutomatizatuVida)
- [Repo Minsearch](https://github.com/alexeygrigorev/minsearch/tree/main) de Alexey Grigorev-Fundador de DataTalskClub
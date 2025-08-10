
# Evaluación de sistemas de recuperación
*Evaluation metrics for retrieval*

Este módulo abarca la importancia de evaluar resultados de recuperación de información en sistemas RAG. Aunque existen distintias técnicas de recuperación (MinSearch, ElasticSearch, VectorSearch), hay que compararlas de manera objetiva para evaluar cuál es mejor para determinado caso.

---
##  Ground Truth
Es el conjunto de datos "correctos" o esperados que usamos como referencia para evaluar si es sistema está funcionando bien.

En el contexto de Retrieval, Ground Truth contiene:
- Una query (pregunta)
- Conjunto de documentos que pueden ser recuperados (respuestas más relevantes)

### Ejemplo de 'ground truth'
- `Query: "¿Puedo unirme al curso después de haber empezado?"`
- Documentos relevantes: 
    - doc1: `Yes, even if you don't register, you're still eligible to submit the homeworks. `
    - doc10: `Yes, we will keep all the materials after the course finishes, so you can follow the course at your own pace after it finishes.`

Tu sistema de recuperación debería ser capaz de encontrar esos documentos.

---

Entonces, 
**¿Por qué necesitamos evaluar?**
- Depende del dataset se puede obtener diferentes resultados aplicando diferentes técnicas.
- Porque se necesita una forma objetiva para comparar el performance entre técnicas.

**¿Qué necesitamos para evaluar?** <p>
Un conjunto de datos con **ground truth** (también llamado gold standard) y [métricas de evaluación](https://github.com/Halsey26/llm-zoomcamp/blob/main/03_Mod_Evaluation/search_evaluation/metricas_evaluacion.md)

**¿Cómo se usa el Ground Truth?**
- Ejecutas el sistema de búsqueda escogido.
- Se compara los documentos que retorna con los que debería retornar según el `ground truth`
- Se usan métricas de evaluación para cuantificar el rendimiento.

**¿Cómo se genera el ground truth?** <p>
Se puede generar manualmente o usando LLM como evaluador(lo que se aplicará en este módulo). 

## Recursos para profundizar

- [How to Evaluate RAG If You Don’t Have Ground Truth Data](https://medium.com/data-science/how-to-evaluate-rag-if-you-dont-have-ground-truth-data-590697061d89)
- [Retrieval-augmented Generation (RAG) evaluators](https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/evaluation-evaluators/rag-evaluators)
- [Evaluation Metrics for Retrieval-Augmented Generation (RAG) Systems
](https://www.geeksforgeeks.org/nlp/evaluation-metrics-for-retrieval-augmented-generation-rag-systems/)
- 
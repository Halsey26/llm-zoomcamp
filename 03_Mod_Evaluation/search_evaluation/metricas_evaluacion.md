# Métricas de evaluación de recuperación

1. **Precision at k (P@k)**:
   - Measures the number of relevant documents in the top k results.
   - Formula: `P@k = (Number of relevant documents in top k results) / k`

2. **Recall**:
   - Measures the number of relevant documents retrieved out of the total number of relevant documents available.
   - Formula: `Recall = (Number of relevant documents retrieved) / (Total number of relevant documents)`

3. **Mean Average Precision (MAP)**:
   - Computes the average precision for each query and then averages these values over all queries.
   - Formula:  `MAP = (1 / |Q|) * Σ (Average Precision(q))` for q in Q

4. **Normalized Discounted Cumulative Gain (NDCG)**:
   - Measures the usefulness, or gain, of a document based on its position in the result list.
   - Formula: `NDCG = DCG / IDCG`
     - `DCG = Σ ((2^rel_i - 1) / log2(i + 1))` for i = 1 to p
     - `IDCG` is the ideal DCG, where documents are perfectly ranked by relevance.

5. ♦️ **Mean Reciprocal Rank (MRR)**:
    *Evaluates the rank position of the first relevant document.*
   
   - ¿Qué mide?

      Evalúa la posición de ranking (o qué tan arriba) se encuentra el primer documentos relevante en los resultados para cada consulta (query).

   - Fórmula:

      $MRR= \frac{1}{|Q|} \sum_{i=1}^{Q} \frac{1}{rank_i} $

      - |Q| = número total de consultas
      - ${rank_i} $ = la posición del primer documento relevante para query_i

      ## Ejemplo 
      Se realizan 3 consultas.

      | Query | Resultados ordenados                                | Primer relevante está en posición | Reciprocal Rank |
      | ----- | --------------------------------------------------- | --------------------------------- | --------------- |
      | Q1    | \[irrelevante, ✅relevante, irrelevante] → pos **2** | 2                                 | 1/2 = 0.5       |
      | Q2    | \[✅relevante, irrelevante, irrelevante] → pos **1** | 1                                 | 1/1 = 1.0       |
      | Q3    | \[irrelevante, irrelevante, ✅relevante] → pos **3** | 3                                 | 1/3 ≈ 0.333     |

      Entonces: 
         $MRR= (0.5+1+0.33) = 0.611$
         
      **Interpretación**
      - Cuanto más cerca del top esté el primer resultado relevante, mayor será el MRR.
      - El máximo valor de MRR es 1.0 (si siempre está en la primera posición).
      - Es sensible al orden exacto.


6. **F1 Score**:
   - Harmonic mean of precision and recall.
   - Formula: `F1 = 2 * (Precision * Recall) / (Precision + Recall)`

7. **Area Under the ROC Curve (AUC-ROC)**:
   - Measures the ability of the model to distinguish between relevant and non-relevant documents.
   - AUC is the area under the Receiver Operating Characteristic (ROC) curve, which plots true positive rate (TPR) against false positive rate (FPR).

8. **Mean Rank (MR)**:
   - The average rank of the first relevant document across all queries.
   - Lower values indicate better performance.

9. ♦️ **Hit Rate (HR) or Recall at k**:
   - Measures the proportion of queries for which at least one relevant document is retrieved in the top k results.
   - Formula: `HR@k = (Number of queries with at least one relevant document in top k) / |Q|`

   - ¿Qué mide?

      Evalúa cuantas querys tienen al menos 1 resultado relevante en el top *k* posiciones.

   - Fórmula:
      
      HR=número de querys con al menos 1 resultado relevante en el top_k/ |Q|

   ## Ejemplo  (k=3)
      Se realizan 3 consultas.

      | Query | Top-3 Resultados                        | ¿Hay relevante en top-3? |
      | ----- | --------------------------------------- | ------------------------ |
      | Q1    | \[irrelevante, ✅relevante, irrelevante] | ✅ Sí                     |
      | Q2    | \[✅relevante, irrelevante, irrelevante] | ✅ Sí                     |
      | Q3    | \[irrelevante, irrelevante, ✅relevante] | ✅ Sí                     |

   Entonces: 
      $HR@3 = 3/3 = 1$
   
   En el caso que una query, por ejemplo Q3, no tuviera relevante en el top 3, entonces: <p>
   - $HR@3 = 2/3 = 0.66$
        
   **Interpretación**
   - HR@k no le importa en qué lugar exacto dentro del top k está el relevante, solo le interesa si existe uno.
   - Es más indulgente que MRR.
   - Muy útil si el sistema debe “acertar al menos una vez”.

10. **Expected Reciprocal Rank (ERR)**:
    - Measures the probability that a user finds a relevant document at each position in the ranked list, assuming a cascading model of user behavior.
    - Formula: `ERR = Σ (1 / i) * Π (1 - r_j) * r_i` for j = 1 to i-1
      - Where `r_i` is the relevance probability of the document at position i.
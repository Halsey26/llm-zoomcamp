
## 0. Conceptos Claves

**Desventajas con otros métodos:**
El método de conteo, es un método donde la asignación del valor depende la frecuencia de la palabra y por ende de su importancia **pero** no toma en consideración la relevancia de las palabras en sí. 
Por ejemplo:
-  Palabras como el, la, los, si, etc. Pueden aparecer múltiples veces pero pueden no tener significancia para el modelo. Aún así, esta técnica les asginaría un peso alto.

### Stop Words
- Son palabras comunes: si, la, el, etc.
- Como se ha mencionado, si se dejan puede sesgar el análsis
- Lo recomendable es eliminarlas, mejorando la precisión. Sin embargo se tendría que analizar el objetivo del modelo si se realiza un análsis de sentimientos, la palabra `no` puede influir significativamente en el contexto.

### Documentos

### Chunk

## 1. Teoría de TF-IDF 
- TF(Term frequency): frecuencia de una palabra en un documento.
- IDF(Inverse Document Frequency): Evalua la rareza la aparición de un término en la colección de documentos. Por ejemplo:
    - Si un término aparece en **muchos** documentos => IDF baja
    - Si un término es poco común => IDF alta

Entonces, ¿qué es el método **TF-IDF**? 
Es una técnica o método de conteo que nos permite evaluar si un término tiene mayor relevancia en un documento de una colección.

¿Cómo funciona?
- Cada palabra o término en un documento se le asigna un puntaje en función de su frecuencia en **ese** documento.
- 



## 2. Similitud de cosenos



## 3. Aplicación en minsearch.py




Se detalla de manera general como usarlo:
- Se define una clase **Index** y se inicializa con
    - text_fields, keyword_fields
- Funciones que se pueden aplicar a un objecto de la clase ```Index```
    - fit(), 


## Recursos

[Método TF-IDF](https://www.youtube.com/watch?v=CBKT-dVnrQo&ab_channel=C%C3%B3digoEspinoza-AutomatizatuVida)
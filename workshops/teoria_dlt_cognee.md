
# 📘 Apuntes – Workshop 1

Estos son conceptos previos 

--- 
## Data Load Tool - dlt

`dlt` Es una librería open-source de Python diseñada para facilitar la construcción de pipelines ETL de forma sencilla y modular.

¿Qué hace *dlt*?
- **Extract**, obtiene datos de múltiples fuentes (APIs, base de datos, archivos csv, json, etc)
- **Transform**, transforma, limpia y normaliza los datos antes de cargarlos.
- **Load**, Carga los datos a diferentes destinos (DuckDB, BigQuery, etc)
- Maneja esquemas, estado y carga incremental

---
### Características claves

✅ Soporte para esquemas: Detecta y valida estructuras de datos automáticamente.

✅ Carga incremental: Solo actualiza los datos nuevos o modificados.

✅ Control de estado: Guarda el estado del pipeline para reinicios seguros.

✅ Transparente y reproducible: Puedes revisar y auditar lo que se carga en cada paso.

✅ Modular y extensible: Puedes construir pipelines complejos de forma progresiva.

---
## ¿Qué es cognee?
Cognee transforma tus datos en knowledge graph a diferencia de usar vector database

Permite: 
- Añadir data estructurada u no estructurada
- Construir automaticamente un knowledge graph
- Preguntar en lenguaje natural y recibir respuestas robustas


notas para averiguar: Entiendo que puede haber relaciones por grafos, pero esencialmente que representa un grafo? 

##








## Recursos

- [Workshop - LLM Zoomcamp](https://www.youtube.com/watch?v=MNt_KK32gys&ab_channel=DataTalksClub%E2%AC%9B)
- [Dlt repo oficial](https://github.com/dlt-hub/dlt)
- [Moving Data with Python and dlt: A Guide for Data Engineers](https://www.datacamp.com/tutorial/python-dlt)
- [Cognee](https://www.youtube.com/watch?v=1bezuvLwJmw)
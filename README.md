## CMAPPS Research

El siguiente proyecto contempla investigación de distintos algoritmos utilizando CMAPPS Dataset.

El proyecto actualmente considera un modelo baseline que es una Regresión Logística automatizado con DVC.

El proyecto considera lo siguiente:

```shell
        +-----------+     
        | featurize |     
        +-----------+     
         **        **     
       **            *    
      *               **  
+-------+               * 
| train |             **  
+-------+            *    
         **        **     
           **    **       
             *  *         
        +----------+      
        | evaluate |      
        +----------+      
+-----------------------+  
| assets/CMAPSSData.dvc |  
+-----------------------+
```
El problema se está modelando como un problema de RUL con las siguientes 3 Etapas:
  * **Featurize**: Con la creación de los Features a Utilizar.
  * **Train**: Con el proceso de entrenamiento del modelo utilizando 5-Fold Cross Validation + Retraining.
  * **Evaluate**: Se está midiendo el resultado del Modelo en Dataset de Test con métricas de MAE, RMSE y R2.


Actualmente el proyecto aborda el Dataset FD0001 que constituye fallas para 100 motores con sólo un modo de falla. A medida que se vaya iterando se irán utilizando versiones con mayor complejidad dentro del Dataset.

## Reproducibilidad del Proyecto

Para poder chequear los resultados actuales del modelo se recomienda Clonar el repo y luego ejecutar:

```python
$ dvc pull
$ dvc repro
$ dvc metrics show 
```
Esto ejecutará sólo los cambios del proceso y mostrará metricas de Validación (5-Fold CV) y Test (Datos no vistos provistos en el mismo CMAPPS).




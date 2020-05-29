# Python Test

## Run

`python main.py
`
## Descripción de solución

Para la solución actual se utilizo un algoritmo asignando un peso a cada variable.

Para las variables de CurrentRole, Country, Industry se utilizaron listas mientras que para las variables de NumberOfRecommendations, NumberOfConnections se utilizaron sus valores (el 10% del valor en caso de la ultima variable).

Se calculó un score para cada persona y luego se seleccionaron los top 100.

## ¿Cómo mejorarías el algoritmo?
Para empezar realizaría una análisis estadístico sobre los datos existentes para determinar el pedo de cada variable y de igual manera determinar la probabilidad de acuerdo a ciertos valores (en la solución actual se toma la misma probabilidad para todos los países de la lista mientras que después del análisis cada país tendría una probabilidad distinta según el histórico).


## ¿Qué otra información sobre las personas te sería útil para mejorar tu algoritmo?

* Arraigo laboral
* Tiempo de la empresa
* Ingreso
* Número de contactos que trabajan en empresas que ya adquirieron los servicios de BairesDev



# Taller Análisis de Datos con Pandas

Este proyecto analiza un conjunto de datos sobre crímenes, identificando patrones y generando estadísticas relevantes utilizando la biblioteca Pandas de Python.

### Taller Nuevas Tecnologías Cesde - Globant Dual 2024
#### Jhony Alexis Martinez

## Preguntas y Respuestas

### 1. Listar las primeras cinco ciudades con el mayor número de agencias
- Respuesta: Se agrupan las agencias por ciudad y se cuentan, listando las cinco ciudades con más agencias.

### 2. Listar los estados más afectados por crímenes perpetrados por mujeres
- Respuesta: Se filtran los datos por crímenes cometidos por mujeres y se cuentan los casos por estado, listando los cinco estados más afectados.

### 3. Listar los estados más afectados por crímenes perpetrados por hombres
- Respuesta: Similar al punto anterior, pero filtrando por crímenes cometidos por hombres.

### 4. Determinar el número exacto de crímenes hechos por mujeres de raza Asian/Pacific Islander
- Respuesta: Se filtran los datos por mujeres de raza Asian/Pacific Islander y se cuenta el número de crímenes.

### 5. Determinar el número exacto de hispanos que han asesinado mediante la estrangulación
- Respuesta: Se filtran los datos por hispanos y por el uso de la estrangulación como arma, contando el número de casos.

### 6. Determinar el tipo de relación más peligrosa, el cual comete más homicidios con arma de tipo Shotgun (escopeta)
- Respuesta: Se agrupan los datos por tipo de relación y se cuenta el uso de escopetas, determinando cuál relación tiene más casos.

### 7. ¿Cuál es el sexo que más homicidios ha cometido con veneno (Poison)?
- Respuesta: Se filtran los datos por el uso de veneno y se cuentan los homicidios por género, identificando el género más común en estos casos.

### 8. ¿Cuántos asesinos de raza negra atrapó el FBI?
- Respuesta: Se filtran los datos por raza negra y casos resueltos, contando el número de perpetradores atrapados.

### 9. ¿Cuál es el total de homicidios desde el año 1995 hasta el año 2000 perpetrado por hombres de raza negra por sofocación (Suffocation)?
- Respuesta: Se filtran los datos por hombres de raza negra, sofocación como arma y el rango de años, contando el número de homicidios.

### 10. Determinar los homicidios de la policía municipal de la ciudad de New York del cual hayan sido por relaciones de tipo Ex-Wife, y además que su arma haya sido la estrangulación (Strangulation)
- Respuesta: Se filtran los datos por el departamento de policía de New York, ex-esposa como relación y estrangulación como arma, contando el número de casos.

## Uso

1. Clona este repositorio.
2. Asegúrate de tener instalado Pandas.
3. Ejecuta el script para cargar y analizar los datos del archivo CSV.
4. Revisa las salidas del script para obtener respuestas a las preguntas anteriores.

## Base de Datos

Puedes descargar la base de datos desde [este enlace](https://www.kaggle.com/datasets/murderaccountability/homicide-reports/download?datasetVersionNumber=1).

## Contribuciones

Las contribuciones son bienvenidas. Por favor, abre un issue para discutir cualquier cambio importante antes de enviar un pull request.

## Licencia

Este proyecto está bajo la licencia MIT. Ver el archivo LICENSE para más detalles.

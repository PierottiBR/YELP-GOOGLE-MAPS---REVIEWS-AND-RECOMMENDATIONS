###### ![](https://github.com/arnaldoquinones/YELP-GOOGLE-MAPS---REVIEWS-AND-RECOMMENDATIONS/blob/main/MULTIMEDIA/data_devs_logo.jpg?raw=true)

### YELP &  GOOGLE-MAPS

### REVIEWS-AND-RECOMMENDATIONS

TRABAJO GRUPAL SOBRE YELP & GOOGLE MAPS - REVIEWS AND RECOMMENDATIONS

## Indice del contenido:

- [Introducción](#introducción)
- [Contexto](#contexto)
- [Desarrollo del Proyecto](#desarrollo-del-proyecto)
- [ETL](#ETL (Exploración, Transformación y Carga))
- [EDA](#EDA (Análisis Exploratorio de datos))
- [Tecnologías Utilizadas](#tecnologías-utilizadas)
- [KPIs](#kpis)
- [Análisis y Conclusiones](#análisis-y-conclusiones)
- [Recomendaciones](#recomendaciones)
- [Staff del proyecto](#Staff)

## Introducción:

En el dinámico mundo del marketing digital, la opinión de los usuarios ha emergido como un recurso invaluable. Plataformas de reseñas como Yelp y Google Maps han democratizado la voz del consumidor, permitiendo que sus experiencias sean compartidas y consultadas a gran escala. Estas reseñas no solo influyen en las decisiones de otros consumidores, sino que también proporcionan a las empresas una fuente rica y directa de feedback sobre sus servicios y productos. Yelp, una plataforma consolidada en el mercado, permite a los usuarios evaluar una amplia gama de negocios, desde restaurantes hasta hoteles, basándose en sus experiencias personales. De manera similar, Google Maps integra una robusta función de reseñas que ayuda a los usuarios a tomar decisiones informadas sobre dónde comer, comprar o alojarse.

Para las empresas, esta información es fundamental. No solo revela la percepción pública y el desempeño de los locales, sino que también destaca áreas específicas que requieren mejoras. En un entorno competitivo, comprender estas opiniones puede ser decisivo para la planificación estratégica y la optimización del servicio.

En este contexto, nuestra consultora de datos ha sido contratada por un conglomerado de empresas del sector restaurantero y de ocio en Estados Unidos. Nuestro objetivo es llevar a cabo un análisis exhaustivo de las opiniones de los usuarios en Yelp y Google Maps sobre hoteles, restaurantes y otros negocios relacionados con el turismo y el entretenimiento. Utilizando técnicas avanzadas de análisis de sentimientos y modelos de machine learning, buscamos predecir tendencias de crecimiento y declive en estos sectores. Además, nuestro análisis ayudará a identificar ubicaciones óptimas para nuevos locales y desarrollará un sistema de recomendación personalizado que mejorará la experiencia del usuario al descubrir nuevos lugares basados en sus preferencias previas.

Para lograr estos objetivos, recopilaremos y procesaremos datos de múltiples fuentes, creando una base de datos integral que servirá como el núcleo de nuestro análisis. Esta base de datos incluirá tanto información estática como datos obtenidos a través de APIs y scrapping. A partir de estos datos, realizaremos análisis detallados para identificar relaciones y factores clave que influyan en las percepciones y decisiones de los consumidores.

## Contexto:

El sector de la restauración es uno de los más dinámicos y competitivos dentro de la industria del turismo y el ocio. La proliferación de plataformas de reseñas como Yelp y Google Maps ha transformado la manera en que los consumidores eligen dónde comer. Estas plataformas permiten a los usuarios compartir sus experiencias y opiniones sobre los restaurantes que visitan, creando una vasta base de datos de feedback valioso. Este fenómeno ha cambiado las reglas del juego para los restaurantes, que ahora deben prestar una atención meticulosa a las opiniones de sus clientes para mantenerse competitivos y relevantes.

En Yelp, los usuarios pueden evaluar y comentar sobre sus experiencias en una amplia variedad de restaurantes, desde pequeños establecimientos locales hasta cadenas internacionales. Las reseñas incluyen detalles sobre la calidad de la comida, el servicio, el ambiente, y la relación calidad-precio, entre otros aspectos. Google Maps, por su parte, no solo facilita la localización de restaurantes, sino que también integra un sistema de reseñas similar que ayuda a los usuarios a decidir dónde comer basándose en las experiencias previas de otros clientes.

Para los restaurantes, estas reseñas representan una mina de oro de información. Analizar estas opiniones permite a los propietarios y gerentes entender cómo los clientes perciben su oferta, identificar puntos fuertes y débiles, y tomar decisiones informadas para mejorar su servicio y atraer a más comensales. Por ejemplo, una tendencia negativa en las reseñas sobre la calidad del servicio puede llevar a una capacitación adicional del personal, mientras que comentarios positivos sobre un plato específico pueden influir en el diseño del menú.

Además, estas plataformas no solo afectan a los consumidores locales, sino que también influyen en los turistas que buscan experiencias gastronómicas en nuevas ciudades. Las decisiones de dónde comer durante un viaje a menudo se basan en las reseñas encontradas en Yelp y Google Maps, lo que significa que un restaurante bien valorado puede atraer a una clientela diversa y aumentar significativamente su visibilidad y reputación.


## Desarrollo del Proyecto

El proyecto se desglosa en varias fases para abordar el análisis del mercado de restaurantes utilizando datos de Yelp y Google Maps, empleando tecnologías de Google Cloud y un diagrama de Gantt para la planificación y seguimiento del proyecto:

- **Extracción, Transformación y Carga (ETL)**: Los datos de reseñas de restaurantes se extraen de las plataformas Yelp y Google Maps. Utilizando Google Cloud Storage para almacenamiento y Google Cloud Dataflow para el procesamiento, estos datos son transformados y cargados en una base de datos central en Google BigQuery para su posterior análisis. Este proceso incluye la limpieza y normalización de datos, garantizando su calidad y coherencia.

- **Análisis Exploratorio de Datos (EDA)**: Se emplean herramientas como Pandas, Numpy, Seaborn y Matplotlib para examinar patrones, relaciones y tendencias en los conjuntos de datos. Google Cloud Datalab se utiliza para el análisis interactivo y visualización de datos. Se identifican variables cruciales, tales como calificaciones promedio, frecuencia de reseñas, términos recurrentes en los comentarios y ubicaciones geográficas destacadas, que serán fundamentales para el análisis posterior.

- **Elaboración del Tablero de Control en Power BI**: Se elabora un tablero de control interactivo en Power BI que resalta análisis clave según variables temporales, ubicación geográfica, categoría del restaurante, y aspectos específicos mencionados en las reseñas. Este tablero se conecta a Google BigQuery para asegurar que los datos estén actualizados y accesibles en tiempo real, permitiendo visualizar las tendencias y relaciones descubiertas durante el EDA, facilitando la toma de decisiones informadas.

- **Desarrollo del Diagrama de Gantt**: Un diagrama de Gantt será desarrollado usando Google Sheets o Microsoft Project para planificar y seguir el progreso del proyecto. Este diagrama detallará las tareas y subtareas de cada fase del proyecto, asignando fechas de inicio y fin, así como recursos y dependencias, asegurando una gestión eficiente del tiempo y los recursos.

- **Definición de KPIs y Conclusiones**: Se definen Indicadores Clave de Desempeño (KPIs) relevantes para el sector restaurantero, tales como la satisfacción del cliente, la frecuencia de visitas, y la calidad del servicio. Se presentan conclusiones y sugerencias para mejorar las estrategias de marketing y operaciones de los restaurantes, así como recomendaciones sobre las mejores ubicaciones para abrir nuevos establecimientos y estrategias para mejorar la experiencia del cliente.

# Pipeline y Stack Tecnológico

Para implementar el proyecto, se utilizarán las siguientes tecnologías y herramientas:

- **Python**: Herramientas y bibliotecas como Pandas, Numpy, Matplotlib y Seaborn serán utilizadas para la manipulación, análisis y visualización de datos.
- **Datasets**: Los datos de Yelp y Google Maps serán manejados en formatos como JSON, PKL, y convertidos a Parquet para eficiencia.
- **Data Warehouse**: Google Cloud Storage se utilizará para el almacenamiento de datos y Google BigQuery para el análisis y consulta de grandes volúmenes de datos.
- **Visualización**: Power BI se utilizará para la creación de tableros interactivos. Streamlit será utilizado para crear aplicaciones web de visualización de datos personalizadas y dinámicas.
- **Modelos de Machine Learning**: Se utilizarán Scikit-Learn y TensorFlow para el desarrollo y entrenamiento de modelos de machine learning que ayudarán a predecir tendencias y hacer recomendaciones.

# Diagrama de Gantt

El diagrama de Gantt para el proyecto incluirá las siguientes fases y tareas:

1. **Preparación**
   - Recolección de requisitos (1 semana)
   - Configuración de Google Cloud Environment (1 semana)

2. **ETL**
   - Extracción de datos de Yelp (2 semanas)
   - Extracción de datos de Google Maps (2 semanas)
   - Transformación y limpieza de datos (3 semanas)
   - Carga de datos en Google BigQuery (1 semana)

3. **EDA**
   - Análisis de patrones y tendencias (2 semanas)
   - Identificación de variables cruciales (1 semana)

4. **Elaboración del Tablero de Control**
   - Diseño del tablero en Power BI (2 semanas)
   - Integración de datos en tiempo real (1 semana)
   - Pruebas y ajustes del tablero (1 semana)

5. **KPIs y Conclusiones**
   - Definición de KPIs (1 semana)
   - Análisis y presentación de conclusiones (2 semanas)

6. **Cierre del Proyecto**
   - Revisión final y entrega del proyecto (1 semana)
   - Capacitación y soporte post-implementación (2 semanas)

Este enfoque estructurado asegura que cada fase del proyecto contribuya de manera significativa a la comprensión y mejora del mercado de restaurantes, proporcionando a nuestros clientes insights valiosos y herramientas prácticas para optimizar sus operaciones y estrategias de marketing.
  
##  ETL (Exploración, Transformación y Carga)
En la fase inicial, se llevó a cabo el proceso de exploración, transformación y carga de datos de los respectivos dataframes para prepararlos de manera óptima para el análisis:

- Normalización de los nombres de las columnas para garantizar consistencia en los registros.
- Adecuación de los tipos de datos de las columnas para facilitar su manipulación y análisis.
- Identificación y eliminación de registros duplicados para mantener la integridad de los datos.
- Creación de nuevas columnas para almacenar las coordenadas, extrayéndolas de otra columna existente.
- Generación de una nueva columna que indique fecha y hora de ingreso de cada comensal.
- Evaluación de la presencia de valores nulos para tomar medidas correctivas cuando sea necesario.
- Creación de una columna que clasifique a las víctimas en rangos etarios, con el fin de facilitar un análisis más detallado y específico.
  
## EDA (Análisis Exploratorio de datos)
Después de completar la limpieza de los conjuntos de datos, se llevó a cabo el Análisis Exploratorio de Datos (EDA). Este proceso implicó la elaboración de gráficos y visualizaciones con el objetivo de investigar y comprender las estadísticas, identificar valores atípicos y orientar investigaciones futuras.


## Tecnologías Utilizadas

El proyecto hace uso de diversas tecnologías y herramientas para realizar un análisis exhaustivo de los siniestros viales. Algunas de las principales tecnologías utilizadas incluyen:

- [![Visual Studio Code](https://img.shields.io/badge/IDE-Visual%20Studio%20Code-blue)](https://code.visualstudio.com/)
- [![Jupyter](https://img.shields.io/badge/Notebook-Jupyter-orange)](https://jupyter.org/)
- [![Pandas](https://img.shields.io/badge/Library-Pandas-brightgreen)](https://pandas.pydata.org/)
- [![Matplotlib](https://img.shields.io/badge/Library-Matplotlib-blue)](https://matplotlib.org/)
- [![Seaborn](https://img.shields.io/badge/Library-Seaborn-yellow)](https://seaborn.pydata.org/)
- [![Folium](https://img.shields.io/badge/Library-Folium-green)](https://python-visualization.github.io/folium/)
- [![GitHub](https://img.shields.io/badge/Platform-GitHub-lightgrey)](https://github.com/)
- [![Git](https://img.shields.io/badge/Version%20Control-Git-blue)](https://git-scm.com/)
- [![Power BI](https://img.shields.io/badge/BI%20Tool-Power%20BI-yellow)](https://powerbi.microsoft.com/)

## KPIs

1. KPI DE CRECIMIENTO:
Definición: Mide el crecimiento en la cantidad de reseñas recibidas por los restaurantes en un periodo determinado.
Fórmula: (Número de reseñas en el periodo actual - Número de reseñas en el periodo anterior) / Número de reseñas en el periodo anterior.
Objetivo: Evaluar el crecimiento en popularidad y visibilidad de los restaurantes a lo largo del tiempo con una esperanza de crecimiento del 8%. Un índice de crecimiento positivo indica un aumento en la atención de los clientes.

2. KPI DE APROBACION:
Definición: Mide el sentimiento general (positivo, negativo o neutral) de las reseñas de los usuarios.
Fórmula: Media ponderada de las calificaciones y sentimiento promedio de las reseñas.
Objetivo: Identificar el sentimiento general hacia los restaurantes y detectar áreas de mejora, con una esperanza positiva anual del 10% . Un sentimiento positivo indica satisfacción del cliente, mientras que un sentimiento negativo sugiere problemas a abordar.

3. KPI PRECIO:
Definición: Evaluación de la relación entre el precio promedio de los platos y la satisfacción del cliente (calificación y sentimiento de las reseñas).
Cálculo: Relación entre el precio promedio de los platos (extraído de menús o reportes) y la calificación promedio de las reseñas. Se puede utilizar una métrica como (Precio Promedio / Calificación Promedio) para evaluar esta relación.
Objetivo: Determinar cómo el precio impacta la percepción de los clientes sobre la calidad del servicio y la comida. Este KPI ayuda a identificar si los precios son percibidos como justos y adecuados por los clientes.


## Análisis y Conclusiones:



## Recomendaciones:

## Staff:

- Pierotti Braulio (Data Analist) Proyect Leader.
- Leandro Funes (Data Scientist)
- Acuña Roman (Data Engineer)
- Mamani Aldo Federico (Data Engineer)
- Quiñones Arnaldo Pedro (Data Analist)

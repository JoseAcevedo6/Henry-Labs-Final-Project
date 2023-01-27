<p align=center><img src=https://d31uz8lwfmyn8g.cloudfront.net/Assets/logo-henry-white-lg.png><p>

# <h1 align=center> **PROYECTO FINAL ** </h1>

##### - ANGEL ZAVALETA 
##### - JOSÉ ACEVEDO 
##### - LEONARDO CUETO
##### - NICOLÁS LIRA

# <h1 align=center>**`OLIST`**</h1>


## **Introducción**

La parte de Business Analytics es una de las más importantes dentro de todo el mundo del procesamiento de datos, 
justo en este parte comienza en Analisis Exploratiorio de Datos a tomar forma, para poder ir sacando conclusiones a medida que nos vamos adentrando en los Datasets

## **Propuesta de trabajo**

En 2021, la venta minorista de productos a través de e-commerce significó un saldo aproximado de 5.2 trillones de dólares en todo el mundo y se infiere que dicha cifra aumentará un 56% en los próximos años, llegando a los 8.1 trillones en 2026.

Olist es una compañía brasileña prestadora de servicio e-commerce para PYMES que funciona como un marketplace, es decir, funciona como “tienda de tiendas” donde diferentes vendedores pueden ofrecer sus productos a consumidores finales.

## **Rol a desarrollar**

Con el objetivo primordial de seguir conectando a pequeñas empresas (PYMES) con mercados más grandes y mejorar la experiencia del usuario, Olist los contrata como consultores externos para encontrar soluciones innovadores que permitan a sus usuarios vender sus productos a un mayor número de clientes.
Para lograrlo, les disponibiliza sus datos de 2016 a 2018 con lo que deberán entregar un MVP (minimum viable product).


## Entendimiento de la situación actual

El e-commerce se refiere a la compra y venta de bienes o servicios a través de Internet. Ha crecido rápidamente en los últimos años y es ahora una parte importante de la economía mundial. El e-commerce permite a las empresas alcanzar una base de clientes más amplia y ofrece comodidad para los compradores. Además, también puede tener un menor costo operativo en comparación con una tienda física, lo que lo hace particularmente atractivo para las pequeñas empresas. Una de las formas más comunes de comercio electrónico es el comercio minorista en línea, que incluye sitios web de compras como Amazon, Alibaba, Mercadolibre, Olist, entre otros.

Una de las principales ventajas del e-commerce es la capacidad de recopilar datos sobre el comportamiento, las preferencias y los hábitos de compra de los clientes, lo que ayuda a las empresas a tomar decisiones basadas en datos y mejorar sus ofertas con el tiempo. Además, el e-commerce también proporciona una herramienta valiosa para las empresas para llegar a los clientes con el comercio transfronterizo, lo que era difícil antes de Internet.

Sin embargo, el e-commerce tiene algunos inconvenientes, como el potencial de fraude y la dificultad de construir confianza con los clientes en línea. También requiere una logística, un servicio de pago y un servicio al cliente eficiente para operar, lo que puede ser desafiante para algunas empresas manejar por sí mismas.


## Objetivos específicos del trabajo y del grupo

**KPI 1: **Calcular la variación de ventas de "categorías de productos" con respecto al mejor "score" (por mes y trimestre (2016/17 y 18)).
Objetivo: Que los productos con buen "score" tengan mejor posicionamiento en la página web (por ende aumentar las ventas).

**KPI 2: **Con respecto a los MQLs, queremos analizar si el ingreso de nuevos "MQLs" (vendedores) afecta el ingreso/venta de Olist.
Objetivo: Acortar/apresurar el tiempo de “aceptación” a Olist para generar más ingresos. (Mejorar procesos)

**KPI 3: **Identificar los productos (top 10) más vendidos por mes y trimestre por ciudad.
Objetivo: Proponer mantener ese producto en stock por ciudad y período de tiempo (mes y trimestre) para satisfacer la demanda y ahorrar en costos de envío.


## Alcance y fuera de alcance

-- Motivación del proyecto
- Ayudar a mejorar el proceso de ventas a través de un análisis de negocios basado en KPI’s para proponer a nuestro cliente una opciones de mejora en sus servicios como E-Commerce

-- Objetivos 
- Verificar la calidad de los datos y proceder con ETL
- Implementar Datawarehouse como modelo de base de datos.
- Presentar un Dashboard con indicadores de desempeño. 
- Crear una aplicación para predecir los productos en tendencia basados en un modelo de ML.


-- Supuestos
- Datasets brindan información confiable para proyección y análisis de datos.
- Tiempo suficiente para término de proyecto.
- Disponibilidad en tiempo por parte del equipo.
- Los integrantes del equipo permanezcan hasta culminación del proyecto.

-- Restricciones 
- Se debe culminar el proyecto en 3 semanas.
- Equipo de trabajo con mínimo 4 integrantes.
- Contar con los perfiles de Data Science asumiendo los roles de Analista e Ingeniería de Datos.

-- Exclusiones
-Un Dashboard, mediante el software Power BI y presentación con Streamlit.
-Datawarehouse con respaldo en GitHub, diseñado con SQLAlquemy y SQLite
-Metodología Ágil, uso de Trello como herramientas para gestión de proyectos.

-- Criterios de Aceptación
- El dashboard debe ser funcional y entendible
- Una base de datos sólida
- EDA de calidad en los entregables.

## Solución propuesta
1. Stack tecnologico

<img src="https://th.bing.com/th/id/OIP.fbVr5gXeIrChfkbOU_S3vgAAAA?pid=ImgDet&rs=1" style="width: 3vw; min-width: 100px;" />  <img src="https://th.bing.com/th/id/OIP.p9U41JwQ1DIfoRou4qIJvAHaC_?pid=ImgDet&rs=1" style="width: 5vw; min-width: 120px;" />   <img src="https://eucariotacdn.azureedge.net/wp-content/uploads/2020/01/PowerBI.jpg" alt="Image" height="80" width="80">  <img src="https://th.bing.com/th/id/R.289ed655c5900c9df33d3ba90e2b52a3?rik=WM47Wyh8ioZM%2fA&pid=ImgRaw&r=0" alt="Image" height="80" width="90">  
<img src="https://th.bing.com/th/id/OIP.8m6LjbgWmIFCteelnno2rQHaEo?pid=ImgDet&rs=1" alt="Image" height="80" width="90"><img src="https://www.01net.it/wp-content/uploads/sites/14/2021/04/streamlit-logo-300x176.png" style="width: 3vw; min-width: 100px;" /><img src="https://www.picademie.nl/wp-content/uploads/2020/11/Tkinter2.png" alt="Image" height="100" width="170"><img src="https://th.bing.com/th/id/R.f4ce6025a42918aaac87560bde710518?rik=FoEcSfIbPvRu1g&pid=ImgRaw&r=0" alt="Image" height="60" width="90" />



	Python, Pandas, Power BI, MySQL, SQLite, Streamlit, Tkinter, Sklearn

#### 2. Metodología de trabajo:
SCRUM (metodología ágil)

<img src="https://th.bing.com/th/id/OIP.Y5sAbcI4o9zQVSrvgDo7ZQHaHK?pid=ImgDet&rs=1" alt="Image" height="180" width="190">


3. Diseño detallado

4. Roles y responsabilidades

##### ANGEL ZAVALETA - Data Analyst
##### JOSÉ ACEVEDO - Data Engineer
##### LEONARDO CUETO Data Engineer
##### NICOLÁS LIRA Data Analyst

5. Cronograma general

<img src="/src/Trello.png" alt="Image" height="820" width="790" />

## **Estructura del proyecto**

El proyecto tiene 2 carpetas principales: 

1. Datasets - contiene todos los archivos csv con los que se realizó el trabajo.

2. Proyectos - contiene los dos proyectos entre los que el equio decidió cual realizar.

y los archivos

3. eda.ipynb - contieneel código generado para la realización de las tareas de la primer semana

4. E-Commerce.md - contiene la descripción del proyecto a realizar


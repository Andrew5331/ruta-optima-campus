# ruta-optima-campus

El proyecto consiste en la modelación de la Universidad de La Sabana como un grafo, con el objetivo principal de optimizar los recorridos dentro del campus universitario en función del tiempo de desplazamiento y la accesibilidad para distintos tipos de usuario, como niños, adolescentes, adultos y personas de tercera edad. En el modelo presentado, lo edificios son vértices y los caminos entre ellos son aristas ponderadas que se basan en datos como el tiempo y peso (medido en una escala de 1-5, dentro del proyecto se enfatizara más), con ajustes en los pesos según el tipo de usuario para ver reflejada la diferencia en la movilidad.

 A partir de este enfoque, se plantearon diversas problemáticas a resolver, tales como: determinar la menor distancia temporal entre dos edificios específicos para diferentes tipos de usuario, analizar cómo podría mejorarse el flujo de personas durante las horas pico, evaluar el impacto del cierre temporal de un edificio en el flujo general de tránsito y proponer optimizaciones para mejorar la eficiencia del campus. Además, se implementó un sistema que calcula la ruta más corta tomando en cuenta la accesibilidad de cada grupo, considerando las dificultades de movilidad de personas mayores o niños.
 
Para abordar estos desafíos, se desarrolló un programa en Python utilizando las bibliotecas networkx, matplotlib y streamlit, lo que permitió crear una interfaz interactiva que visualiza la red de desplazamiento dentro de la universidad. A través del uso de algoritmos sobre grafos, el sistema identifica las rutas más eficientes entre distintos puntos del campus, proporcionando una herramienta útil para la toma de decisiones en términos de movilidad, planificación espacial y la mejora de la accesibilidad en el campus.



Declaración de Propiedad y Uso
Este proyecto educativo-investigativo, desarrollado bajo el auspicio académico de la Universidad de La Sabana, se provee para acceso libre con fines estrictamente formativos y de investigación. Su contenido está protegido por las normativas de derecho intelectual de Bogotá (Decreto 622 de 2022, modificatorio de la Ley 23 de 1982) y los estatutos de propiedad intelectual de la Universidad. Queda expresamente prohibido:

Su utilización con fines comerciales o de monetización directa/indirecta

La modificación, reproducción o distribución no autorizada

Cualquier uso que vulnere los derechos morales y patrimoniales de la Universidad

Para autorizaciones excepcionales, contactar a la Oficina de Transferencia de Conocimiento de la Universidad de La Sabana.

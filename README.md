

# Web scraping



- Web crawling
  - Saltar a diferentes webs en base a los links
- Web scraping
  - Extraer info de **1** web



## Funcionamiento del protocolo http (simplificado)

- Verbos

  - GET
  - POST
  - ...

  

  ```mermaid
  graph LR
  A[Client] -->|GET HEADERS + BODY|B[Server]
B[Server] -->|RESPONSE HEADERS + BODY|A[Server]
  ```

  
  
  

## Tipos de webs

- Estáticas + (dinámica lado servidor)
- Dinámica lado cliente
  - dom (html + eventos) (vista) cambiante. 



## Herramientas básicas a construir / usar

- Básico: Librerías que combinan esas caracteríscticas: **scrapy, nutch**, jsoup (java)
  - Red -> http
    - URL lib -> un peñazo
    - requests
    - cURL
  - Extracción -> interpretar html
    - Beautiful Soap 4 -> Python
    - SXML -> LISP
  - Serializar -> (persistencia)
    - Estándar: JSON ... etc
- Extras
  - Proxy, VPN -> bloqueo de IPs ...
  - Usar navegador headless



Scrapping.org -> SASS para probar



### Herramientas developer del navegador

- Consola Javascript
  - En principio no vamos a usarlo para el scraping
- Inspector
  - Inspeccionar un cacho de la página y ver su código fuente
- Red
  - Capturar todas las peticiones, por cada una de ellas:
    - Ver cabeceras
    - Respuesta
    - Campos
    - etc
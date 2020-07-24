1. LIGRA PRO EC
     1.1 Se crea el proyecto con el comando: scrapy startproject ligrapro
     1.2 Se crea el spider con el comando: scrapy genspider ligrapro ligapro.ec
     1.3 En la página buscamos los campos que se va a analizar, en este caso: fecha, título, url.
     1.4 Inspeccionamos el XPath de estos para añadir al código de "ligrapro.py"
     
2. WALLAPOP
	 2.1 Se crea el proyecto con el comando: scrapy startproject ligrapro
     2.2 Se crea el spider con el comando: scrapy genspider ligrapro ligapro.ec
     2.3 En la página buscamos los campos que se va a analizar, en este caso: fecha, título, url.
     2.4 Inspeccionamos el XPath de estos para añadir al código de "ligrapro.py"
     
	
3. MERCADO LIBRE
   3.1 Se crea la información de 2 URL
   3.2 Se realizan filtrados de cada una de las tablas seleccionadas
   3.3 Se crean gráficos representativos de los datos filtrados
   
4. wikipedia
   4.1 se crea la conexion con la base mongodb
   4.2 se realiza la busqeuda de los campos de los cuales se requiere obtener la informacion o la lista generada.
   4.3 se crea la estructura del json y los campos que van a ir.
   4.4 se encuentra los datos y son guardados den la base de mongodb
          

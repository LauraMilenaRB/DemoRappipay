# Proyecto Demo: Generaci贸n de extractos Rappipay
Es la billetera virtual de Rappi en alianza con Davivienda, con la que puedes disfrutar la nueva forma de administrar y controlar tu dinero de manera segura, sin papeleos, 100% digital y todo desde una misma App馃摬. RappiPay vive dentro de la aplicaci贸n Rappi que est谩 disponible en App Store y Google Play.

**APP Amplify:** https://main.d18r3h05m1zwek.amplifyapp.com/
## Problema
La generaci贸n de extractos para los diferentes productos financieros es tardada, se tarda casi una hora por extracto procesados en paralelo. Se necesitan 10 horas para generar 50 mil extractos.
### Cuando se da por solucionado
Cuando se logre generar 50 mil extractos por hora con cero errores. Esto representa una reducci贸n del 80% en el tiempo de procesamiento respecto al proceso actual.
### Periodo de medici贸n: 
Mensual para todos los pa铆ses

## Dominio y linea destino de arquitectura
Para el proyecto se realizo la definicion del problema, el alcance y la identificacion base de arquitecturas de Rappipay. 
Las siguientes imagenes muestran las arquitecturas base definidas.
### Linea base: Conceptos de informaci贸n
En la siguiente diagrama tenemos los conceptos de informaci贸n relacionados al alcance del proyecto, estos conceptos son los requeridos para generar los extractos de los clientes.
Contienen informacion del contrato, rewards, detalles de movimientos, caschback e informacion adicional reqeurida.
![img_13.png](imagenes/img_13.png)

### Linea base: Mapa de aplicaciones
En el siguiente diagrama tenemos la arquitectura de aplicaciones actual que soporta el proceso de generacion de extractos y en el cual tenemos los problemas mencionados.
![img_10.png](imagenes/img_10.png)

### Linea destino: Mapa de aplicaciones 
En el siguiente diagrama tenemos la arquitectura de aplicaciones al que queremos llegar a implementar y tiene muchos de los servicios que se utilizaron en el prototipo.
![img_11.png](imagenes/img_11.png)

## Arquitectura del prototipo
![img.png](imagenes/img.png)

En la imagen anterior se muestra la arquitectura del prototipo, esta arquitectura esta dise帽ada para una soluci贸n en la nube y para este caso con el proveedor de Amazon.
En esta arquitectura se utilizan los isguientes servicios.

* **AWS Amplify:** Es un servicio que provee un conjunto de heraamientas creados espec铆ficamente para que los desarrolladores web y m贸viles de frontend puedan crear aplicaciones de pila completa en AWS de forma r谩pida y sencilla. 
  Se decide usar este servicio ya que es compatible con los leguajes, marcos y plataformas conocidos para el desarrollo web y android como JavaScript.
  ![img_4.png](imagenes/img_4.png)
* **Amazon S3:** Amazon S3 es un servicio de almacenamiento de objetos que ofrece escalabilidad, disponibilidad de datos, seguridad y rendimiento. En este servicio de almacenamiento alojamos la informacion DATA MINSAIT generada por las interfaces de minsat y los extractos generados para cada cliente por contrato.
  ![img_8.png](imagenes/img_8.png)
  ![img_9.png](imagenes/img_9.png)
* **AWS Lambda:** AWS Lambda es un servicio inform谩tico sin servidor y basado en eventos que le permite ejecutar c贸digo sin necesidad de aprovisionar servidores. En el prototipo este servicio se implemento mediante Python 3.8 con las librerias de boto3, pymongo, Jija2, weasyprint y es la pieza principal que genera el extracto bancario (pdf) con cierto template y que solo se ejecutara cuando reciba toda la informacion requerida y que sea la fecha de corte.
  ![img_5.png](imagenes/img_5.png)
* **DocumentDB:** Amazon DocumentDB es un servicio de base de datos escalable, de larga duraci贸n y completamente administrado para operar cargas de trabajo de MongoDB esenciales. 
  Este servicio se utiliza principalmente por la copatibilidad con MongoDB, se cargan la informaci贸n lista para ser usada en la cosntrucci贸n del extracto de los clientes y la informacion DATA BASICS generada por los diferentes Squads.
  ![img_6.png](imagenes/img_6.png)
* **AWS Glue:** AWS Glue es un servicio de integraci贸n de datos sin servidores que facilita la detecci贸n, preparaci贸n y combinaci贸n de datos para an谩lisis, machine learning y desarrollo de aplicaciones. En el servicio de AWS Glue alojamos el proceso de Extracci贸n, Transformaci贸n y Carga de la informaci贸n recibida por los diferentes squadas y por minsait, que compone la informaci贸n template de DATA BASICS y DATA MINSAIT.
  El template de DATA BASIC y MINSATIN esta compuesto por imformaci贸n relacionada con el cliente como el contrato, rewards, pago de movimiento, detalle de los movimientos e ifo relacionada.
  ![img_7.png](imagenes/img_7.png)
### Evidencias prototipo
![img_2.png](imagenes/img_2.png)
![img_3.png](imagenes/img_3.png)
![img_1.png](imagenes/img_1.png)
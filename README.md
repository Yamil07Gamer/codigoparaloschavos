# README LEEME

Aun tienes problemas con lo de fastapi, te dare una guia completa de que es lo que necesitas hacer paso a paso (desde el inicio).


1.- Abrir el cmd y escribir "WSL" (entrar al linux).

ejecuta el WSL y llega a la carpeta raiz de "C" con cd ..

2.- Entrar al entorno vitual que se hizo al inicio de semestre:

Debido a que este no me dio problemas a diferencia del de mitad de semestre ya que me faltaba uvicorn y no me dejaba instalarlo
recomiendo usar el entorno vitual que se hizo al inicio del semestre, si aun no tienes tu entorno ejecuta estos comandos en orden

python3 -m venv .[nombre de tu entorno]
source [nombre del entorno]/bin/activate
pip install fastapi uvicorn[standard] mysql-connector-python

3.- Descargar app:

descarga la carpeta app y guardala en la ruta del entrono virtual -> C:/poo/pooweb/app

4.- Dentro de la carpeta del entorno ejecuta el comando:

uvicorn app.main:app --reload y encomiendate a tu santo de confianza para que jale

Si no sale error ya estas del otro lado, si no

  1.- Verificar en el archivo de la carpeta db que tu usuario, contraseña y base de datos coincidan con el que tienes
    recuerda que a mediados del semestre instalamos mysql en el WSL y creamos un usuario llamado admin, si no recuerdas la contraseña del usuario que dios te bendiga

  2.- Verifica si estas una carpeta atras del app, no dentro de app, una carpeta atras

  3.- Que tu base de datos exista

  4.- Que las tablas y atributos coincidan en el archvo "/models/queries" en la insercion y busqueda de datos coincidan en nombre

  5.- No se ya deberia de funcionar XDXDXD

Si todo esta en orden al copiar y pegar en el firefox la direccion IP que te suelta uvicorn y agragar "/docs", deberian aparecer los endpoints del programa
En la terminal si exite un error al inicar el "uvicorn app.main:app --reload" te dira el error de maneta muy clara, al igual si hay un problema con la base de datos, solo leelo en ingles lit te lo dice en la cara.

Mucha suerte con el examen de mañana :)

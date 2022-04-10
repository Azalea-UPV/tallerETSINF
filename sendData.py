

"""
Para almacenar la información obtenida de los sensores hemos decidido utilizar una base de datos alojada en heroku. Para almacenar la información hemos creado una api que nos permite enviar los datos que deben ser guardados. Para esta comunicación utilizamos el protocolo http. Cada dato que recopilamos tiene su propio endPoint en la API.  Los últimos valores almacenados en la base  de datos se pueden observar en la página web: https://workshopetsinf.herokuapp.com/


"""
API_URL = "https://workshopetsinf.herokuapp.com/api/"


# La url  de la humedad es:'humidity/changeHumidityHw' y espera un método PUT
# En la api esperan que el body de la petición sea un body de la forma:
# {
#    "newValue": 20
# }
# Pista:
# · Se puede utilizar la librería request de python para realizar las peticiones http
# · https://docs.python-requests.org/en/latest/
# · Se puede usar un diccionario de python con clave "newValue" para el body del método
def humidity(value): 
    pass


# La url  de la humedad es:'/temperature/changeTemperatureHw' y espera un método PUT
# En la api esperan que el body de la petición sea un body de la forma:
# {
#    "newValue": 20
# }
# Pista:
# · Se puede utilizar la librería request de python para realizar las peticiones http
# · https://docs.python-requests.org/en/latest/
# · Se puede usar un diccionario de python con clave "newValue" para el body del método
def temperature(value):
    pass


# La url  de la humedad es:'airQuality/changeairQualityHw' y espera un método PUT
# En la api esperan que el body de la petición sea un body de la forma:
# {
#    "newValue": 20
# }
# Pista:
# · Se puede utilizar la librería request de python para realizar las peticiones http
# · https://docs.python-requests.org/en/latest/
# · Se puede usar un diccionario de python con clave "newValue" para el body del método
def airQuality(value):
    pass


switch = {

        7:humidity,
        10:temperature,
        15: airQuality,
    }


"""
En Modbus la información se guarda en direcciones de memoria. Nosotros hemos decidido relacionar cada registro con una variable, este método permite decodificar el dato recibido a que variable hace referencia.
"""
def decode(address, value):

    return switch[address](value[0])


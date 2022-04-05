

"""
Esta es la dirección base de la api donde vamos a mandar la información para almacenarla mediante peticiones http
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

def decode(address, value):
    print(f'Addres: {address}, Value: {value}')
    return switch[address](value[0])


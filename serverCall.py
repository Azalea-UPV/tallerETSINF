"""
Modbus es el protocolo de comunicaciones más extendido en la automatización industrial y el medio más común para conectar dispositivos electrónicos automatizados. En este taller lo vamos a utilizar para recopilar la información proveniente de un sensor de temperatura, humedad y CO2. ¿Tienes curiosidad de porqué hemos usado este protocolo? Acércate a preguntar.

Servidor que escucha los mensajes provenientes del PLC y los procesa.
Aquí te presentamos el código base de un servidor asíncrono de Modbus.


Enlaces de ayuda:
    ·https://pymodbus.readthedocs.io/en/latest/source/library/pymodbus.html#pymodbus-modbus-protocol-implementation
    ·https://pymodbus.readthedocs.io/en/3.0.0/source/example/modules.html
    · https://docs.python.org/3/
"""
from pymodbus.server.asynchronous import StartTcpServer
from pymodbus.datastore import ModbusSparseDataBlock
from pymodbus.datastore import ModbusSlaveContext, ModbusServerContext
from multiprocessing import Queue

import sendData


"""
En este método creamos el método que se va a activar cada vez que recibamos un dato
"""
class CallbackDataBlock(ModbusSparseDataBlock):


    def __init__(self):
                                                                    
        super().__init__({k: k for k in range(60)})

    def setValues(self, address, value):
        
        print(f" Got {value} for {address}. We start decodifyng\n")  
        sendData.decode(address,value)
        super().setValues(address, value)


def run_callback_server():

    queue = Queue()
    
    block = CallbackDataBlock()
    store = ModbusSlaveContext(di=block, co=block, hr=block, ir=block)
    context = ModbusServerContext(slaves=store, single=True)


    # --------------------------------------------------------------------------- #
    # Aquí debemos inicializar el servidor.
    # Datos a tener en cuenta:
    #   ·¿Cuál es  nuestro protocolo de comunicación?
    #   ·¿Qué información necesitamos?
    # --------------------------------------------------------------------------- #


if __name__ == "__main__":
    print('Lanzando server')
    run_callback_server()
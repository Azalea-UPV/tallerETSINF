"""
Explicacion del servidor modbus

Servidor que escucha los mensajes provenientes del PLC y los procesa.

Meter pequeña explicación de Modbus,de la diferencia entre registros y coils


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
Explicacion del callback. Se activa al recibir
"""
class CallbackDataBlock(ModbusSparseDataBlock):


    def __init__(self):
                                                                    
        super().__init__({k: k for k in range(60)})

    def setValues(self, address, value):
        
        print(f" Got {value} for {address}. We start decodifyng\n")  
        sendData.decode(address,value)
        super().setValues(address, value)


def run_callback_server():
    """
     Inicializa el almacenamiento de los datos. Ampliar explicacion
    """
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
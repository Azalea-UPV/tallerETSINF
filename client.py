from pymodbus.client.sync import ModbusTcpClient as ModbusClient

"""
Aquí te presentamos un ejemplo de cliente Modbus para que puedas probar el servidor
"""
client = ModbusClient('localhost', port=5000)
client.connect()
client.write_registers(29,True)
#client.write_coils(29,True)
client.close()

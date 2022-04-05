from pymodbus.client.sync import ModbusTcpClient as ModbusClient

"""
Explicar que hace el papel del PLC
"""
client = ModbusClient('localhost', port=5000)
client.connect()
client.write_registers(29,True)
#client.write_coils(29,True)
client.close()

#Arthur: TuTQ2

import serial.tools.list_ports

def get_ports():
    ports = serial.tools.list_ports.comports()
    comPorts = []
    numConnection = len(ports)
    for i in range(numConnection):
        strPort = str(ports[i])
        splitPort = strPort.split(' ')
        comPorts.append(splitPort[0])
    return comPorts
                    
connectPort = get_ports()
print(connectPort)
# TODO: get list of ports and try to read to volt&current -> to detect com control board
# if connectPort != 'None':
#     ser = serial.Serial(connectPort,baudrate = 9600, timeout=1)
#     print('Connected to ' + connectPort)
# else:
#     print('Connection Issue!')
# print('DONE')

import serial.tools.list_ports
ports = list(serial.tools.list_ports.comports())

for items in range(len(ports)):
	print("["+str(items)+"]   [PORT]: "+str(ports[items][0])+"; [NAME]: "+str(ports[items][1]))
portNum = input("Please select the serial port: ")
print(ports[int(portNum)][0])

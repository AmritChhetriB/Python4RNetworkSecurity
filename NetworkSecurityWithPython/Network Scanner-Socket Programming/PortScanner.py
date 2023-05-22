# Author: Amrit Chhetri, Digital Forensic Researcher
# Purpose: Network Port Scanning
# Module: Socket Programming, default
import socket
socketObj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
for port in range(60, 90):
	try:
		conObj = socketObj.connect(("192.168.3.1", port))
		if conObj==None:
			print('Port', port,'is open')
		else:
			print('Port', port,'is close')
	except:
		print(port, " is close")
		continue
	finally:
		socketObj.close()
		


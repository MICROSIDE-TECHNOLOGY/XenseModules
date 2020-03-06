import RPi.GPIO as GPIO
import serial
import time 
import numpy as np 

class TurnLed:
	''' 
	name: TurnLed
	resume: Class to take control of one led,is necesary 
	write the name of the pin in GPIO when create this object 
	'''
	
	gpio_pin=0
	status=False
	GPIO.setmode(GPIO.BOARD)

	def __init__(self,gpio_pin):
		'''Constructor  '''
		self.gpio_pin=gpio_pin
		GPIO.setup(self.gpio_pin, GPIO.OUT)

	def __del__(self):
		''' Destructor 
		Clean the pin use in the object 
		'''
		GPIO.cleanup(self.gpio_pin)

	def turnOn(self):
		''' Encender led '''

		GPIO.output(self.gpio_pin, True)  
		
		self.status=True

	def turnOff(self):
		''' Apagar led'''
		GPIO.output(self.gpio_pin, False)
		
		self.status=True
	def getStatus(self):
		return status

class Temperature:

	serial_type=""
	port_line=""
	dato=0
	salto="\n\r"

	GPIO.setmode(GPIO.BOARD)

	def __init__(self,serial_type):
		''' Constructor '''
		self.serial_type=serial_type




		if self.serial_type == 'GPIO':
			self.port_line="/dev/ttyS0"

		else:
			self.port_line="/dev/ttyACM0"

		
		try:
			self.puerto= serial.Serial(port = self.port_line, 
                         baudrate = 9600,
                         bytesize = serial.EIGHTBITS,
                         parity   = serial.PARITY_NONE,
                         stopbits = serial.STOPBITS_ONE)
		except:
			error="Error!, I have a problem when I try to create a port, maybe you do not make  a  correctly conection"
			print(error)



	def __del__(self):
		if self.serial_type == 'GPIO':
			GPIO.cleanup()

	def getValue(self):

		orden="T"
		self.puerto.write(orden.encode())
		time.sleep(0.1)
		self.puerto.write(self.salto.encode())
		time.sleep(0.1)
		self.dato = self.puerto.readline()
		self.dato = np.fromstring(self.dato.decode('ascii', errors = 'replase'), sep = ' ') 
		return str(self.dato[0]) 

class GenericSensor:

	serial_type=""
	port_line=""
	dato=0
	salto="\n\r"
	

	GPIO.setmode(GPIO.BOARD)

	def __init__(self,serial_type):
		''' Constructor '''
		self.serial_type=serial_type
		

		if self.serial_type == 'GPIO':
			self.port_line="/dev/ttyS0"

		else:
			self.port_line="/dev/ttyACM0"

		self.puerto= serial.Serial(port = self.port_line, 
                         baudrate = 9600,
                         bytesize = serial.EIGHTBITS,
                         parity   = serial.PARITY_NONE,
                         stopbits = serial.STOPBITS_ONE)
		


	def __del__(self):
		if self.serial_type == 'GPIO':
			GPIO.cleanup()

	def getValue(self,orden):

		
		self.puerto.write(orden.encode())
		time.sleep(0.1)
		self.puerto.write(self.salto.encode())
		time.sleep(0.1)
		self.dato = self.puerto.readline()
		self.dato = np.fromstring(self.dato.decode('ascii', errors = 'replase'), sep = ' ') 
		return str(self.dato[0]) 

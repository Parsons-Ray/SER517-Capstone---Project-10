import sys
from PyQt5 import QtWidgets, QtGui

def window():

	app = QtWidgets.QApplication(sys.argv)
	w = QtWidgets.QWidget()

	w.setWindowTitle("ATMega Simulator")
	w.setGeometry(100, 100, 300 ,200)

	label1 =  QtWidgets.QLabel(w)
	label2 =  QtWidgets.QLabel(w)
	label3 =  QtWidgets.QLabel(w)
	label4 =  QtWidgets.QLabel(w)
	label5 =  QtWidgets.QLabel(w)
	label6 =  QtWidgets.QLabel(w)
	label7 =  QtWidgets.QLabel(w)

	label1.setText("ATMega328p Simulator")
	label2.setText("Connected to Simulavr  ")
	label3.setText("In Debugging Mode    ")
	label4.setText("Disconnected  ")
	label5.setText("Program Loading")
	label6.setText("ATMega328p")
	label7.setText("ATMega328p")

	label1.move(540 , 45)

	label2.move(330 , 105)
	label3.move(530 , 105)
	label4.move(730 , 105)
	label5.move(930 , 105)

	label6.move(606 , 195)

	label7.move(606 , 530)
	
	

	label1font = QtGui.QFont("Times", 25, QtGui.QFont.Bold)
	label_2_4_font = QtGui.QFont("Times", 15, QtGui.QFont.Bold)
	label6font = QtGui.QFont("Times", 20, QtGui.QFont.Bold)



	label1.setFont(label1font)
	label2.setFont(label_2_4_font)
	label3.setFont(label_2_4_font)
	label4.setFont(label_2_4_font)
	label5.setFont(label_2_4_font)
	label6.setFont(label6font)
	label7.setFont(label6font)



	pins = ['CORE.GPIOR2', 'PORTB.PORT', 'PORTB.PIN', 'PORTB.DDR', 'PORTB.B0-Out', 'IRQ.VECTOR0','EEPROM.EEDR', 'TMRIRQ0.TIMSKO','TIMER0.Counter',
	'TIMER0.TCNT','SPI.SPDR','UART0.UDR']

	pin_dict = {}
	vert_space = 195

	for i in pins:

		pin_dict[i] = QtWidgets.QLabel(w)

		pin_dict[i].setText(i)
		pin_dict[i].move(90, vert_space)
		pin_dict[i].setFont(label_2_4_font)
		
		vert_space += 30

	w.show()

	#to let us know if the process ended successfully or not
	sys.exit(app.exec_())

window()


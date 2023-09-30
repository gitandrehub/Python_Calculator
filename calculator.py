from PyQt5.QtWidgets import QApplication, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QWidget, QDesktopWidget
import sys

class draw_window(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Python Calculator")
        self.setFixedSize(340, 500)

        layout = QVBoxLayout()

        # display
        self.label = QLabel("")
        self.label.setStyleSheet("background-color:#ffffff; font-size:30px; height:60px;")
        layout.addWidget(self.label)

        # row 1: 1 2 3 +
        row1 = QHBoxLayout()
        self.button1 = QPushButton("1")
        self.button2 = QPushButton("2")
        self.button3 = QPushButton("3")
        self.buttonp = QPushButton("+")
        self.button1.setStyleSheet("background-color:#ffffff; font-size:25px; height:70px; width:70px; border-radius:25px;")
        self.button2.setStyleSheet("background-color:#ffffff; font-size:25px; height:70px; width:70px; border-radius:25px;")
        self.button3.setStyleSheet("background-color:#ffffff; font-size:25px; height:70px; width:70px; border-radius:25px;")
        self.buttonp.setStyleSheet("background-color:#000000; color:#ffffff; font-size:25px; height:70px; width:70px; border-radius:25px;")
        row1.addWidget(self.button1)
        row1.addWidget(self.button2)
        row1.addWidget(self.button3)
        row1.addWidget(self.buttonp)
        layout.addLayout(row1)

        # row 2: 4 5 6 -
        row2 = QHBoxLayout()
        self.button4 = QPushButton("4")
        self.button5 = QPushButton("5")
        self.button6 = QPushButton("6")
        self.buttonm = QPushButton("-")
        self.button4.setStyleSheet("background-color:#ffffff; font-size:25px; height:70px; width:70px; border-radius:25px;")
        self.button5.setStyleSheet("background-color:#ffffff; font-size:25px; height:70px; width:70px; border-radius:25px;")
        self.button6.setStyleSheet("background-color:#ffffff; font-size:25px; height:70px; width:70px; border-radius:25px;")
        self.buttonm.setStyleSheet("background-color:#000000; color:#ffffff; font-size:25px; height:70px; width:70px; border-radius:25px;")
        row2.addWidget(self.button4)
        row2.addWidget(self.button5)
        row2.addWidget(self.button6)
        row2.addWidget(self.buttonm)
        layout.addLayout(row2)

        # row 3: 7 8 9 *
        row3 = QHBoxLayout()
        self.button7 = QPushButton("7")
        self.button8 = QPushButton("8")
        self.button9 = QPushButton("9")
        self.buttont = QPushButton("*")
        self.button7.setStyleSheet("background-color:#ffffff; font-size:25px; height:70px; width:70px; border-radius:25px;")
        self.button8.setStyleSheet("background-color:#ffffff; font-size:25px; height:70px; width:70px; border-radius:25px;")
        self.button9.setStyleSheet("background-color:#ffffff; font-size:25px; height:70px; width:70px; border-radius:25px;")
        self.buttont.setStyleSheet("background-color:#000000; color:#ffffff; font-size:25px; height:70px; width:70px; border-radius:25px;")
        row3.addWidget(self.button7)
        row3.addWidget(self.button8)
        row3.addWidget(self.button9)
        row3.addWidget(self.buttont)
        layout.addLayout(row3)

        # row 4: canc 0 back /
        row4 = QHBoxLayout()
        self.buttona = QPushButton("canc")
        self.button0 = QPushButton("0")
        self.buttonc = QPushButton("<")
        self.buttond = QPushButton("/")
        self.buttona.setStyleSheet("background-color:#000000; color:#ffffff; font-size:25px; height:70px; width:70px; border-radius:25px;")
        self.button0.setStyleSheet("background-color:#ffffff; font-size:25px; height:70px; width:70px; border-radius:25px;")
        self.buttonc.setStyleSheet("background-color:#000000; color:#ffffff; font-size:25px; height:70px; width:70px; border-radius:25px;")
        self.buttond.setStyleSheet("background-color:#000000; color:#ffffff; font-size:25px; height:70px; width:70px; border-radius:25px;")
        row4.addWidget(self.buttona)
        row4.addWidget(self.button0)
        row4.addWidget(self.buttonc)
        row4.addWidget(self.buttond)
        layout.addLayout(row4)

        # row 5: =
        self.buttone = QPushButton("=")
        self.buttone.setStyleSheet("background-color:#000000; color:#ffffff; font-size:25px; height:50px; width:70px; border-radius:20px;")
        layout.addWidget(self.buttone)

        self.setLayout(layout)
        self.start()

        # when i push buttons
        self.button0.clicked.connect(self.clickbutton0)
        self.button1.clicked.connect(self.clickbutton1)
        self.button2.clicked.connect(self.clickbutton2)
        self.button3.clicked.connect(self.clickbutton3)
        self.button4.clicked.connect(self.clickbutton4)
        self.button5.clicked.connect(self.clickbutton5)
        self.button6.clicked.connect(self.clickbutton6)
        self.button7.clicked.connect(self.clickbutton7)
        self.button8.clicked.connect(self.clickbutton8)
        self.button9.clicked.connect(self.clickbutton9)
        self.buttonp.clicked.connect(self.clickbuttonp)
        self.buttonm.clicked.connect(self.clickbuttonm)
        self.buttone.clicked.connect(self.clickbuttone)
        self.buttonc.clicked.connect(self.clickbuttonc)
        self.buttona.clicked.connect(self.clickbuttona)
        self.buttond.clicked.connect(self.clickbuttond)
        self.buttont.clicked.connect(self.clickbuttont)      

    def clickbutton0(self):
        if(self.finop):
            self.start()
        self.add_el("0")
    def clickbutton1(self):
        if(self.finop):
            self.start()
        self.add_el("1")
    def clickbutton2(self):
        if(self.finop):
            self.start()
        self.add_el("2")
    def clickbutton3(self):
        if(self.finop):
            self.start()
        self.add_el("3")
    def clickbutton4(self):
        if(self.finop):
            self.start()
        self.add_el("4")
    def clickbutton5(self):
        if(self.finop):
            self.start()
        self.add_el("5")
    def clickbutton6(self):
        if(self.finop):
            self.start()
        self.add_el("6")
    def clickbutton7(self):
        if(self.finop):
            self.start()
        self.add_el("7")
    def clickbutton8(self):
        if(self.finop):
            self.start()
        self.add_el("8")
    def clickbutton9(self):
        if(self.finop):
            self.start()
        self.add_el("9")   

    def clickbuttonp(self):
        if(self.finop):
            self.dato = str(self.res)
            self.exp = self.dato
            self.label.setText(self.exp)
            self.first = True
            self.finop = False
        try:
            self.calcolo_op("+")
            self.exp += "+"
            self.dato = ""
            self.label.setText(self.exp)
        except:
            self.label.setText("error")
            self.res = 0
            self.exp = ""
            self.dato = ""
            self.operation = ""
            self.first = True
    def clickbuttonm(self):
        if(self.finop):
            self.dato = str(self.res)
            self.exp = self.dato
            self.label.setText(self.exp)
            self.first = True
            self.finop = False
        try:
            self.calcolo_op("-")
            self.exp += "-"
            self.dato = ""
            self.label.setText(self.exp)
        except:
            self.label.setText("error")
            self.res = 0
            self.exp = ""
            self.dato = ""
            self.operation = ""
            self.first = True
    def clickbuttond(self):
        if(self.finop):
            self.dato = str(self.res)
            self.exp = self.dato
            self.label.setText(self.exp)
            self.first = True
            self.finop = False
        try:
            self.calcolo_op("/")
            self.exp += "/"
            self.dato = ""
            self.label.setText(self.exp)
        except:
            self.label.setText("error")
            self.res = 0
            self.exp = ""
            self.dato = ""
            self.operation = ""
            self.first = True
    def clickbuttont(self):
        if(self.finop):
            self.dato = str(self.res)
            self.exp = self.dato
            self.label.setText(self.exp)
            self.first = True
            self.finop = False
        try:
            self.calcolo_op("*")
            self.exp += "*"
            self.dato = ""
            self.label.setText(self.exp)
        except:
            self.label.setText("error")
            self.res = 0
            self.exp = ""
            self.dato = ""
            self.operation = ""
            self.first = True
    def clickbuttone(self):
        if(self.first):
            self.exp = self.dato
        else:
            self.calcolo_op(self)
        self.finop = True
        self.exp = ""
        self.dato = ""
        self.operation = ""
    def clickbuttona(self):
        self.exp = ""
        self.label.setText(self.exp)
        self.dato = ""
        self.operation = ""
        self.res = 0
        self.first = True
        self.finop = False
    def clickbuttonc(self):
        try:
            last = self.exp[len(self.exp)-1]
            if(last != "+" and last != "-" and last != "*" and last != "/" and self.dato != ""):
                self.dato = self.dato[0:int(len(self.dato))-1]
            elif (last == "+" or last == "-" or last == "*" or last == "/"):
                self.operation = ""
                self.first = True
            elif (self.operation == "" and self.dato == ""):
                temp = self.exp
                temp = temp[0:int(len(temp))-1]
                self.dato = temp
                self.res = int(temp)
            self.exp = self.exp[0:int(len(self.exp))-1]
            self.label.setText(self.exp)
        except:
            self.exp = ""
            self.label.setText(self.exp)
            self.dato = ""
            self.operation = ""
            self.res = 0
            self.first = True
            self.finop = False  

    def start(self):
        self.res = 0
        self.dato = ""
        self.operation = ""
        self.exp = ""
        self.first = True
        self.finop = False
    def add_el(self, el):
        self.dato += el
        self.exp += el
        self.label.setText(self.exp)
    def calcolo_op(self, arg):
        if(self.first):
            self.operation = arg
            try:
                self.res = float(self.dato)
            except:
                print("errore")
            self.first = False   
        else:
            match (self.operation):
                case "+":
                    self.res += int(self.dato)
                case "-":
                    self.res -= int(self.dato)
                case "*":
                    self.res *= int(self.dato)
                case "/":
                    self.res /= int(self.dato)
            self.operation = arg
            self.exp = str(self.res)
            self.label.setText(self.exp)

                
app = QApplication(sys.argv)
window = draw_window()
window.show()
app.exec()
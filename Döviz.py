import json
import requests
import sys
from PyQt5.QtWidgets import QWidget, QApplication, QComboBox, QVBoxLayout, QHBoxLayout, QPushButton, QDoubleSpinBox,QLCDNumber


class Pencere(QWidget):

    def __init__(self):
        super().__init__()
        self.SetupUI()

    def SetupUI(self):
        self.sonuc = QLCDNumber()
        self.sonuc.setGeometry(20, 10, 360, 130)

        self.comboBox = QComboBox()
        self.comboBox_2 = QComboBox()
        self.symbols()

        v_box = QVBoxLayout()
        v_box.addWidget(self.comboBox)
        v_box.addWidget(self.comboBox_2)

        self.float_box = QDoubleSpinBox()
        self.convert_button = QPushButton("Çevir")

        v_box2 = QVBoxLayout()
        v_box2.addWidget(self.float_box)
        v_box2.addWidget(self.convert_button)

        h_box = QHBoxLayout()
        h_box.addLayout(v_box)
        h_box.addLayout(v_box2)

        v_box3 = QVBoxLayout()
        v_box3.addWidget(self.sonuc)
        v_box3.addLayout(h_box)

        self.setLayout(v_box3)
        self.setWindowTitle("Para Birimi Dönüştürücü")
        self.convert_button.clicked.connect(self.Cevir)

        self.show()

        print("SetupUI Başarılı")

    def Veri(self):
        to_sembol = self.comboBox.currentText()
        from_sembol = self.comboBox_2.currentText()
        amount = str(self.float_box.text())

        self.Cevir(self, to_sembol, from_sembol ,amount)

    def Cevir(self,to_sembol,from_sembol,amount):
        url = "https://api.apilayer.com/fixer/convert?to=" + str(to_sembol) + "&from=" + str(from_sembol) + "&amount=" + amount

        payload = {}
        headers = {"apikey": "h10Leknyt53QRaQQpt85ps3Q5eOprLT8"}

        response = requests.request("GET", url, headers=headers, data=payload)
        result = response.text

        result_dict = json.loads(result)

        print(result_dict["result"])
        self.sonuc.display(result_dict["result"])

        print("Cevir Başarılı")

    def symbols(self):
        url = "https://api.apilayer.com/fixer/symbols"

        payload = {}
        headers = {
            "apikey": "h10Leknyt53QRaQQpt85ps3Q5eOprLT8"
        }

        response = requests.request("GET", url, headers=headers, data=payload)
        result = response.text

        result_dick = json.loads(result)
        for i in result_dick["symbols"]:
            self.comboBox.addItem(i)
            self.comboBox_2.addItem(i)

        print("Symbols Başarılı")


app = QApplication(sys.argv)

pencere = Pencere()

sys.exit(app.exec_())

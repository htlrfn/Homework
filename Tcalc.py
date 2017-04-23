import sys
import requests

from PyQt5.QtWebEngine import  QtWebEngine
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEnginePage
from PyQt5.QtWidgets import (QApplication, QMainWindow, QPushButton, QFormLayout, QLabel, QLineEdit, QComboBox,
                             QWidget, QHBoxLayout, QVBoxLayout, QLayout, QGridLayout, QSpacerItem, QSizePolicy,
                             QDoubleSpinBox, QDesktopWidget)
from PyQt5.QtCore import *


class Calculator(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.initUi()
        self.initSignals()
        self.initLayouts()



    def initUi(self):
        self.lLabel = QLabel('Длина груза (м.см)',self)
        self.wLabel = QLabel('Ширина груза (м.см)', self)
        self.hLabel = QLabel('Высота груза (м.см)', self)
        self.weLabel = QLabel('Вес Груза (кг)', self)
        self.fnLabel = QLabel('Тип груза', self)
        self.dLabel = QLabel('Город отправки', self)
        self.aLabel = QLabel('Город Прибытия', self)
        self.length = QDoubleSpinBox(self)
        self.length.setMaximum(100)
        self.width = QDoubleSpinBox(self)
        self.width.setMaximum(100)
        self.height = QDoubleSpinBox(self)
        self.height.setMaximum(100)
        self.weight = QDoubleSpinBox(self)
        self.weight.setMaximum(100000)
        self.freight_name = QLineEdit('Крепеж',self)
        self.derivalCity = QLineEdit('Санкт Петербург', self)
        self.derival = QComboBox(self)
        self.arrivalCity = QLineEdit(self)
        self.arrival = QComboBox(self)
        self.btn = QPushButton('OK', self)
        self.setFixedSize(300,400)

    def cityFromJson(self, city= None):
        self.cityCode = []
        cityList = requests.get('http://spb.dellin.ru/api/cities/search.json?q={}'.format(city))
        js = cityList.json()

        for city in js:
            self.cityCode.append(dict(city=city['fullName'], code=city['code']))

        return self.cityCode


    def comboFill(self, city = None):
        self.cf=[]
        c=self.cityFromJson(city)
        for cName in c:
            self.cf.append(cName['city'])
        return self.cf


    def initSignals(self):
        self.btn.clicked.connect(self.onClick)
        self.arrivalCity.textChanged.connect(self.onFillA)
        self.derivalCity.textChanged.connect(self.onFillD)
        self.derival.currentIndexChanged.connect(self.dIndex)


    def dIndex(self):
        return self.cf


    def onClick(self):
        self.weightValue = self.weight.value()
        self.heightValue = self.height.value()
        self.lengthValue = self.length.value()
        self.widthValue = self.width.value()
        self.fnText = self.freight_name.text()
        if self.derival.currentIndex() >= 0:
            self.dc = self.derival.currentIndex()
            self.derivalCode = (self.dCityFromJson[self.dc]['code'])

        else:
            self.derivalCode = 7800000000000000000000000
        if self.arrival.currentIndex() >= 0:
            self.ac = self.arrival.currentIndex()
            self.arrivalCode = (self.aCityFromJSon[self.ac]['code'])
            #print(self.arrivalCode)
        else:
            self.arrivalCode = 0
        b.dPage()

    def onFillA(self):
        self.arrivalCityText = self.arrivalCity.text()
        self.comboFill(self.arrivalCityText)
        self.arrival.clear()
        self.arrival.addItems(self.cf)
        self.aCityFromJSon = self.cityCode

    def onFillD(self):
        self.derivalCityText = self.derivalCity.text()
        self.comboFill(self.derivalCityText)
        self.derival.clear()
        self.derival.addItems(self.cf)
        self.dCityFromJson = self.cityCode

    def initLayouts(self):
        self.mainLayout = QFormLayout()
        self.mainLayout.addWidget(self.lLabel)
        self.mainLayout.addWidget(self.length)
        self.mainLayout.addWidget(self.wLabel)
        self.mainLayout.addWidget(self.width)
        self.mainLayout.addWidget(self.hLabel)
        self.mainLayout.addWidget(self.height)
        self.mainLayout.addWidget(self.weLabel)
        self.mainLayout.addWidget(self.weight)
        self.mainLayout.addWidget(self.fnLabel)
        self.mainLayout.addWidget(self.freight_name)
        self.mainLayout.addWidget(self.dLabel)
        self.mainLayout.addWidget(self.derivalCity)
        self.mainLayout.addWidget(self.derival)
        self.mainLayout.addWidget(self.aLabel)
        self.mainLayout.addWidget(self.arrivalCity)
        self.mainLayout.addWidget(self.arrival)
        self.mainLayout.addWidget(self.btn)
        self.setLayout(self.mainLayout)


class Delovie_Browser(QWebEngineView):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.initSignals()

        self.arrivalD = int
        self.derivalD = int
        self.heightD = float
        self.lengthD = float
        self.widthD = float
        self.weightD = float
        self.freightNameD = str
        self.lp = self.loadPage

        self.initLayouts()
        self.setFixedSize((window_width -350), (window_height - 50))
        self.page().setZoomFactor(0.9)







    def __call__(self, *args, **kwargs):
        self.arrivalD = int(b.calc.arrivalCode)
        self.derivalD = int(b.calc.derivalCode)
        self.heightD = b.calc.heightValue
        self.lengthD = b.calc.lengthValue
        self.weightD = b.calc.weightValue
        self.widthD = b.calc.widthValue
        self.freightNameD = b.calc.fnText
        self.lp()

    def loadPage(self):
        self.load(QUrl(
            'http://spb.dellin.ru/requests/?derival_point_code={}&arrival_point_code={}'.format(self.derivalD,
                                                                                                self.arrivalD)))

    def calcPage(self):
        p = self.page()
        self.page().runJavaScript('document.getElementById("length_view").value = "{}";'.format(self.lengthD))
        self.page().runJavaScript('document.getElementById("width_view").focus();')
        self.page().runJavaScript('document.getElementById("width_view").value = "{}";'.format(self.widthD))
        self.page().runJavaScript('document.getElementById("height_view").focus();')
        self.page().runJavaScript('document.getElementById("height_view").value = "{}";'.format(self.heightD))
        self.page().runJavaScript('document.getElementById("sized_weight").value = "{}";'.format(self.weightD))
        self.page().runJavaScript('document.getElementById("freight_name").value = "{}";'.format(self.freightNameD))
        self.page().runJavaScript('document.getElementById("freight_name").focus();')
        self.page().runJavaScript('window.onbeforeunload = null;')

    def initLayouts(self):
        self.layout = QHBoxLayout()
        #self.setLayout(self.layout)

    def initSignals(self):
        self.loadFinished.connect(self.calcPage)

class MainCalcWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.initUi()
        self.initLayouts()


    def initUi(self):
        self.calc = Calculator()
        self.dPage = Delovie_Browser()

    def initLayouts(self):
        self.spacer_1 = QSpacerItem(0,0, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.spacer_2 = QSpacerItem(0, 0, QSizePolicy.Maximum, QSizePolicy.Expanding)
        self.mainLayout = QHBoxLayout()
        self.leftLayout = QVBoxLayout()
        self.leftTopLayout = QHBoxLayout()
        self.mainLayout.addLayout(self.leftLayout)
        self.leftLayout.addLayout(self.leftTopLayout)
        self.leftTopLayout.addWidget(self.calc)
        self.leftTopLayout.addItem(self.spacer_1)
        self.leftLayout.addItem(self.spacer_1)
        self.leftLayout.addItem(self.spacer_2)
        self.mainLayout.addWidget(self.dPage)
        self.setLayout(self.mainLayout)





if __name__ == '__main__':
    app=QApplication(sys.argv)
    a=QDesktopWidget()
    hw=a.availableGeometry()
    window_width = ((hw.getRect()[2])* 0.95)
    window_height = ((hw.getRect()[3]) * 0.95)
    b=MainCalcWindow()
    b.show()
    b.setGeometry(0,30, window_width, window_height )
    b.setFixedSize(window_width, window_height)
    app.exec_()

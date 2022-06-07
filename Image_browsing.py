from PyQt5 import QtCore, QtGui, QtWidgets
import os
import requests
from bs4 import BeautifulSoup

class Ui_Browser(object):
    def setupUi(self, Browser):
        Browser.setObjectName("Browser")
        Browser.setFixedSize(831, 576)
        Browser.setStyleSheet("background-color: rgb(124, 62, 102);")
        self.Inputs = QtWidgets.QLineEdit(Browser)
        self.Inputs.setGeometry(QtCore.QRect(2, 11, 831, 41))
        self.Inputs.setStyleSheet("background-color: rgb(242, 235, 233);")
        self.Inputs.setObjectName("Inputs")
        self.Search = QtWidgets.QPushButton(Browser)
        self.Search.setGeometry(QtCore.QRect(10, 60, 131, 41))
        self.Search.setStyleSheet("background-color: rgb(165, 190, 204);\n"
"\n"
"")
        self.Search.setObjectName("Search")
        self.Clear = QtWidgets.QPushButton(Browser)
        self.Clear.setGeometry(QtCore.QRect(690, 60, 131, 41))
        self.Clear.clicked.connect(self.Clearing)
        self.Clear.setStyleSheet("background-color: rgb(165, 190, 204);\n"
"")
        self.Clear.setObjectName("Clear")
        self.Image_holder = QtWidgets.QScrollArea(Browser)
        self.Image_holder.setGeometry(QtCore.QRect(0, 110, 831, 391))
        self.Image_holder.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.Image_holder.setStyleSheet("background-color: rgb(242, 235, 233);")
        self.Image_holder.setWidgetResizable(True)
        self.Image_holder.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.Image_holder.setObjectName("Image_holder")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 1175, 1135))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName("verticalLayout")
        
        self.Exit = QtWidgets.QPushButton(Browser)
        self.Exit.setGeometry(QtCore.QRect(10, 530, 131, 41))
        self.Exit.setStyleSheet("background-color: rgb(165, 190, 204);\n"
"\n"
"")
        

        self.label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label.setText("")
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.Image_holder.setWidget(self.scrollAreaWidgetContents)
        
        self.Exit.setObjectName("Exit")
        self.retranslateUi(Browser)
        self.Exit.clicked.connect(Browser.close)
        self.Search.clicked.connect(self.Searching)
        QtCore.QMetaObject.connectSlotsByName(Browser)
    
    def Searching(self):
        Inputs = self.Inputs.text()
        URL = f"https://www.bing.com/images/search?q={Inputs}+&form=HDRSC2&first=1&tsc=ImageHoverTitle"
        URl_info = requests.get(URL)
        soup = BeautifulSoup(URl_info.text, "html.parser")
        Images = soup.findAll("img", attrs={"class": "mimg"})
        Images_URL = []
        #getting images scr from tag
        for image_URL in Images :
            url = image_URL.get("src")
            if url == None :
                continue
            else :
                Images_URL.append(url)
    
        o = 0
        print(len(Images_URL))
        for image_url in Images_URL:
            try:
                with open(f"s{o}.jpg", "wb") as picture :
                    picture_file = requests.get((image_url)).content
                    picture.write(picture_file)
            except requests.exceptions.Timeout:
                pass
            except requests.exceptions.TooManyRedirects:
                pass
            except requests.exceptions.RequestException as e:
                pass
            o += 1
        directory = "C:\\Users\\pc\\Image_browsing"
        for filename in os.listdir(directory):
            f = os.path.join(directory, filename)
            if os.path.isfile(f) and "jpg" in f :
                file_name = f.split(sep=" \ ")
                self.label_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
                self.label_2.setText("")
                self.label_2.setPixmap(QtGui.QPixmap(f'{file_name[-1]}'))
                self.label_2.setObjectName("label_2")
                self.verticalLayout.addWidget(self.label_2)
        
                




    def Clearing(self) :
        directory = "C:\\Users\\pc\\Image_browsing"
        for filename in os.listdir(directory):
            f = os.path.join(directory, filename)
            if os.path.isfile(f) and "jpg" in f :
                os.remove(f)
        for i in reversed(range(self.verticalLayout.count())):
            self.verticalLayout.itemAt(i).widget().setParent(None)
        




        
        

    def retranslateUi(self, Browser):
        _translate = QtCore.QCoreApplication.translate
        Browser.setWindowTitle(_translate("Browser", "Bing Image Browser"))
        self.Search.setText(_translate("Browser", "Click to Search"))
        self.Clear.setText(_translate("Browser", "Click to Clear"))
        self.Exit.setText(_translate("Browser", "Click to Exit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Browser = QtWidgets.QWidget()
    ui = Ui_Browser()
    ui.setupUi(Browser)
    Browser.show()
    sys.exit(app.exec())



"""

    ### Computer application to calculate fatigue strength of selected machine elements. ###

 -*- coding: utf-8 -*-
Form implementation generated from reading ui file (and manual editing)
Created by: PyQt4 UI code generator 4.11.4
 
Demo version in Polish language.

# Author: Karol Domanski
# Date: 12/2017
# Version: Demo 1.0

"""

from PyQt4 import QtCore, QtGui
import matplotlib.pyplot as plt
import sys

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

#------ Support window
    
class Ui_MainWindow2(object):
    def setupUi(self, MainWindow2):
        MainWindow2.setObjectName(_fromUtf8("MainWindow"))
        MainWindow2.resize(825, 623)
        MainWindow2.setGeometry(QtCore.QRect(1100, 200, 825, 623))
        self.centralwidget = QtGui.QWidget(MainWindow2)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.textEdit_22 = QtGui.QTextEdit(self.centralwidget)
        self.textEdit_22.setGeometry(QtCore.QRect(10, 10, 811, 591))
        self.textEdit_22.setReadOnly(True)
        self.textEdit_22.setObjectName(_fromUtf8("textEdit_22"))
        MainWindow2.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow2)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow2.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow2)
        
    def retranslateUi(self, MainWindow2):
        MainWindow2.setWindowTitle(_translate("Okno pomocy", "Okno pomocy", None))
        self.textEdit_22.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.5pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Wykonał:</span></p>\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Domański Karol</span><span style=\" font-size:12pt;\"><br /></span><span style=\" font-size:8pt;\">v.1.0 (2017r.)</span><span style=\" font-size:12pt;\"><br /></span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600;\">Aplikacja do obliczeń wytrzymałości zmęczeniowej.</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">Opis programu</span><span style=\" font-size:10pt;\">:<br />    </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">    </span><span style=\" font-size:9pt;\">Aplikacja ma za zadanie zautomatyzować oraz przyspieszyć proces obliczeń z zakresu zagadnień wytrzymałości zmęczeniowej. Ma także za zadanie wykreślenie charakterystyki zmęczeniowej na podstawie wykresu Haigha. Dotyczy ona obciążenia sinusoidalnego pręta. Wyniki w postaci wykresu i rozwiązania zagadnienia można zapisać lub skopiować do pliku umożliwiającego wydruk. Aplikacja może znaleźć zastosowanie w celach dydaktycznych. Program rozpatruje przypadki naprężeń średnich o wartościach dodatnich jak i ujemnych. Aplikacja automatycznie dostosowuje oś dodatnią lub oś ujemną dla wprowadzonych danych. Rozwiązanie każdego z zagadnień dzieli się na cztery przypadki. Rozpatruje zadanie ze względu na współczynnik kierunkowy prostej obciążeniowej, a następnie uzależnia rozwiązanie wobec punktu przecięcia tej prostej z warunkami wyznaczonymi przez stałe materiałowe. Na tej podstawie dokonuje obliczeń i wykreśla wykres Haigha.<br /><br /><br /></span><span style=\" font-size:10pt; font-weight:600;\">Funkcje głównego okna</span><span style=\" font-size:10pt;\">:</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">    </span><span style=\" font-size:9pt;\">Aby uzyskać wynik potrzebnej szukanej należy kliknąć w nazwę jednej z nich. Każda znajduje się poniżej okna pomocy. Po kliknięciu w odpowiednią wielkość uzyskujemy dostęp do wpisania poszczególnych danych wejściowych. Każdy ze skrótów został opisany w legendzie. Po wpisaniu istnieje możliwość obliczenia wartości szukanej, wykreślenia wykresu Haigha, uzyskania opisu poszczególnych obliczeń. Prawe okno funkcyjne służy do ukazania rozwiązania poszczególnych części zadania oraz objaśnień dotyczących rysowania uproszczonego wykresu Haigha.<br /><br /></span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">Funkcje okna &quot;</span><span style=\" font-size:10pt; font-weight:600;\">Wykres Haigha</span><span style=\" font-size:10pt;\">&quot;:<br /><br />    </span><span style=\" font-size:9pt;\">Wykres można uzyskać tylko po wpisaniu danych wejściowych. Posiada on własne menu znajdujące się pod nim. Każda z nich posiada podpowiedź po najechaniu kursorem na ikonę funkcji. Pierwsza funkcja umożliwia powrót do pierwotnego wyglądu. Kolejne dwa to cofnięcie lub powrót do widoku. Czwarta funkcja to manipulacja wykresem za pomocą kursora. Piąta powiększenie danego obszaru. Szósta manipuluje całościowym wyglądem wykresu. Oraz ostatnia, która oferuje możliwość zapisania wykresu w formatach: .png, .eps, .pdf, .pgf, .ps, .raw, .svg . Po otrzymaniu wykresu istnieje możliwość zminimalizowania okna i wpisania innych wartości i otrzymanie kolejnego wykresu w kolejnym oknie. Automatyzacja obliczeń dopuszcza do szybkiego porównania zmian w wykresie spowodowanymi innymi danymi wejściowymi.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:9pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">Funkcje okna &quot;</span><span style=\" font-size:10pt; font-weight:600;\">Oblicz/ rozwiązanie</span><span style=\" font-size:10pt;\">&quot;:</span><span style=\" font-size:9pt;\"><br />    </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">    Po załączeniu tej funkcji w prawym oknie wyświetla się rozwiązanie zagadnienia z opisem kolejno wykonywanych obliczeń. W oknie wyjaśnione jest także w jaki sposób narysować otrzymany wykres Haigha. Okno posiada możliwość skopiowania otrzymanego rozwiązania w postaci edytowanego tekstu. Rozwiązanie jest zależne od czterech przypadków znajdujących się w opisie programu.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:9pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">Funkcje okna &quot;</span><span style=\" font-size:10pt; font-weight:600;\">Rozwiąż zadanie</span><span style=\" font-size:10pt;\">&quot;:</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">    </span><span style=\" font-size:9pt;\">Pozwala na jednoczesne wykonanie dwóch powyższych funkcji.<br /></span></p>\n"
"<p align=\"right\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p></body></html>", None))


#------ Main window
        
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1656, 938)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.toolBox = QtGui.QToolBox(self.centralwidget)
        self.toolBox.setGeometry(QtCore.QRect(10, 50, 801, 831))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.toolBox.setFont(font)
        self.toolBox.setObjectName(_fromUtf8("toolBox"))
        self.page1 = QtGui.QWidget()
        self.page1.setEnabled(True)
        self.page1.setGeometry(QtCore.QRect(0, 0, 801, 651))
        self.page1.setObjectName(_fromUtf8("page1"))
        self.label_16 = QtGui.QLabel(self.page1)
        self.label_16.setGeometry(QtCore.QRect(40, 190, 711, 291))
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.pushButton_9 = QtGui.QPushButton(self.page1)
        self.pushButton_9.setEnabled(True)
        self.pushButton_9.setGeometry(QtCore.QRect(340, 40, 111, 41))
        self.pushButton_9.setObjectName(_fromUtf8("pushButton_9"))
        self.label_20 = QtGui.QLabel(self.page1)
        self.label_20.setGeometry(QtCore.QRect(270, 0, 261, 41))
        self.label_20.setObjectName(_fromUtf8("label_20"))
        self.label_15 = QtGui.QLabel(self.page1)
        self.label_15.setGeometry(QtCore.QRect(110, 610, 551, 41))
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.toolBox.addItem(self.page1, _fromUtf8(""))
        self.page2 = QtGui.QWidget()
        self.page2.setGeometry(QtCore.QRect(0, 0, 801, 651))
        self.page2.setObjectName(_fromUtf8("page2"))
        self.label_4 = QtGui.QLabel(self.page2)
        self.label_4.setGeometry(QtCore.QRect(40, 290, 91, 31))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.textEdit_3 = QtGui.QTextEdit(self.page2)
        self.textEdit_3.setGeometry(QtCore.QRect(180, 280, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.textEdit_3.setFont(font)
        self.textEdit_3.setTabChangesFocus(True)
        self.textEdit_3.setObjectName(_fromUtf8("textEdit_3"))
        self.label_5 = QtGui.QLabel(self.page2)
        self.label_5.setGeometry(QtCore.QRect(560, 110, 161, 61))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label = QtGui.QLabel(self.page2)
        self.label.setGeometry(QtCore.QRect(250, 0, 351, 51))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_8 = QtGui.QLabel(self.page2)
        self.label_8.setGeometry(QtCore.QRect(310, 160, 121, 31))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.label_12 = QtGui.QLabel(self.page2)
        self.label_12.setGeometry(QtCore.QRect(320, 280, 91, 31))
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.label_10 = QtGui.QLabel(self.page2)
        self.label_10.setGeometry(QtCore.QRect(110, 80, 111, 61))
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.pushButton = QtGui.QPushButton(self.page2)
        self.pushButton.setGeometry(QtCore.QRect(470, 220, 141, 51))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.label_2 = QtGui.QLabel(self.page2)
        self.label_2.setGeometry(QtCore.QRect(10, 150, 151, 51))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.textEdit_6 = QtGui.QTextEdit(self.page2)
        self.textEdit_6.setGeometry(QtCore.QRect(660, 200, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.textEdit_6.setFont(font)
        self.textEdit_6.setTabChangesFocus(True)
        self.textEdit_6.setObjectName(_fromUtf8("textEdit_6"))
        self.label_11 = QtGui.QLabel(self.page2)
        self.label_11.setGeometry(QtCore.QRect(310, 210, 121, 31))
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.line_2 = QtGui.QFrame(self.page2)
        self.line_2.setGeometry(QtCore.QRect(440, 60, 20, 441))
        self.line_2.setFrameShape(QtGui.QFrame.VLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.textEdit_2 = QtGui.QTextEdit(self.page2)
        self.textEdit_2.setGeometry(QtCore.QRect(180, 210, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.textEdit_2.setFont(font)
        self.textEdit_2.setTabChangesFocus(True)
        self.textEdit_2.setObjectName(_fromUtf8("textEdit_2"))
        self.textEdit = QtGui.QTextEdit(self.page2)
        self.textEdit.setGeometry(QtCore.QRect(180, 150, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.textEdit.setFont(font)
        self.textEdit.setMouseTracking(False)
        self.textEdit.setToolTip(_fromUtf8(""))
        self.textEdit.setStatusTip(_fromUtf8(""))
        self.textEdit.setWhatsThis(_fromUtf8(""))
        self.textEdit.setAutoFillBackground(False)
        self.textEdit.setTabChangesFocus(True)
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.label_3 = QtGui.QLabel(self.page2)
        self.label_3.setGeometry(QtCore.QRect(20, 210, 131, 61))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.line_3 = QtGui.QFrame(self.page2)
        self.line_3.setGeometry(QtCore.QRect(-3, 50, 821, 20))
        self.line_3.setFrameShape(QtGui.QFrame.HLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.label_14 = QtGui.QLabel(self.page2)
        self.label_14.setGeometry(QtCore.QRect(320, 420, 91, 31))
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.textEdit_5 = QtGui.QTextEdit(self.page2)
        self.textEdit_5.setGeometry(QtCore.QRect(180, 420, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.textEdit_5.setFont(font)
        self.textEdit_5.setTabChangesFocus(True)
        self.textEdit_5.setObjectName(_fromUtf8("textEdit_5"))
        self.label_7 = QtGui.QLabel(self.page2)
        self.label_7.setGeometry(QtCore.QRect(40, 420, 101, 31))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.label_13 = QtGui.QLabel(self.page2)
        self.label_13.setGeometry(QtCore.QRect(320, 350, 91, 31))
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.label_6 = QtGui.QLabel(self.page2)
        self.label_6.setGeometry(QtCore.QRect(40, 360, 101, 31))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.textEdit_4 = QtGui.QTextEdit(self.page2)
        self.textEdit_4.setGeometry(QtCore.QRect(180, 350, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.textEdit_4.setFont(font)
        self.textEdit_4.setTabChangesFocus(True)
        self.textEdit_4.setObjectName(_fromUtf8("textEdit_4"))
        self.label_9 = QtGui.QLabel(self.page2)
        self.label_9.setGeometry(QtCore.QRect(10, 510, 781, 141))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_9.setFont(font)
        self.label_9.setFrameShape(QtGui.QFrame.WinPanel)
        self.label_9.setLineWidth(1)
        self.label_9.setMidLineWidth(0)
        self.label_9.setWordWrap(False)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.line = QtGui.QFrame(self.page2)
        self.line.setGeometry(QtCore.QRect(10, 490, 801, 20))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.pushButton_2 = QtGui.QPushButton(self.page2)
        self.pushButton_2.setGeometry(QtCore.QRect(470, 290, 141, 51))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton_4 = QtGui.QPushButton(self.page2)
        self.pushButton_4.setGeometry(QtCore.QRect(630, 270, 161, 91))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.label_75 = QtGui.QLabel(self.page2)
        self.label_75.setGeometry(QtCore.QRect(350, 560, 211, 61))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_75.setFont(font)
        self.label_75.setObjectName(_fromUtf8("label_75"))
        self.toolBox.addItem(self.page2, _fromUtf8(""))
        self.page3 = QtGui.QWidget()
        self.page3.setGeometry(QtCore.QRect(0, 0, 801, 651))
        self.page3.setObjectName(_fromUtf8("page3"))
        self.line_4 = QtGui.QFrame(self.page3)
        self.line_4.setGeometry(QtCore.QRect(-13, 50, 1011, 20))
        self.line_4.setFrameShape(QtGui.QFrame.HLine)
        self.line_4.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_4.setObjectName(_fromUtf8("line_4"))
        self.label_17 = QtGui.QLabel(self.page3)
        self.label_17.setGeometry(QtCore.QRect(250, 0, 351, 51))
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.pushButton_5 = QtGui.QPushButton(self.page3)
        self.pushButton_5.setGeometry(QtCore.QRect(470, 210, 141, 51))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        self.label_18 = QtGui.QLabel(self.page3)
        self.label_18.setGeometry(QtCore.QRect(560, 110, 161, 61))
        self.label_18.setObjectName(_fromUtf8("label_18"))
        self.line_5 = QtGui.QFrame(self.page3)
        self.line_5.setGeometry(QtCore.QRect(440, 60, 20, 441))
        self.line_5.setFrameShape(QtGui.QFrame.VLine)
        self.line_5.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_5.setObjectName(_fromUtf8("line_5"))
        self.pushButton_6 = QtGui.QPushButton(self.page3)
        self.pushButton_6.setGeometry(QtCore.QRect(630, 270, 161, 91))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setObjectName(_fromUtf8("pushButton_6"))
        self.pushButton_7 = QtGui.QPushButton(self.page3)
        self.pushButton_7.setGeometry(QtCore.QRect(470, 280, 141, 51))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setObjectName(_fromUtf8("pushButton_7"))
        self.textEdit_7 = QtGui.QTextEdit(self.page3)
        self.textEdit_7.setGeometry(QtCore.QRect(630, 190, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.textEdit_7.setFont(font)
        self.textEdit_7.setTabChangesFocus(True)
        self.textEdit_7.setLineWrapMode(QtGui.QTextEdit.WidgetWidth)
        self.textEdit_7.setLineWrapColumnOrWidth(0)
        self.textEdit_7.setObjectName(_fromUtf8("textEdit_7"))
        self.line_6 = QtGui.QFrame(self.page3)
        self.line_6.setGeometry(QtCore.QRect(-10, 490, 821, 20))
        self.line_6.setFrameShape(QtGui.QFrame.HLine)
        self.line_6.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_6.setObjectName(_fromUtf8("line_6"))
        self.label_19 = QtGui.QLabel(self.page3)
        self.label_19.setGeometry(QtCore.QRect(20, 510, 751, 141))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_19.setFont(font)
        self.label_19.setFrameShape(QtGui.QFrame.WinPanel)
        self.label_19.setLineWidth(1)
        self.label_19.setMidLineWidth(0)
        self.label_19.setWordWrap(False)
        self.label_19.setObjectName(_fromUtf8("label_19"))
        self.textEdit_8 = QtGui.QTextEdit(self.page3)
        self.textEdit_8.setGeometry(QtCore.QRect(190, 160, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.textEdit_8.setFont(font)
        self.textEdit_8.setTabChangesFocus(True)
        self.textEdit_8.setLineWrapMode(QtGui.QTextEdit.WidgetWidth)
        self.textEdit_8.setLineWrapColumnOrWidth(0)
        self.textEdit_8.setObjectName(_fromUtf8("textEdit_8"))
        self.label_21 = QtGui.QLabel(self.page3)
        self.label_21.setGeometry(QtCore.QRect(330, 340, 91, 41))
        self.label_21.setObjectName(_fromUtf8("label_21"))
        self.label_22 = QtGui.QLabel(self.page3)
        self.label_22.setGeometry(QtCore.QRect(0, 60, 91, 41))
        self.label_22.setObjectName(_fromUtf8("label_22"))
        self.label_23 = QtGui.QLabel(self.page3)
        self.label_23.setGeometry(QtCore.QRect(330, 410, 91, 31))
        self.label_23.setObjectName(_fromUtf8("label_23"))
        self.textEdit_9 = QtGui.QTextEdit(self.page3)
        self.textEdit_9.setGeometry(QtCore.QRect(190, 340, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.textEdit_9.setFont(font)
        self.textEdit_9.setTabChangesFocus(True)
        self.textEdit_9.setLineWrapMode(QtGui.QTextEdit.WidgetWidth)
        self.textEdit_9.setLineWrapColumnOrWidth(0)
        self.textEdit_9.setObjectName(_fromUtf8("textEdit_9"))
        self.label_26 = QtGui.QLabel(self.page3)
        self.label_26.setGeometry(QtCore.QRect(70, 160, 51, 41))
        self.label_26.setObjectName(_fromUtf8("label_26"))
        self.label_27 = QtGui.QLabel(self.page3)
        self.label_27.setGeometry(QtCore.QRect(320, 160, 51, 41))
        self.label_27.setObjectName(_fromUtf8("label_27"))
        self.textEdit_10 = QtGui.QTextEdit(self.page3)
        self.textEdit_10.setGeometry(QtCore.QRect(190, 220, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.textEdit_10.setFont(font)
        self.textEdit_10.setTabChangesFocus(True)
        self.textEdit_10.setLineWrapMode(QtGui.QTextEdit.WidgetWidth)
        self.textEdit_10.setLineWrapColumnOrWidth(0)
        self.textEdit_10.setObjectName(_fromUtf8("textEdit_10"))
        self.label_28 = QtGui.QLabel(self.page3)
        self.label_28.setGeometry(QtCore.QRect(70, 210, 41, 51))
        self.label_28.setObjectName(_fromUtf8("label_28"))
        self.textEdit_11 = QtGui.QTextEdit(self.page3)
        self.textEdit_11.setGeometry(QtCore.QRect(190, 410, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.textEdit_11.setFont(font)
        self.textEdit_11.setTabChangesFocus(True)
        self.textEdit_11.setLineWrapMode(QtGui.QTextEdit.WidgetWidth)
        self.textEdit_11.setLineWrapColumnOrWidth(0)
        self.textEdit_11.setObjectName(_fromUtf8("textEdit_11"))
        self.label_29 = QtGui.QLabel(self.page3)
        self.label_29.setGeometry(QtCore.QRect(70, 100, 51, 41))
        self.label_29.setObjectName(_fromUtf8("label_29"))
        self.textEdit_12 = QtGui.QTextEdit(self.page3)
        self.textEdit_12.setGeometry(QtCore.QRect(190, 100, 101, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("MS Shell Dlg 2"))
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.textEdit_12.setFont(font)
        self.textEdit_12.setTabChangesFocus(True)
        self.textEdit_12.setLineWrapMode(QtGui.QTextEdit.WidgetWidth)
        self.textEdit_12.setLineWrapColumnOrWidth(0)
        self.textEdit_12.setObjectName(_fromUtf8("textEdit_12"))
        self.label_30 = QtGui.QLabel(self.page3)
        self.label_30.setGeometry(QtCore.QRect(310, 100, 71, 41))
        self.label_30.setObjectName(_fromUtf8("label_30"))
        self.label_58 = QtGui.QLabel(self.page3)
        self.label_58.setGeometry(QtCore.QRect(330, 280, 91, 41))
        self.label_58.setObjectName(_fromUtf8("label_58"))
        self.textEdit_25 = QtGui.QTextEdit(self.page3)
        self.textEdit_25.setGeometry(QtCore.QRect(190, 280, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.textEdit_25.setFont(font)
        self.textEdit_25.setTabChangesFocus(True)
        self.textEdit_25.setLineWrapMode(QtGui.QTextEdit.WidgetWidth)
        self.textEdit_25.setLineWrapColumnOrWidth(0)
        self.textEdit_25.setObjectName(_fromUtf8("textEdit_25"))
        self.label_59 = QtGui.QLabel(self.page3)
        self.label_59.setGeometry(QtCore.QRect(70, 280, 41, 31))
        self.label_59.setObjectName(_fromUtf8("label_59"))
        self.label_60 = QtGui.QLabel(self.page3)
        self.label_60.setGeometry(QtCore.QRect(320, 540, 451, 111))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_60.setFont(font)
        self.label_60.setObjectName(_fromUtf8("label_60"))
        self.label_57 = QtGui.QLabel(self.page3)
        self.label_57.setGeometry(QtCore.QRect(730, 190, 61, 31))
        self.label_57.setObjectName(_fromUtf8("label_57"))
        self.label_35 = QtGui.QLabel(self.page3)
        self.label_35.setGeometry(QtCore.QRect(40, 340, 111, 41))
        self.label_35.setObjectName(_fromUtf8("label_35"))
        self.label_80 = QtGui.QLabel(self.page3)
        self.label_80.setGeometry(QtCore.QRect(40, 410, 111, 41))
        self.label_80.setObjectName(_fromUtf8("label_80"))
        self.toolBox.addItem(self.page3, _fromUtf8(""))
        self.page4 = QtGui.QWidget()
        self.page4.setGeometry(QtCore.QRect(0, 0, 801, 651))
        self.page4.setObjectName(_fromUtf8("page4"))
        self.line_7 = QtGui.QFrame(self.page4)
        self.line_7.setGeometry(QtCore.QRect(420, 60, 20, 441))
        self.line_7.setFrameShape(QtGui.QFrame.VLine)
        self.line_7.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_7.setObjectName(_fromUtf8("line_7"))
        self.pushButton_11 = QtGui.QPushButton(self.page4)
        self.pushButton_11.setGeometry(QtCore.QRect(450, 290, 141, 51))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_11.setFont(font)
        self.pushButton_11.setObjectName(_fromUtf8("pushButton_11"))
        self.line_8 = QtGui.QFrame(self.page4)
        self.line_8.setGeometry(QtCore.QRect(-23, 50, 831, 20))
        self.line_8.setFrameShape(QtGui.QFrame.HLine)
        self.line_8.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_8.setObjectName(_fromUtf8("line_8"))
        self.pushButton_12 = QtGui.QPushButton(self.page4)
        self.pushButton_12.setGeometry(QtCore.QRect(450, 220, 141, 51))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_12.setFont(font)
        self.pushButton_12.setObjectName(_fromUtf8("pushButton_12"))
        self.label_24 = QtGui.QLabel(self.page4)
        self.label_24.setGeometry(QtCore.QRect(190, 0, 471, 51))
        self.label_24.setObjectName(_fromUtf8("label_24"))
        self.pushButton_13 = QtGui.QPushButton(self.page4)
        self.pushButton_13.setGeometry(QtCore.QRect(610, 270, 161, 91))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_13.setFont(font)
        self.pushButton_13.setObjectName(_fromUtf8("pushButton_13"))
        self.label_25 = QtGui.QLabel(self.page4)
        self.label_25.setGeometry(QtCore.QRect(430, 110, 381, 61))
        self.label_25.setObjectName(_fromUtf8("label_25"))
        self.textEdit_13 = QtGui.QTextEdit(self.page4)
        self.textEdit_13.setGeometry(QtCore.QRect(610, 190, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.textEdit_13.setFont(font)
        self.textEdit_13.setTabChangesFocus(True)
        self.textEdit_13.setObjectName(_fromUtf8("textEdit_13"))
        self.label_31 = QtGui.QLabel(self.page4)
        self.label_31.setGeometry(QtCore.QRect(70, 400, 91, 31))
        self.label_31.setObjectName(_fromUtf8("label_31"))
        self.textEdit_14 = QtGui.QTextEdit(self.page4)
        self.textEdit_14.setGeometry(QtCore.QRect(160, 130, 61, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.textEdit_14.setFont(font)
        self.textEdit_14.setTabChangesFocus(True)
        self.textEdit_14.setObjectName(_fromUtf8("textEdit_14"))
        self.textEdit_15 = QtGui.QTextEdit(self.page4)
        self.textEdit_15.setGeometry(QtCore.QRect(200, 200, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.textEdit_15.setFont(font)
        self.textEdit_15.setTabChangesFocus(True)
        self.textEdit_15.setObjectName(_fromUtf8("textEdit_15"))
        self.label_36 = QtGui.QLabel(self.page4)
        self.label_36.setGeometry(QtCore.QRect(340, 300, 91, 31))
        self.label_36.setObjectName(_fromUtf8("label_36"))
        self.label_37 = QtGui.QLabel(self.page4)
        self.label_37.setGeometry(QtCore.QRect(-10, 60, 111, 61))
        self.label_37.setObjectName(_fromUtf8("label_37"))
        self.textEdit_16 = QtGui.QTextEdit(self.page4)
        self.textEdit_16.setGeometry(QtCore.QRect(200, 250, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.textEdit_16.setFont(font)
        self.textEdit_16.setTabChangesFocus(True)
        self.textEdit_16.setObjectName(_fromUtf8("textEdit_16"))
        self.label_39 = QtGui.QLabel(self.page4)
        self.label_39.setGeometry(QtCore.QRect(70, 300, 91, 31))
        self.label_39.setObjectName(_fromUtf8("label_39"))
        self.textEdit_17 = QtGui.QTextEdit(self.page4)
        self.textEdit_17.setGeometry(QtCore.QRect(200, 350, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.textEdit_17.setFont(font)
        self.textEdit_17.setTabChangesFocus(True)
        self.textEdit_17.setObjectName(_fromUtf8("textEdit_17"))
        self.label_40 = QtGui.QLabel(self.page4)
        self.label_40.setGeometry(QtCore.QRect(340, 260, 91, 31))
        self.label_40.setObjectName(_fromUtf8("label_40"))
        self.label_41 = QtGui.QLabel(self.page4)
        self.label_41.setGeometry(QtCore.QRect(340, 350, 91, 31))
        self.label_41.setObjectName(_fromUtf8("label_41"))
        self.label_42 = QtGui.QLabel(self.page4)
        self.label_42.setGeometry(QtCore.QRect(70, 350, 91, 31))
        self.label_42.setObjectName(_fromUtf8("label_42"))
        self.label_43 = QtGui.QLabel(self.page4)
        self.label_43.setGeometry(QtCore.QRect(340, 400, 91, 31))
        self.label_43.setObjectName(_fromUtf8("label_43"))
        self.textEdit_18 = QtGui.QTextEdit(self.page4)
        self.textEdit_18.setGeometry(QtCore.QRect(200, 300, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.textEdit_18.setFont(font)
        self.textEdit_18.setTabChangesFocus(True)
        self.textEdit_18.setObjectName(_fromUtf8("textEdit_18"))
        self.label_44 = QtGui.QLabel(self.page4)
        self.label_44.setGeometry(QtCore.QRect(10, 520, 751, 131))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_44.setFont(font)
        self.label_44.setFrameShape(QtGui.QFrame.WinPanel)
        self.label_44.setLineWidth(1)
        self.label_44.setMidLineWidth(0)
        self.label_44.setWordWrap(False)
        self.label_44.setObjectName(_fromUtf8("label_44"))
        self.line_9 = QtGui.QFrame(self.page4)
        self.line_9.setGeometry(QtCore.QRect(-10, 490, 821, 20))
        self.line_9.setFrameShape(QtGui.QFrame.HLine)
        self.line_9.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_9.setObjectName(_fromUtf8("line_9"))
        self.label_45 = QtGui.QLabel(self.page4)
        self.label_45.setGeometry(QtCore.QRect(70, 250, 91, 31))
        self.label_45.setObjectName(_fromUtf8("label_45"))
        self.label_32 = QtGui.QLabel(self.page4)
        self.label_32.setGeometry(QtCore.QRect(300, 540, 171, 111))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_32.setFont(font)
        self.label_32.setObjectName(_fromUtf8("label_32"))
        self.textEdit_26 = QtGui.QTextEdit(self.page4)
        self.textEdit_26.setGeometry(QtCore.QRect(200, 400, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.textEdit_26.setFont(font)
        self.textEdit_26.setTabChangesFocus(True)
        self.textEdit_26.setObjectName(_fromUtf8("textEdit_26"))
        self.label_61 = QtGui.QLabel(self.page4)
        self.label_61.setGeometry(QtCore.QRect(160, 70, 181, 51))
        self.label_61.setObjectName(_fromUtf8("label_61"))
        self.label_62 = QtGui.QLabel(self.page4)
        self.label_62.setGeometry(QtCore.QRect(70, 130, 91, 41))
        self.label_62.setObjectName(_fromUtf8("label_62"))
        self.label_63 = QtGui.QLabel(self.page4)
        self.label_63.setGeometry(QtCore.QRect(230, 130, 21, 31))
        self.label_63.setObjectName(_fromUtf8("label_63"))
        self.textEdit_27 = QtGui.QTextEdit(self.page4)
        self.textEdit_27.setGeometry(QtCore.QRect(250, 130, 61, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.textEdit_27.setFont(font)
        self.textEdit_27.setTabChangesFocus(True)
        self.textEdit_27.setObjectName(_fromUtf8("textEdit_27"))
        self.label_64 = QtGui.QLabel(self.page4)
        self.label_64.setGeometry(QtCore.QRect(320, 130, 71, 41))
        self.label_64.setObjectName(_fromUtf8("label_64"))
        self.label_70 = QtGui.QLabel(self.page4)
        self.label_70.setGeometry(QtCore.QRect(720, 190, 61, 31))
        self.label_70.setObjectName(_fromUtf8("label_70"))
        self.label_73 = QtGui.QLabel(self.page4)
        self.label_73.setGeometry(QtCore.QRect(380, 140, 41, 21))
        self.label_73.setObjectName(_fromUtf8("label_73"))
        self.label_38 = QtGui.QLabel(self.page4)
        self.label_38.setGeometry(QtCore.QRect(100, 190, 41, 51))
        self.label_38.setObjectName(_fromUtf8("label_38"))
        self.label_77 = QtGui.QLabel(self.page4)
        self.label_77.setGeometry(QtCore.QRect(480, 540, 271, 81))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_77.setFont(font)
        self.label_77.setObjectName(_fromUtf8("label_77"))
        self.toolBox.addItem(self.page4, _fromUtf8(""))
        self.page5 = QtGui.QWidget()
        self.page5.setGeometry(QtCore.QRect(0, 0, 801, 651))
        self.page5.setObjectName(_fromUtf8("page5"))
        self.line_10 = QtGui.QFrame(self.page5)
        self.line_10.setGeometry(QtCore.QRect(-10, 490, 821, 20))
        self.line_10.setFrameShape(QtGui.QFrame.HLine)
        self.line_10.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_10.setObjectName(_fromUtf8("line_10"))
        self.pushButton_14 = QtGui.QPushButton(self.page5)
        self.pushButton_14.setGeometry(QtCore.QRect(460, 210, 141, 61))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_14.setFont(font)
        self.pushButton_14.setObjectName(_fromUtf8("pushButton_14"))
        self.label_46 = QtGui.QLabel(self.page5)
        self.label_46.setGeometry(QtCore.QRect(10, 60, 111, 61))
        self.label_46.setObjectName(_fromUtf8("label_46"))
        self.line_11 = QtGui.QFrame(self.page5)
        self.line_11.setGeometry(QtCore.QRect(430, 60, 20, 441))
        self.line_11.setFrameShape(QtGui.QFrame.VLine)
        self.line_11.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_11.setObjectName(_fromUtf8("line_11"))
        self.line_12 = QtGui.QFrame(self.page5)
        self.line_12.setGeometry(QtCore.QRect(-13, 50, 831, 20))
        self.line_12.setFrameShape(QtGui.QFrame.HLine)
        self.line_12.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_12.setObjectName(_fromUtf8("line_12"))
        self.pushButton_16 = QtGui.QPushButton(self.page5)
        self.pushButton_16.setGeometry(QtCore.QRect(460, 290, 141, 51))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_16.setFont(font)
        self.pushButton_16.setObjectName(_fromUtf8("pushButton_16"))
        self.textEdit_21 = QtGui.QTextEdit(self.page5)
        self.textEdit_21.setGeometry(QtCore.QRect(620, 190, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.textEdit_21.setFont(font)
        self.textEdit_21.setTabChangesFocus(True)
        self.textEdit_21.setObjectName(_fromUtf8("textEdit_21"))
        self.label_53 = QtGui.QLabel(self.page5)
        self.label_53.setGeometry(QtCore.QRect(140, 0, 541, 51))
        self.label_53.setObjectName(_fromUtf8("label_53"))
        self.pushButton_17 = QtGui.QPushButton(self.page5)
        self.pushButton_17.setGeometry(QtCore.QRect(620, 270, 161, 91))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_17.setFont(font)
        self.pushButton_17.setObjectName(_fromUtf8("pushButton_17"))
        self.label_55 = QtGui.QLabel(self.page5)
        self.label_55.setGeometry(QtCore.QRect(460, 110, 351, 61))
        self.label_55.setObjectName(_fromUtf8("label_55"))
        self.label_56 = QtGui.QLabel(self.page5)
        self.label_56.setGeometry(QtCore.QRect(20, 520, 771, 131))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_56.setFont(font)
        self.label_56.setFrameShape(QtGui.QFrame.WinPanel)
        self.label_56.setLineWidth(1)
        self.label_56.setMidLineWidth(0)
        self.label_56.setWordWrap(False)
        self.label_56.setObjectName(_fromUtf8("label_56"))
        self.label_65 = QtGui.QLabel(self.page5)
        self.label_65.setGeometry(QtCore.QRect(250, 150, 21, 31))
        self.label_65.setObjectName(_fromUtf8("label_65"))
        self.label_66 = QtGui.QLabel(self.page5)
        self.label_66.setGeometry(QtCore.QRect(0, 150, 71, 31))
        self.label_66.setObjectName(_fromUtf8("label_66"))
        self.textEdit_28 = QtGui.QTextEdit(self.page5)
        self.textEdit_28.setGeometry(QtCore.QRect(180, 150, 61, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.textEdit_28.setFont(font)
        self.textEdit_28.setTabChangesFocus(True)
        self.textEdit_28.setObjectName(_fromUtf8("textEdit_28"))
        self.textEdit_29 = QtGui.QTextEdit(self.page5)
        self.textEdit_29.setGeometry(QtCore.QRect(270, 150, 61, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.textEdit_29.setFont(font)
        self.textEdit_29.setTabChangesFocus(True)
        self.textEdit_29.setObjectName(_fromUtf8("textEdit_29"))
        self.label_67 = QtGui.QLabel(self.page5)
        self.label_67.setGeometry(QtCore.QRect(340, 150, 71, 41))
        self.label_67.setObjectName(_fromUtf8("label_67"))
        self.label_68 = QtGui.QLabel(self.page5)
        self.label_68.setGeometry(QtCore.QRect(180, 100, 181, 51))
        self.label_68.setObjectName(_fromUtf8("label_68"))
        self.textEdit_30 = QtGui.QTextEdit(self.page5)
        self.textEdit_30.setGeometry(QtCore.QRect(210, 370, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.textEdit_30.setFont(font)
        self.textEdit_30.setTabChangesFocus(True)
        self.textEdit_30.setObjectName(_fromUtf8("textEdit_30"))
        self.textEdit_19 = QtGui.QTextEdit(self.page5)
        self.textEdit_19.setGeometry(QtCore.QRect(210, 270, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.textEdit_19.setFont(font)
        self.textEdit_19.setTabChangesFocus(True)
        self.textEdit_19.setObjectName(_fromUtf8("textEdit_19"))
        self.textEdit_20 = QtGui.QTextEdit(self.page5)
        self.textEdit_20.setGeometry(QtCore.QRect(210, 320, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.textEdit_20.setFont(font)
        self.textEdit_20.setTabChangesFocus(True)
        self.textEdit_20.setObjectName(_fromUtf8("textEdit_20"))
        self.textEdit_23 = QtGui.QTextEdit(self.page5)
        self.textEdit_23.setGeometry(QtCore.QRect(210, 220, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.textEdit_23.setFont(font)
        self.textEdit_23.setTabChangesFocus(True)
        self.textEdit_23.setObjectName(_fromUtf8("textEdit_23"))
        self.label_49 = QtGui.QLabel(self.page5)
        self.label_49.setGeometry(QtCore.QRect(80, 280, 91, 31))
        self.label_49.setObjectName(_fromUtf8("label_49"))
        self.label_50 = QtGui.QLabel(self.page5)
        self.label_50.setGeometry(QtCore.QRect(330, 280, 91, 31))
        self.label_50.setObjectName(_fromUtf8("label_50"))
        self.label_52 = QtGui.QLabel(self.page5)
        self.label_52.setGeometry(QtCore.QRect(330, 330, 91, 31))
        self.label_52.setObjectName(_fromUtf8("label_52"))
        self.textEdit_31 = QtGui.QTextEdit(self.page5)
        self.textEdit_31.setGeometry(QtCore.QRect(80, 150, 61, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.textEdit_31.setFont(font)
        self.textEdit_31.setTabChangesFocus(True)
        self.textEdit_31.setObjectName(_fromUtf8("textEdit_31"))
        self.label_69 = QtGui.QLabel(self.page5)
        self.label_69.setGeometry(QtCore.QRect(150, 150, 31, 41))
        self.label_69.setObjectName(_fromUtf8("label_69"))
        self.label_54 = QtGui.QLabel(self.page5)
        self.label_54.setGeometry(QtCore.QRect(330, 380, 91, 31))
        self.label_54.setObjectName(_fromUtf8("label_54"))
        self.label_47 = QtGui.QLabel(self.page5)
        self.label_47.setGeometry(QtCore.QRect(300, 540, 261, 111))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_47.setFont(font)
        self.label_47.setObjectName(_fromUtf8("label_47"))
        self.label_71 = QtGui.QLabel(self.page5)
        self.label_71.setGeometry(QtCore.QRect(730, 190, 61, 31))
        self.label_71.setObjectName(_fromUtf8("label_71"))
        self.label_72 = QtGui.QLabel(self.page5)
        self.label_72.setGeometry(QtCore.QRect(400, 160, 41, 21))
        self.label_72.setObjectName(_fromUtf8("label_72"))
        self.label_51 = QtGui.QLabel(self.page5)
        self.label_51.setGeometry(QtCore.QRect(110, 220, 41, 51))
        self.label_51.setObjectName(_fromUtf8("label_51"))
        self.label_78 = QtGui.QLabel(self.page5)
        self.label_78.setGeometry(QtCore.QRect(80, 330, 91, 31))
        self.label_78.setObjectName(_fromUtf8("label_78"))
        self.label_48 = QtGui.QLabel(self.page5)
        self.label_48.setGeometry(QtCore.QRect(80, 380, 91, 31))
        self.label_48.setObjectName(_fromUtf8("label_48"))
        self.label_79 = QtGui.QLabel(self.page5)
        self.label_79.setGeometry(QtCore.QRect(560, 540, 231, 21))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_79.setFont(font)
        self.label_79.setObjectName(_fromUtf8("label_79"))
        self.toolBox.addItem(self.page5, _fromUtf8(""))
        self.line_14 = QtGui.QFrame(self.centralwidget)
        self.line_14.setGeometry(QtCore.QRect(-20, 900, 1661, 20))
        self.line_14.setFrameShape(QtGui.QFrame.HLine)
        self.line_14.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_14.setObjectName(_fromUtf8("line_14"))
        self.textEdit_24 = QtGui.QTextEdit(self.centralwidget)
        self.textEdit_24.setGeometry(QtCore.QRect(840, 50, 781, 851))
        self.textEdit_24.setReadOnly(True)
        self.textEdit_24.setObjectName(_fromUtf8("textEdit_24"))
        self.label_74 = QtGui.QLabel(self.centralwidget)
        self.label_74.setGeometry(QtCore.QRect(990, 10, 551, 41))
        self.label_74.setObjectName(_fromUtf8("label_74"))
        self.line_15 = QtGui.QFrame(self.centralwidget)
        self.line_15.setGeometry(QtCore.QRect(-40, 0, 1681, 21))
        self.line_15.setFrameShape(QtGui.QFrame.HLine)
        self.line_15.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_15.setObjectName(_fromUtf8("line_15"))
        self.line_13 = QtGui.QFrame(self.centralwidget)
        self.line_13.setGeometry(QtCore.QRect(809, 10, 31, 901))
        self.line_13.setFrameShape(QtGui.QFrame.VLine)
        self.line_13.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_13.setObjectName(_fromUtf8("line_13"))
        self.line_16 = QtGui.QFrame(self.centralwidget)
        self.line_16.setGeometry(QtCore.QRect(1630, 10, 31, 901))
        self.line_16.setFrameShape(QtGui.QFrame.VLine)
        self.line_16.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_16.setObjectName(_fromUtf8("line_16"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)


        self.retranslateUi(MainWindow)
        self.toolBox.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.textEdit, self.textEdit_2)
        MainWindow.setTabOrder(self.textEdit_2, self.textEdit_3)
        MainWindow.setTabOrder(self.textEdit_3, self.textEdit_4)
        MainWindow.setTabOrder(self.textEdit_4, self.textEdit_5)
        MainWindow.setTabOrder(self.textEdit_5, self.textEdit_6)
        MainWindow.setTabOrder(self.textEdit_6, self.pushButton)
        MainWindow.setTabOrder(self.pushButton, self.pushButton_2)
        MainWindow.setTabOrder(self.pushButton_2, self.pushButton_4)
        MainWindow.setTabOrder(self.pushButton_4, self.textEdit_12)
        MainWindow.setTabOrder(self.textEdit_12, self.textEdit_8)
        MainWindow.setTabOrder(self.textEdit_8, self.textEdit_10)
        MainWindow.setTabOrder(self.textEdit_10, self.textEdit_25)
        MainWindow.setTabOrder(self.textEdit_25, self.textEdit_9)
        MainWindow.setTabOrder(self.textEdit_9, self.textEdit_11)
        MainWindow.setTabOrder(self.textEdit_11, self.textEdit_7)
        MainWindow.setTabOrder(self.textEdit_7, self.pushButton_5)
        MainWindow.setTabOrder(self.pushButton_5, self.pushButton_7)
        MainWindow.setTabOrder(self.pushButton_7, self.pushButton_6)
        MainWindow.setTabOrder(self.pushButton_6, self.textEdit_14)
        MainWindow.setTabOrder(self.textEdit_14, self.textEdit_27)
        MainWindow.setTabOrder(self.textEdit_27, self.textEdit_15)
        MainWindow.setTabOrder(self.textEdit_15, self.textEdit_16)
        MainWindow.setTabOrder(self.textEdit_16, self.textEdit_18)
        MainWindow.setTabOrder(self.textEdit_18, self.textEdit_17)
        MainWindow.setTabOrder(self.textEdit_17, self.textEdit_26)
        MainWindow.setTabOrder(self.textEdit_26, self.textEdit_13)
        MainWindow.setTabOrder(self.textEdit_13, self.pushButton_12)
        MainWindow.setTabOrder(self.pushButton_12, self.pushButton_11)
        MainWindow.setTabOrder(self.pushButton_11, self.pushButton_13)
        MainWindow.setTabOrder(self.pushButton_13, self.textEdit_31)
        MainWindow.setTabOrder(self.textEdit_31, self.textEdit_28)
        MainWindow.setTabOrder(self.textEdit_28, self.textEdit_29)
        MainWindow.setTabOrder(self.textEdit_29, self.textEdit_23)
        MainWindow.setTabOrder(self.textEdit_23, self.textEdit_19)
        MainWindow.setTabOrder(self.textEdit_19, self.textEdit_20)
        MainWindow.setTabOrder(self.textEdit_20, self.textEdit_30)
        MainWindow.setTabOrder(self.textEdit_30, self.textEdit_21)
        MainWindow.setTabOrder(self.textEdit_21, self.pushButton_14)
        MainWindow.setTabOrder(self.pushButton_14, self.pushButton_16)
        MainWindow.setTabOrder(self.pushButton_16, self.pushButton_17)
        MainWindow.setTabOrder(self.pushButton_17, self.textEdit_24)
        MainWindow.setTabOrder(self.textEdit_24, self.pushButton_9)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("Wykresy Haigha", "Wykresy Haigha", None))
        self.label_16.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:22pt;\">Program do obliczeń zagadnień<br/></span><span style=\" font-size:22pt; font-weight:600; font-style:italic;\">WYTRZYMAŁOŚCI ZMĘCZENIOWEJ</span><span style=\" font-size:22pt;\">.<br/><br/></span><span style=\" font-size:16pt;\">Przejdź do wyboru poniższych<br/>wielkości aby wprowadzić dane.</span><span style=\" font-size:22pt;\"><br/></span></p></body></html>", None))
        self.pushButton_9.setText(_translate("MainWindow", "Pomoc", None))
        self.label_20.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">Aby uzyskać opis programu kliknij </span></p></body></html>", None))
        self.label_15.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600; font-style:italic;\">Wybierz szukaną wielkość:</span></p></body></html>", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page1), _translate("MainWindow", "                                                                          Pomoc", None))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:11pt;\">R</span><span style=\" font-size:11pt; vertical-align:sub;\">e</span></p></body></html>", None))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600; font-style:italic;\">Współczynnik</span></p></body></html>", None))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600; font-style:italic;\">Współczynnik</span></p></body></html>", None))
        self.label_8.setText(_translate("MainWindow", "<html><head/><body><p>MPa </p></body></html>", None))
        self.label_12.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">MPa</span></p></body></html>", None))
        self.label_10.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600;\">Dane:</span></p></body></html>", None))
        self.pushButton.setText(_translate("MainWindow", "Oblicz/ Rozwiązanie", None))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:11pt;\">σ </span><span style=\" font-size:11pt; vertical-align:sub;\">max </span></p></body></html>", None))
        self.label_11.setText(_translate("MainWindow", "<html><head/><body><p>MPa</p></body></html>", None))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:11pt;\">σ </span><span style=\" font-size:11pt; vertical-align:sub;\">min </span></p></body></html>", None))
        self.label_14.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">MPa</span></p></body></html>", None))
        self.label_7.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:11pt;\">Z</span><span style=\" font-size:11pt; vertical-align:sub;\">rj </span></p></body></html>", None))
        self.label_13.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">MPa</span></p></body></html>", None))
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:11pt;\">Z</span><span style=\" font-size:11pt; vertical-align:sub;\">rc </span></p></body></html>", None))
        self.label_9.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-style:italic; text-decoration: underline;\">Legenda</span><span style=\" font-size:12pt; font-style:italic;\"><br/></span></p><p>Re - granica plastyczności</p><p>Zrc - wytrzymałość na ściskanie-rozciąganie</p><p>Zrj - wytrzymałość na pulsacyjne rozciąganie </p><p><br/></p></body></html>", None))
        self.pushButton_2.setText(_translate("MainWindow", "Wykres Haigha", None))
        self.pushButton_4.setText(_translate("MainWindow", "Rozwiąż zadanie", None))
        self.label_75.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:9pt;\">σ </span><span style=\" font-size:9pt; vertical-align:sub;\">max</span>- naprężenie maksymalne</p><p><span style=\" font-size:9pt;\">σ </span><span style=\" font-size:9pt; vertical-align:sub;\">min</span>- naprężenie minimalne</p><p><br/></p></body></html>", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page2), _translate("MainWindow", "Współczynnik bezpieczeństwa. Rozciaganie - ściskanie. ", None))
        self.label_17.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600; font-style:italic;\">Przekrój poprzeczny</span></p></body></html>", None))
        self.pushButton_5.setText(_translate("MainWindow", "Oblicz/ Rozwiązanie", None))
        self.label_18.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600; font-style:italic;\">Pole przekroju</span></p></body></html>", None))
        self.pushButton_6.setText(_translate("MainWindow", "Rozwiąż zadanie", None))
        self.pushButton_7.setText(_translate("MainWindow", "Wykres Haigha", None))
        self.label_19.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-style:italic; text-decoration: underline;\">Legenda</span><span style=\" font-size:12pt; font-style:italic;\"><br/></span></p><p>Pmax - siła maksymalna</p><p>Pmin - siła minimalna</p><p>Zrc - wytrzymałośc na ściskanie-rozciąganie</p></body></html>", None))
        self.label_21.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">MPa</span></p></body></html>", None))
        self.label_22.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600;\">Dane:</span></p></body></html>", None))
        self.label_23.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">MPa</span></p></body></html>", None))
        self.label_26.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">P</span><span style=\" font-size:12pt; vertical-align:sub;\">min</span></p></body></html>", None))
        self.label_27.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\"> kN </span></p></body></html>", None))
        self.label_28.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">δ </span></p></body></html>", None))
        self.label_29.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">P</span><span style=\" font-size:12pt; vertical-align:sub;\">max</span></p></body></html>", None))
        self.label_30.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\"> kN </span></p></body></html>", None))
        self.label_58.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">MPa</span></p></body></html>", None))
        self.label_59.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">R</span><span style=\" font-size:14pt; vertical-align:sub;\">e</span></p></body></html>", None))
        self.label_60.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:7pt;\">Re - granica plastyczności </span></p><p>Zrj - wytrzymałość na pulsacyjne rozciąganie</p><p><span style=\" font-size:7pt;\">δ - współczynnik bezpieczeństwa</span></p><p><br/></p></body></html>", None))
        self.label_57.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">mm</span><span style=\" font-size:14pt; vertical-align:super;\">2</span></p></body></html>", None))
        self.label_35.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Z</span><span style=\" font-size:12pt; vertical-align:sub;\">rc </span></p></body></html>", None))
        self.label_80.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Z</span><span style=\" font-size:12pt; vertical-align:sub;\">rj </span></p></body></html>", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page3), _translate("MainWindow", "Przekrój poprzeczny.  Rozciaganie - ściskanie. ", None))
        self.pushButton_11.setText(_translate("MainWindow", "Wykres Haigha", None))
        self.pushButton_12.setText(_translate("MainWindow", "Oblicz/ Rozwiązanie", None))
        self.label_24.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600; font-style:italic;\">Moment zginający/skręcający</span></p></body></html>", None))
        self.pushButton_13.setText(_translate("MainWindow", "Rozwiąż zadanie", None))
        self.label_25.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:600; font-style:italic;\">Dopuszczalna wartość momentu &quot;M&quot;</span></p></body></html>", None))
        self.label_31.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:11pt;\">Z</span><span style=\" font-size:11pt; vertical-align:sub;\">gj</span><span style=\" font-size:11pt;\">/</span><span style=\" font-size:11pt;\">Z</span><span style=\" font-size:11pt; vertical-align:sub;\">s</span><span style=\" font-size:11pt; vertical-align:sub;\">j</span></p></body></html>", None))
        self.label_36.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">MPa</span></p></body></html>", None))
        self.label_37.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600;\">Dane:</span></p></body></html>", None))
        self.label_39.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:11pt;\">R</span><span style=\" font-size:11pt; vertical-align:sub;\">e</span></p></body></html>", None))
        self.label_40.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:11pt;\">mm</span><span style=\" font-size:11pt; vertical-align:super;\">3</span></p></body></html>", None))
        self.label_41.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">MPa</span></p></body></html>", None))
        self.label_42.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:11pt;\">Z</span><span style=\" font-size:11pt; vertical-align:sub;\">go</span><span style=\" font-size:11pt;\">/</span><span style=\" font-size:11pt;\">Z</span><span style=\" font-size:11pt; vertical-align:sub;\">s</span><span style=\" font-size:11pt; vertical-align:sub;\">o</span></p></body></html>", None))
        self.label_43.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">MPa</span></p></body></html>", None))
        self.label_44.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-style:italic; text-decoration: underline;\">Legenda</span><span style=\" font-size:12pt; font-style:italic;\"><br/></span></p><p>Re - granica plastyczności</p><p>Zgo - wytrzymałość na wahadłowe zginanie</p><p>Zgj - wytrzymałość na pulsacyjne zginanie</p><p><br/></p></body></html>", None))
        self.label_45.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:11pt;\">W</span><span style=\" font-size:11pt; vertical-align:sub;\">g</span><span style=\" font-size:11pt;\">/W</span><span style=\" font-size:11pt; vertical-align:sub;\">s</span></p></body></html>", None))
        self.label_32.setText(_translate("MainWindow", "<html><head/><body><p>Mg - moment gnący</p><p>Wg - wskaźnik na zginanie</p><p>Ms - moment skręcający</p><p>Ws - wskaźnik na skręcanie</p><p><span style=\" font-size:7pt;\">δ - współczynnik bezpieczeństwa</span></p><p><br/></p></body></html>", None))
        self.label_61.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:11pt;\">Formuła momentu</span></p></body></html>", None))
        self.label_62.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:11pt;\">M</span><span style=\" font-size:11pt; vertical-align:sub;\">g</span><span style=\" font-size:11pt;\">/M</span><span style=\" font-size:11pt; vertical-align:sub;\">s </span><span style=\" font-size:11pt;\">=</span><span style=\" font-size:11pt; font-weight:600;\">M</span><span style=\" font-size:12pt;\">(</span></p></body></html>", None))
        self.label_63.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:11pt;\">+</span></p></body></html>", None))
        self.label_64.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:11pt;\">sin ωt</span><span style=\" font-size:12pt;\">)</span></p></body></html>", None))
        self.label_70.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">kNm</span></p></body></html>", None))
        self.label_73.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:11pt;\">kNm</span></p></body></html>", None))
        self.label_38.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">δ </span></p></body></html>", None))
        self.label_77.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:7pt;\">δ - współczynnik bezpieczeństwa</span></p><p>Zso - wytrzymałość na wahadłowe skręcanie</p><p>Zsj - wytrzymałość na pulsacyjne skręcanie<br/></p></body></html>", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page4), _translate("MainWindow", "Moment zginający / moment skręcający", None))
        self.pushButton_14.setText(_translate("MainWindow", "Oblicz/ Rozwiązanie", None))
        self.label_46.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600;\">Dane:</span></p></body></html>", None))
        self.pushButton_16.setText(_translate("MainWindow", "Wykres Haigha", None))
        self.label_53.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600; font-style:italic;\">Wskaźnik na skręcanie / zginanie</span></p></body></html>", None))
        self.pushButton_17.setText(_translate("MainWindow", "Rozwiąż zadanie", None))
        self.label_55.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600; font-style:italic;\">Wartość wskaźnika</span></p></body></html>", None))
        self.label_56.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-style:italic; text-decoration: underline;\">Legenda</span><span style=\" font-size:12pt; font-style:italic;\"><br/></span></p><p>Re - granica plastyczności</p><p>Zso - wytrzymałość na wahadłowe skręcanie</p><p>Zsj - wytrzymałość na pulsacyjne skręcanie</p><p><br/></p></body></html>", None))
        self.label_65.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:11pt;\">+</span></p></body></html>", None))
        self.label_66.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">M</span><span style=\" font-size:12pt; vertical-align:sub;\">s</span><span style=\" font-size:12pt;\">/M</span><span style=\" font-size:12pt; vertical-align:sub;\">g </span><span style=\" font-size:12pt;\">=</span><span style=\" font-size:12pt; vertical-align:sub;\"/></p></body></html>", None))
        self.label_67.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:11pt;\">sin ωt</span><span style=\" font-size:12pt;\">)</span></p></body></html>", None))
        self.label_68.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:11pt;\">Formuła momentu</span></p></body></html>", None))
        self.label_49.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:11pt;\">R</span><span style=\" font-size:11pt; vertical-align:sub;\">e</span></p></body></html>", None))
        self.label_50.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:11pt;\">mm</span><span style=\" font-size:11pt; vertical-align:super;\">3</span></p></body></html>", None))
        self.label_52.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">MPa</span></p></body></html>", None))
        self.label_69.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:11pt;\">x </span><span style=\" font-size:12pt;\">(</span></p></body></html>", None))
        self.label_54.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">MPa</span></p></body></html>", None))
        self.label_47.setText(_translate("MainWindow", "<html><head/><body><p>Ms - moment skręcający</p><p>Ms - moment zginający</p><p>Zgo - wytrzymałość na wahadłowe zginanie</p><p>Zgj - wytrzymałość na pulsacyjne zginanie</p><p><br/></p></body></html>", None))
        self.label_71.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">cm</span><span style=\" font-size:10pt; vertical-align:super;\">3</span></p></body></html>", None))
        self.label_72.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:11pt;\">kNm</span></p></body></html>", None))
        self.label_51.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:11pt;\">δ </span></p></body></html>", None))
        self.label_78.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:11pt;\">Z</span><span style=\" font-size:11pt; vertical-align:sub;\">gj</span><span style=\" font-size:11pt;\">/</span><span style=\" font-size:11pt;\">Z</span><span style=\" font-size:11pt; vertical-align:sub;\">s</span><span style=\" font-size:11pt; vertical-align:sub;\">j</span></p></body></html>", None))
        self.label_48.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:11pt;\">Z</span><span style=\" font-size:11pt; vertical-align:sub;\">go</span><span style=\" font-size:11pt;\">/</span><span style=\" font-size:11pt;\">Z</span><span style=\" font-size:11pt; vertical-align:sub;\">s</span><span style=\" font-size:11pt; vertical-align:sub;\">o</span></p></body></html>", None))
        self.label_79.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:7pt;\">δ - współczynnik bezpieczeństwa</span></p><p><br/></p></body></html>", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page5), _translate("MainWindow", "Wskaźnik na skręcanie / zginanie", None))
        self.textEdit_24.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.5pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Aby otrzymać rozwiązanie zadania oraz opis poszczególnych obliczeń<br /> wpisz dane wejściowe oraz kliknij oblicz.</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p></body></html>", None))
        self.label_74.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600; font-style:italic;\">Rozwiązanie</span></p></body></html>", None))
        self.pushButton.clicked.connect(self.obliczenia)
        self.pushButton_2.clicked.connect(self.wykres)
        self.pushButton_4.clicked.connect(self.obliczenia)
        self.pushButton_4.clicked.connect(self.wykres)
        self.pushButton_5.clicked.connect(self.obliczenia2)
        self.pushButton_7.clicked.connect(self.wykres2)
        self.pushButton_6.clicked.connect(self.obliczenia2)
        self.pushButton_6.clicked.connect(self.wykres2)
        self.pushButton_12.clicked.connect(self.obliczenia3)
        self.pushButton_11.clicked.connect(self.wykres3)
        self.pushButton_13.clicked.connect(self.obliczenia3)
        self.pushButton_13.clicked.connect(self.wykres3)
        self.pushButton_14.clicked.connect(self.obliczenia4)
        self.pushButton_16.clicked.connect(self.wykres4)
        self.pushButton_17.clicked.connect(self.obliczenia4)
        self.pushButton_17.clicked.connect(self.wykres4)
        self.pushButton_9.clicked.connect(self.okienkopomocy)


#------ Open support window
        
    def okienkopomocy(self):
        
        self.MainWindow2 = QtGui.QMainWindow()
        self.ui2 = Ui_MainWindow2()
        self.ui2.setupUi(self.MainWindow2)
        self.MainWindow2.show()


#------ Calculating in first page. Fatigue compression - outstretch. Safety factor is output datum.   
        
    def obliczenia(self):
        sigmamax = float(str(self.textEdit.toPlainText()).replace(",","."))
        sigmamin = float(str(self.textEdit_2.toPlainText()).replace(",","."))
        Re = float(str(self.textEdit_3.toPlainText()).replace(",","."))
        Zrc = float(str(self.textEdit_4.toPlainText()).replace(",","."))
        Zrj = float(str(self.textEdit_5.toPlainText()).replace(",","."))
        sigmam0=float(0.5*(sigmamax+sigmamin))
        sigmaa0=float(0.5*(sigmamax-sigmamin))
        sigmaa=float(sigmaa0/sigmam0)
        rgp=float((2*Zrc-Zrj)/Zrj) #equation upper straight
        rgp_str=str(round(rgp,3))
        sigmamax_str = str(round(sigmamax,3))
        sigmamin_str = str(round(sigmamin,3))
        Re_str = str(round(Re,3))
        Zrc_str = str(round(Zrc))
        Zrj_str = str(round(Zrj,3))
        sigmam0_str= str(round(sigmam0,3))
        sigmaa0_str= str(round(sigmaa0,3))
        sigmaa_str= str(round(sigmaa,3))
        
        if sigmaa > 0: #condition for right side of graph
                    
            sigmam=float(Zrc/((sigmaa0/sigmam0)+((2*Zrc-Zrj)/Zrj)))
            sigmam_str=str(round(sigmam,3))
            x2=float((Zrc-Re)/(-1+((2*Zrc-Zrj)/Zrj)))
            if sigmam > x2:     #condition for points place on particular straight
                sigmam=float(Re/(1+(sigmaa0/sigmam0)))
                sigmam_str=str(round(sigmam,3))
                sigmaad=float(sigmam*sigmaa)
                sigmaad_str=str(round(sigmaad,3))
                wspolczynnik=float(sigmam/sigmam0)
                wspolczynnik_str = str(round(wspolczynnik,3))

                # Description result for user.
                self.textEdit_24.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.5pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\">1)</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\">Wyznaczamy współrzędne punktu cyklu obciążeniowego z naprężenia minimalnego i naprężenia     maksymalnego:</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\"><br /><br />σ</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt; vertical-align:sub;\">m(0)</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\">=0.5(σ</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt; vertical-align:sub;\">n max </span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\">+ σ</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt; vertical-align:sub;\">n min</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\">) ="+sigmam0_str+" MPa\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\"><br />σ</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt; vertical-align:sub;\">a(0)</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\">=0.5(σ</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt; vertical-align:sub;\">n max -</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\"> σ</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt; vertical-align:sub;\">n min</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\">) = "+sigmaa0_str+" MPa\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Calibri,sans-serif\'; font-size:11pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Calibri,sans-serif\'; font-size:11pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\">2) </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\">Wyznaczamy równanie prostej obciążeniowej, która przechodzi przez powyższy punkt:<br /></span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\">σ</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt; vertical-align:sub;\">a</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\">=( σ</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt; vertical-align:sub;\">a(0) </span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\">/ σ</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt; vertical-align:sub;\">m(0) </span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\">)*σ</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt; vertical-align:sub;\">m </span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\">= "+sigmaa_str+"<span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\"> σ</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt; vertical-align:sub;\">m </span>"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Calibri,sans-serif\'; font-size:11pt;\"><br /></p>\n"
"<p align=\"right\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Calibri,sans-serif\'; font-size:9pt;\"><br /></p>\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri,sans-serif\'; font-size:9pt;\">(Prosta ta posiada wartość dodatnią dlatego cały wykres będzie rysowany po dodatniej stronie wartości na osi &quot;X&quot;.)</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\">3)</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Calibri,sans-serif\'; font-size:11pt;\"><br /></p>\n""<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\"> Równanie górnej prostej ograniczającej obliczamy ze wzoru:<br /></span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\">σ</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt; vertical-align:sub;\">a</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\">=Z</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt; vertical-align:sub;\">rc </span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\"> -σ</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt; vertical-align:sub;\">m</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\">* (2Z</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt; vertical-align:sub;\">rc </span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\">- Z</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt; vertical-align:sub;\">rj</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\">)/Z</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt; vertical-align:sub;\">rj </span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\">= "+Zrc_str+" - "+rgp_str+"<span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\"> σ</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt; vertical-align:sub;\">m </span>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Calibri,sans-serif\'; font-size:11pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\"><br />(W przypadku innych obciążeń, podstawiamy odpowiednie zmienne materiałowe </span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:10pt;\">Z</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:10pt; vertical-align:sub;\">so</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:10pt;\">, Z</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:10pt; vertical-align:sub;\">sj</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:10pt;\">, Z</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:10pt; vertical-align:sub;\">rc</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:10pt;\">, Z</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:10pt; vertical-align:sub;\">rj</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:9pt; vertical-align:sub;\">  </span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:9pt;\">. </span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:10pt;\">To samo dotyczy wykresu.</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:9pt;\">)<br /><br /></span></p></body></html>"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\">4)</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\"> Rysujemy proste przerywane na wykresie (X - σ</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt; vertical-align:sub;\">m</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\">; Y - σ</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt; vertical-align:sub;\">a</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\">):<br />    a) prostej obciążeniowej z pkt.2</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\">    b)prostej ograniczającej z pkt.3</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\">    c)prostej od punktu wartości Re na osi X do punktu o wartości Re na osi Y</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Calibri,sans-serif\'; font-size:11pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\">5)</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\"> Prosta obciążeniowa w tym przypadku przecina się z prostą ograniczającą wartościami granicy plastyczności Re, zatem przyrównujemy obie proste w celu uzyskania punktu P</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt; vertical-align:sub;\">d</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\">:</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\"><br /><br />"+sigmaa_str+"<span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\"> σ</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt; vertical-align:sub;\">m </span>"+" = "+Re_str+" - "+"<span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\"> σ</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt; vertical-align:sub;\">m </span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Calibri,sans-serif\'; font-size:11pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\">6)</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\"> Wyliczamy współrzędne punktu P</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt; vertical-align:sub;\">d</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\">:</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Calibri,sans-serif\'; font-size:11pt;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\">σ</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt; vertical-align:sub;\">m(d)</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\">= "+sigmam_str+" MPa "+ ", σ</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt; vertical-align:sub;\">a(d)</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\"> = "+sigmaad_str+" MPa "+" </span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Calibri,sans-serif\'; font-size:11pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\">7)</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt; font-weight:600;\"> Współczynnik bezpieczeństwa</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\">:<br /></span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\"><br />δ = σ</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt; vertical-align:sub;\">m(d)</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\">/σ</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt; vertical-align:sub;\">m(0) </span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\">= "+wspolczynnik_str+"</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Calibri,sans-serif\'; font-size:11pt;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Calibri,sans-serif\'; font-size:11pt;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Calibri,sans-serif\'; font-size:11pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Calibri,sans-serif\'; font-size:11pt;\"><br /></p></body></html>", None))

            else:
                sigmaad=float(sigmam*sigmaa)
                sigmaad_str=str(round(sigmaad,3))
                wspolczynnik=float(sigmam/sigmam0)
                wspolczynnik_str = str(round(wspolczynnik,3))
                self.textEdit_24.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.5pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\">1)</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\">Wyznaczamy współrzędne punktu cyklu obciążeniowego z naprężenia minimalnego i naprężenia     maksymalnego:</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\"><br /><br />σ</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt; vertical-align:sub;\">m(0)</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\">=0.5(σ</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt; vertical-align:sub;\">n max </span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\">+ σ</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt; vertical-align:sub;\">n min</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\">) ="+sigmam0_str+" MPa\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\"><br />σ</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt; vertical-align:sub;\">a(0)</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\">=0.5(σ</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt; vertical-align:sub;\">n max -</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\"> σ</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt; vertical-align:sub;\">n min</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\">) = "+sigmaa0_str+" MPa\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Calibri,sans-serif\'; font-size:11pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Calibri,sans-serif\'; font-size:11pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\">2) </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\">Wyznaczamy równanie prostej obciążeniowej, która przechodzi przez powyższy punkt:<br /></span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\">σ</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt; vertical-align:sub;\">a</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\">=( σ</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt; vertical-align:sub;\">a(0) </span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\">/ σ</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt; vertical-align:sub;\">m(0) </span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\">)*σ</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt; vertical-align:sub;\">m </span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\">= "+sigmaa_str+"<span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\"> σ</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt; vertical-align:sub;\">m </span>"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Calibri,sans-serif\'; font-size:11pt;\"><br /></p>\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri,sans-serif\'; font-size:9pt;\">(Prosta ta posiada wartość dodatnią dlatego cały wykres będzie rysowany po dodatniej stronie wartości na osi &quot;X&quot;.)</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\">3)</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\"> Równanie górnej prostej ograniczającej obliczamy ze wzoru:<br /></span></p>\n"

"<p align=\"right\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Calibri,sans-serif\'; font-size:9pt;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Calibri,sans-serif\'; font-size:11pt;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\">σ</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt; vertical-align:sub;\">a</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\">=Z</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt; vertical-align:sub;\">rc </span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\"> -σ</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt; vertical-align:sub;\">m</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\">* (2Z</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt; vertical-align:sub;\">rc </span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\">- Z</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt; vertical-align:sub;\">rj</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\">)/Z</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt; vertical-align:sub;\">rj </span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\">= "+Zrc_str+" - "+rgp_str+"<span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\"> σ</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt; vertical-align:sub;\">m </span>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Calibri,sans-serif\'; font-size:11pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\"><br />(W przypadku innych obciążeń, podstawiamy odpowiednie zmienne materiałowe </span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:10pt;\">Z</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:10pt; vertical-align:sub;\">so</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:10pt;\">, Z</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:10pt; vertical-align:sub;\">sj</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:10pt;\">, Z</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:10pt; vertical-align:sub;\">rc</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:10pt;\">, Z</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:10pt; vertical-align:sub;\">rj</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:9pt; vertical-align:sub;\">  </span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:9pt;\">. </span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:10pt;\">To samo dotyczy wykresu.</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:9pt;\">)<br /><br /></span></p></body></html>"

"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\">4)</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\"> Rysujemy proste przerywane na wykresie (X - σ</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt; vertical-align:sub;\">m</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\">; Y - σ</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt; vertical-align:sub;\">a</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\">):<br />    a) prostej obciążeniowej z pkt.2</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\">    b)prostej ograniczającej z pkt.3</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\">    c)prostej od punktu wartości Re na osi X do punktu o wartości Re na osi Y</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Calibri,sans-serif\'; font-size:11pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\">5)</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\"> Prosta obciążeniowa w tym przypadku przecina się z górną prostą ograniczającą, zatem przyrównujemy obie proste w celu uzyskania punktu P</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt; vertical-align:sub;\">d</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\">:</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\"><br /><br />"+sigmaa_str+"<span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\"> σ</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt; vertical-align:sub;\">m </span>"+" = "+Zrc_str+" - "+rgp_str+"<span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\"> σ</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt; vertical-align:sub;\">m </span>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Calibri,sans-serif\'; font-size:11pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\">6)</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\"> Wyliczamy współrzędne punktu P</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt; vertical-align:sub;\">d</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\">:</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Calibri,sans-serif\'; font-size:11pt;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\">σ</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt; vertical-align:sub;\">m(d)</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\">= "+sigmam_str+" MPa , σ</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt; vertical-align:sub;\">a(d)</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\"> = "+sigmaad_str+" MPa </span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Calibri,sans-serif\'; font-size:11pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\">7)</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt; font-weight:600;\"> Współczynnik bezpieczeństwa</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\">:<br /></span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\"><br />δ = σ</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt; vertical-align:sub;\">m(d)</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\">/σ</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt; vertical-align:sub;\">m(0) </span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\">= "+wspolczynnik_str+"</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Calibri,sans-serif\'; font-size:11pt;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Calibri,sans-serif\'; font-size:11pt;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Calibri,sans-serif\'; font-size:11pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Calibri,sans-serif\'; font-size:11pt;\"><br /></p></body></html>", None))
              
        else:

            sigmam=float(Zrc/((sigmaa0/sigmam0)+((2*Zrc-Zrj)/Zrj)))
            sigmam_str=str(round(sigmam,3))
            x2=float((Zrc-Re)/(1+((2*Zrc-Zrj)/Zrj)))
            
            if sigmam < x2:
                sigmam=float(Re/((sigmaa0/sigmam0)-1))
                sigmam_str=str(round(sigmam,3))
                sigmaad=float(sigmam*sigmaa)
                sigmaad_str=str(round(sigmaad,3))
                wspolczynnik=float(sigmam/sigmam0)
                wspolczynnik_str = str(round(wspolczynnik,3))
                self.textEdit_24.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.5pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\">1)</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\">Wyznaczamy współrzędne punktu cyklu obciążeniowego z naprężenia minimalnego i naprężenia     maksymalnego:</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\"><br /><br />σ</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt; vertical-align:sub;\">m(0)</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\">=0.5(σ</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt; vertical-align:sub;\">n max </span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\">+ σ</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt; vertical-align:sub;\">n min</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\">) ="+sigmam0_str+" MPa\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\"><br />σ</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt; vertical-align:sub;\">a(0)</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\">=0.5(σ</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt; vertical-align:sub;\">n max -</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\"> σ</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt; vertical-align:sub;\">n min</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\">) = "+sigmaa0_str+" MPa\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Calibri,sans-serif\'; font-size:11pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Calibri,sans-serif\'; font-size:11pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\">2) </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\">Wyznaczamy równanie prostej obciążeniowej, która przechodzi przez powyższy punkt:<br /></span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\">σ</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt; vertical-align:sub;\">a</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\">=( σ</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt; vertical-align:sub;\">a(0) </span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\">/ σ</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt; vertical-align:sub;\">m(0) </span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\">)*σ</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt; vertical-align:sub;\">m </span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\">= "+sigmaa_str+"<span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\"> σ</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt; vertical-align:sub;\">m </span>"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Calibri,sans-serif\'; font-size:11pt;\"><br /></p>\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri,sans-serif\'; font-size:9pt;\">(Prosta ta posiada wartość ujemną dlatego cały wykres będzie rysowany po ujemnej stronie wartości na osi &quot;X&quot;.)</span></p>\n"

"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\">3)</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\"> Równanie górnej prostej ograniczającej obliczamy ze wzoru:<br /></span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\">σ</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt; vertical-align:sub;\">a</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\">=Z</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt; vertical-align:sub;\">rc </span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\"> -σ</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt; vertical-align:sub;\">m</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\">* (2Z</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt; vertical-align:sub;\">rc </span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\">- Z</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt; vertical-align:sub;\">rj</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\">)/Z</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt; vertical-align:sub;\">rj </span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\">= "+Zrc_str+" - "+rgp_str+"<span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\"> σ</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt; vertical-align:sub;\">m </span>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Calibri,sans-serif\'; font-size:11pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\"><br />(W przypadku innych obciążeń, podstawiamy odpowiednie zmienne materiałowe </span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:10pt;\">Z</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:10pt; vertical-align:sub;\">so</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:10pt;\">, Z</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:10pt; vertical-align:sub;\">sj</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:10pt;\">, Z</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:10pt; vertical-align:sub;\">rc</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:10pt;\">, Z</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:10pt; vertical-align:sub;\">rj</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:9pt; vertical-align:sub;\">  </span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:9pt;\">. </span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:10pt;\">To samo dotyczy wykresu.</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:9pt;\">)<br /><br /></span></p></body></html>"

"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\">4)</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\"> Rysujemy proste przerywane na wykresie (X - σ</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt; vertical-align:sub;\">m</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\">; Y - σ</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt; vertical-align:sub;\">a</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\">):<br />    a) prostej obciążeniowej z pkt.2</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\">    b)prostej ograniczającej z pkt.3</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\">    c)prostej od punktu wartości Re na osi X do punktu o wartości Re na osi Y</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Calibri,sans-serif\'; font-size:11pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\">5)</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\"> Prosta obciążeniowa w tym przypadku przecina się z prostą ograniczającą wartościami granicy plastyczności Re, zatem przyrównujemy obie proste w celu uzyskania punktu P</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt; vertical-align:sub;\">d</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\">:</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\"><br /><br />"+sigmaa_str+"<span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\"> σ</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt; vertical-align:sub;\">m </span>"+" = "+Re_str+" + "+"<span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\"> σ</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt; vertical-align:sub;\">m </span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Calibri,sans-serif\'; font-size:11pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\">6)</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\"> Wyliczamy współrzędne punktu P</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt; vertical-align:sub;\">d</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\">:</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Calibri,sans-serif\'; font-size:11pt;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\">σ</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt; vertical-align:sub;\">m(d)</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\">= "+sigmam_str+" MPa "+ ", σ</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt; vertical-align:sub;\">a(d)</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\"> = "+sigmaad_str+" MPa "+" </span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Calibri,sans-serif\'; font-size:11pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\">7)</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt; font-weight:600;\"> Współczynnik bezpieczeństwa</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\">:<br /></span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\"><br />δ = σ</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt; vertical-align:sub;\">m(d)</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\">/σ</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt; vertical-align:sub;\">m(0) </span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\">= "+wspolczynnik_str+"</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Calibri,sans-serif\'; font-size:11pt;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Calibri,sans-serif\'; font-size:11pt;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Calibri,sans-serif\'; font-size:11pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Calibri,sans-serif\'; font-size:11pt;\"><br /></p></body></html>", None))

            else:
                
                sigmaad=float(sigmam*sigmaa)
                sigmaad_str=str(round(sigmaad,3))
                wspolczynnik=float(sigmam/sigmam0)
                wspolczynnik_str = str(round(wspolczynnik,3))
                self.textEdit_24.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.5pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\">1)</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\">Wyznaczamy współrzędne punktu cyklu obciążeniowego z naprężenia minimalnego i naprężenia     maksymalnego:</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\"><br /><br />σ</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt; vertical-align:sub;\">m(0)</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\">=0.5(σ</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt; vertical-align:sub;\">n max </span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\">+ σ</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt; vertical-align:sub;\">n min</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\">) ="+sigmam0_str+" MPa\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\"><br />σ</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt; vertical-align:sub;\">a(0)</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\">=0.5(σ</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt; vertical-align:sub;\">n max -</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\"> σ</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt; vertical-align:sub;\">n min</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\">) = "+sigmaa0_str+" MPa\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Calibri,sans-serif\'; font-size:11pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Calibri,sans-serif\'; font-size:11pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\">2) </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\">Wyznaczamy równanie prostej obciążeniowej, która przechodzi przez powyższy punkt:<br /></span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\">σ</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt; vertical-align:sub;\">a</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\">=( σ</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt; vertical-align:sub;\">a(0) </span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\">/ σ</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt; vertical-align:sub;\">m(0) </span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\">)*σ</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt; vertical-align:sub;\">m </span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\">= "+sigmaa_str+"<span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\"> σ</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt; vertical-align:sub;\">m </span>"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Calibri,sans-serif\'; font-size:11pt;\"><br /></p>\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri,sans-serif\'; font-size:9pt;\">(Prosta ta posiada wartość ujemną dlatego cały wykres będzie rysowany po ujemnej stronie wartości na osi &quot;X&quot;.)</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\">3)</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\"> Równanie górnej prostej ograniczającej obliczamy ze wzoru:<br /></span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\">σ</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt; vertical-align:sub;\">a</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\">=Z</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt; vertical-align:sub;\">rc </span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\"> -σ</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt; vertical-align:sub;\">m</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\">* (2Z</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt; vertical-align:sub;\">rc </span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\">- Z</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt; vertical-align:sub;\">rj</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\">)/Z</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt; vertical-align:sub;\">rj </span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\">= "+Zrc_str+" - "+rgp_str+"<span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\"> σ</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt; vertical-align:sub;\">m </span>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Calibri,sans-serif\'; font-size:11pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\"><br />(W przypadku innych obciążeń, podstawiamy odpowiednie zmienne materiałowe </span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:10pt;\">Z</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:10pt; vertical-align:sub;\">so</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:10pt;\">, Z</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:10pt; vertical-align:sub;\">sj</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:10pt;\">, Z</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:10pt; vertical-align:sub;\">rc</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:10pt;\">, Z</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:10pt; vertical-align:sub;\">rj</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:9pt; vertical-align:sub;\">  </span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:9pt;\">. </span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:10pt;\">To samo dotyczy wykresu.</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:9pt;\">)<br /><br /></span></p></body></html>"

"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\">4)</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\"> Rysujemy proste przerywane na wykresie (X - σ</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt; vertical-align:sub;\">m</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\">; Y - σ</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt; vertical-align:sub;\">a</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\">):<br />    a) prostej obciążeniowej z pkt.2</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\">    b)prostej ograniczającej z pkt.3</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\">    c)prostej od punktu wartości -Re na osi X do punktu o wartości Re na osi Y</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Calibri,sans-serif\'; font-size:11pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\">5)</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\"> Prosta obciążeniowa w tym przypadku przecina się z górną prostą ograniczającą, zatem przyrównujemy obie proste w celu uzyskania punktu P</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt; vertical-align:sub;\">d</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\">:</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\"><br /><br />"+sigmaa_str+"<span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\"> σ</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt; vertical-align:sub;\">m </span>"+" = "+Zrc_str+" - "+rgp_str+"<span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\"> σ</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt; vertical-align:sub;\">m </span>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Calibri,sans-serif\'; font-size:11pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\">6)</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\"> Wyliczamy współrzędne punktu P</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt; vertical-align:sub;\">d</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\">:</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Calibri,sans-serif\'; font-size:11pt;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\">σ</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt; vertical-align:sub;\">m(d)</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\">= "+sigmam_str+" MPa , σ</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt; vertical-align:sub;\">a(d)</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\"> = "+sigmaad_str+" MPa </span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Calibri,sans-serif\'; font-size:11pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\">7)</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt; font-weight:600;\"> Współczynnik bezpieczeństwa</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\">:<br /></span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\"><br />δ = σ</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt; vertical-align:sub;\">m(d)</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\">/σ</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt; vertical-align:sub;\">m(0) </span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\">= "+wspolczynnik_str+"</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Calibri,sans-serif\'; font-size:11pt;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Calibri,sans-serif\'; font-size:11pt;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Calibri,sans-serif\'; font-size:11pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Calibri,sans-serif\'; font-size:11pt;\"><br /></p></body></html>", None))
                
        wspolczynnik=float(sigmam/sigmam0)
        wspolczynnik_str = str(round(wspolczynnik, 3))
        self.textEdit_6.setText(wspolczynnik_str)


#------ Calculating and determine graphs in first page. Fatigue compression - outstretch. 

    def wykres(self):
        sigmamax = float(str(self.textEdit.toPlainText()).replace(",","."))
        sigmamin = float(str(self.textEdit_2.toPlainText()).replace(",","."))
        Re = float(str(self.textEdit_3.toPlainText()).replace(",","."))
        Zrc = float(str(self.textEdit_4.toPlainText()).replace(",","."))
        Zrj = float(str(self.textEdit_5.toPlainText()).replace(",","."))
        sigmam0=float(0.5*(sigmamax+sigmamin))
        sigmaa0=float(0.5*(sigmamax-sigmamin))
        sigmaa=float(sigmaa0/sigmam0)
        x7=0
        y7=Re
        fig = plt.figure()
        ax = fig.add_subplot(1,1,1)
        ax.text(0, Re, "Re" )
        ax.text(0,Zrc, "Zrc")
        k=float(Zrj/2)
        if sigmaa > 0:
                    
            sigmam=float(Zrc/((sigmaa0/sigmam0)+((2*Zrc-Zrj)/Zrj)))
            x2=float((Zrc-Re)/(-1+((2*Zrc-Zrj)/Zrj)))
            x1=0
            y1=Zrc
            x2=float((Zrc-Re)/(-1+((2*Zrc-Zrj)/Zrj)))
            y2=float(Re-x2)
            y3=0
            x3=Re
            ax.text(k,0, "Zrj/2")
            ax.text(0,k, "Zrj/2")
            ax.text(Re, 0, "Re")
            x=[k,Re,k]
            y=[0,0,k]
            plt.scatter(x,y,color="black")
            x=[0,k,k]
            y=[k,k,0]
            plt.plot(x, y,'--', color="gray")

            if sigmam > x2: 
                sigmam=float(Re/(1+(sigmaa0/sigmam0)))


        else:
            sigmam=float(Zrc/((sigmaa0/sigmam0)+((2*Zrc-Zrj)/Zrj)))
            x2=float((Zrc-Re)/(1+((2*Zrc-Zrj)/Zrj)))
            x1=-Re
            y1=0
            y2=float(Re+x2)
            y3=Zrc
            x3=0
            x=[-k,-Re,-k]
            y=[0,0,k]
            ax.text(-k,0, "-Zrj/2")
            ax.text(0,k, "Zrj/2")
            ax.text(Re, 0, "-Re" )
            plt.scatter(x,y,color="black")
            x=[0,-k,-k]
            y=[k,k,0]
            plt.plot(x, y,'--', color="gray")
          
            if sigmam < x2:
                sigmam=float(Re/((sigmaa0/sigmam0)-1))
        
        x=[x1,x2,x3,]
        y=[y1,y2,y3]
        x4=y4=0                
        x5=sigmam
        y5=sigmaa*sigmam
        ax.text(x5,y5, "Pd")
        x3=[x2,x7]
        y3=[y2,y7]
        x2=[x4,x5]
        y2=[y4,y5]
        plt.plot(x2, y2, '--',color="gray")
        x55=str(round(x5,3))
        y55=str(round(y5,3))
        plt.plot(x3, y3,'--', color="gray")
        plt.plot(x,y,label='Obszar bezpiecznych obciążeń',color='black',linewidth=3)
        plt.xlabel('Naprężenie średnie σ [MPa]')
        plt.ylabel('Naprężenie amplitudalne σ [MPa]')
        plt.title('Wykres Haigha')
        plt.legend()
        x=[0,0,x5,0]
        y=[Re,Zrc,y5,k]
        plt.scatter(x,y, label=' \n   Pd\n\nσm(d)= '+x55+'\nσa(d)= '+y55, color="black")
        ax.legend()
        plt.gca().set_aspect('equal', adjustable='box')
        plt.show()
                
    def obliczenia2(self):
        silamax = float(str(self.textEdit_12.toPlainText()).replace(",","."))
        silamin = float(str(self.textEdit_8.toPlainText()).replace(",","."))
        wspolczynnik = float(str(self.textEdit_10.toPlainText()).replace(",","."))
        Re = float(str(self.textEdit_25.toPlainText()).replace(",","."))
        Zrc = float(str(self.textEdit_9.toPlainText()).replace(",","."))
        Zrj = float(str(self.textEdit_11.toPlainText()).replace(",","."))
        silam0=float(0.5*(silamax+silamin))
        silam0_str=str(round(silam0/1000,3))
        silaa0=float(0.5*(silamax-silamin))
        silaa0_str=str(round(silaa0/1000,3))
        sigmaa=float(silaa0/silam0)
        sigmaa_str=str(round(sigmaa,3))
        rgp=float((2*Zrc-Zrj)/Zrj)
        rgp_str=str(round(rgp,3))
        Re_str = str(round(Re,3))
        Zrc_str = str(Zrc)
        if sigmaa > 0:

            sigmamd=float(Zrc/((silaa0/silam0)+((2*Zrc-Zrj)/Zrj)))
            sigmamd_str=str(round(sigmamd,3))
            x2=float((Zrc-Re)/(-1+((2*Zrc-Zrj)/Zrj)))
            
			
            if sigmamd > x2:     
                sigmamd=float(Re/(1+(silaa0/silam0)))
                sigmamd_str=str(round(sigmamd,3))
                sigmaad=float(sigmamd*sigmaa)
                sigmaad_str=str(round(sigmaad,3))
                uzyteczna= float(sigmamd/wspolczynnik)
                uzyteczna_str=str(round(uzyteczna,3))
                A=float((silam0/uzyteczna)*1000)
                A_str=str(round(A,3))

                # Description result not avaible for demo version.
                self.textEdit_24.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.5pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:16pt;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:16pt;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:16pt;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:16pt;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:16pt;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:16pt;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:16pt;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:16pt;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:16pt;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:16pt;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:16pt;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt;\">DEMO VERSION.<br /><br /></span><span style=\" font-size:11pt;\">Install full version for description.</span></p></body></html>", None))

            else:
              sigmaad=float(sigmamd*sigmaa)
              sigmaad_str=str(round(sigmaad,3))
              uzyteczna= float(sigmamd/wspolczynnik)
              uzyteczna_str=str(round(uzyteczna,3))
              A=float((silam0/uzyteczna)*1000)
              A_str=str(round(A,3))			
              self.textEdit_24.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.5pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:16pt;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:16pt;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:16pt;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:16pt;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:16pt;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:16pt;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:16pt;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:16pt;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:16pt;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:16pt;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:16pt;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt;\">DEMO VERSION.<br /><br /></span><span style=\" font-size:11pt;\">Install full version for description.</span></p></body></html>", None))
  
        else:

            sigmamd=float(Zrc/((silaa0/silam0)+((2*Zrc-Zrj)/Zrj)))
            sigmamd_str=str(round(sigmamd,3))
            x2=float((Zrc-Re)/(1+((2*Zrc-Zrj)/Zrj)))
            if sigmamd < x2:
                sigmamd=float(Re/((silaa0/silam0)-1))
                sigmamd_str=str(round(sigmamd,3))
                sigmaad=float(sigmamd*sigmaa)
                sigmaad_str=str(round(sigmaad,3))
                uzyteczna= float(sigmamd/wspolczynnik)
                uzyteczna_str=str(round(uzyteczna,3))
                A=float((silam0/uzyteczna)*1000)
                A_str=str(round(A,3))
                self.textEdit_24.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.5pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:16pt;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:16pt;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:16pt;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:16pt;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:16pt;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:16pt;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:16pt;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:16pt;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:16pt;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:16pt;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:16pt;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt;\">DEMO VERSION.<br /><br /></span><span style=\" font-size:11pt;\">Install full version for description.</span></p></body></html>", None))
               
            else:
                sigmaad=float(sigmamd*sigmaa)
                sigmaad_str=str(round(sigmaad,3))
                uzyteczna= float(sigmamd/wspolczynnik)
                uzyteczna_str=str(round(uzyteczna,3))
                A=float((silam0/uzyteczna)*1000)
                A_str=str(round(A,3))	
                self.textEdit_24.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.5pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:16pt;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:16pt;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:16pt;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:16pt;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:16pt;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:16pt;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:16pt;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:16pt;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:16pt;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:16pt;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:16pt;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt;\">DEMO VERSION.<br /><br /></span><span style=\" font-size:11pt;\">Install full version for description.</span></p></body></html>", None))
   
        self.textEdit_7.setText(A_str)

    def wykres2(self):
        silamax = float(str(self.textEdit_12.toPlainText()).replace(",","."))
        silamin = float(str(self.textEdit_8.toPlainText()).replace(",","."))
        wspolczynnik = float(str(self.textEdit_10.toPlainText()).replace(",","."))
        Re = float(str(self.textEdit_25.toPlainText()).replace(",","."))
        Zrc = float(str(self.textEdit_9.toPlainText()).replace(",","."))
        Zrj = float(str(self.textEdit_11.toPlainText()).replace(",","."))
        silam0=float(0.5*(silamax+silamin))
        silaa0=float(0.5*(silamax-silamin))
        x7=0
        y7=Re
        fig = plt.figure()
        ax = fig.add_subplot(1,1,1)
        ax.text(0, Re, "Re" )
        ax.text(0,Zrc, "Zrc")
        k=float(Zrj/2)
        sigmaa=float(silaa0/silam0)
        sigmam=float(Zrc/((silaa0/silam0)+((2*Zrc-Zrj)/Zrj)))
        
        if sigmaa> 0:

            x1=0
            y1=Zrc
            x2=float((Zrc-Re)/(-1+((2*Zrc-Zrj)/Zrj)))
            y2=float(Re-x2)
            y3=0
            x3=Re
            ax.text(k,0, "Zrj/2")
            ax.text(0,k, "Zrj/2")
            ax.text(Re, 0, "Re")
            x=[k,Re,k]
            y=[0,0,k]
            plt.scatter(x,y,color="black")
            x=[0,k,k]
            y=[k,k,0]

            if sigmam > x2: 
                sigmam=float(Re/(1+(silaa0/silam0)))

        else:
            
            x1=-Re
            y1=0
            x2=float((Zrc-Re)/(1+((2*Zrc-Zrj)/Zrj)))
            y2=float(Re+x2)
            y3=Zrc
            x3=0
            x=[-k,-Re,-k]
            y=[0,0,k]
            ax.text(-k,0, "-Zrj/2")
            ax.text(0,k, "Zrj/2")
            ax.text(Re, 0, "-Re" )
            plt.scatter(x,y,color="black")
            x=[0,-k,-k]
            y=[k,k,0]
            if sigmam < x2:
                sigmam=float(Re/((silaa0/silam0)-1))
        plt.plot(x, y,'--', color="gray")        
        x=[x1,x2,x3,] 
        y=[y1,y2,y3]
        x4=y4=0                
        x5=sigmam
        y5=sigmaa*sigmam
        ax.text(x5,y5, "Pd")
        x3=[x2,x7]
        y3=[y2,y7]
        x2=[x4,x5]
        y2=[y4,y5]
        plt.plot(x2, y2, '--',color="gray")
        x55=str(round(x5,3))
        y55=str(round(y5,3))
        plt.plot(x3, y3,'--', color="gray")
        plt.plot(x,y,label='Obszar bezpiecznych obciążeń',color='black',linewidth=3)
        plt.xlabel('Naprężenie średnie σ [MPa]')
        plt.ylabel('Naprężenie amplitudalne σ [MPa]')
        plt.title('Wykres Haigha')
        plt.legend()
        x=[0,0,x5,0]
        y=[Re,Zrc,y5,k]
        plt.scatter(x,y, label=' \n   Pd\n\nσm(d)= '+x55+'\nσa(d)= '+y55, color="black")
        ax.legend()
        plt.gca().set_aspect('equal', adjustable='box')
        plt.show()

    def obliczenia3(self): 
        Mgm0 = float(str(self.textEdit_14.toPlainText()).replace(",","."))
        Mgm0_str=str(round(Mgm0,3))
        Mga0 = float(str(self.textEdit_27.toPlainText()).replace(",","."))
        Mga0_str=str(round(Mga0,3))
        wspolczynnik = float(str(self.textEdit_15.toPlainText()).replace(",","."))
        Wg = float(str(self.textEdit_16.toPlainText()).replace(",","."))
        Re = float(str(self.textEdit_18.toPlainText()).replace(",","."))
        Re_str=str(round(Re,3))
        Zgo = float(str(self.textEdit_17.toPlainText()).replace(",","."))
        Zgo_str = str(round(Zgo,3))
        Zgj = float(str(self.textEdit_26.toPlainText()).replace(",","."))
        sigmaa=float(Mga0/Mgm0)
        sigmaa_str=str(round(sigmaa,3))
        rgp=float((2*Zgo-Zgj)/Zgj)
        rgp_str=str(round(rgp,3))
        
        if sigmaa > 0:

            sigmamd=float(Zgo/((Mga0/Mgm0)+((2*Zgo-Zgj)/Zgj)))
            sigmamd_str=str(round(sigmamd,3))
            x2=float((Zgo-Re)/(-1+((2*Zgo-Zgj)/Zgj)))
            
            if sigmamd > x2:     
                sigmamd=float(Re/(1+(Mga0/Mgm0)))
                sigmamd_str=str(round(sigmamd,3))
                sigmaad=sigmamd*sigmaa
                sigmaad_str=str(round(sigmaad,3))
                sigmam=float(sigmamd/wspolczynnik)
                sigmam_str=str(round(sigmam,3))
                M=float(sigmam*Wg/1000000)
                M_str=str(round(M,3))
                
                # Description result not avaible for demo version.
                self.textEdit_24.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.5pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:16pt;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:16pt;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:16pt;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:16pt;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:16pt;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:16pt;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:16pt;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:16pt;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:16pt;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:16pt;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:16pt;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt;\">DEMO VERSION.<br /><br /></span><span style=\" font-size:11pt;\">Install full version for description.</span></p></body></html>", None))

            else:
                sigmam=float(sigmamd/wspolczynnik)
                sigmam_str=str(round(sigmam,3))
                sigmaad=sigmamd*sigmaa
                sigmaad_str=str(round(sigmaad,3))
                M=float(sigmam*Wg/1000000)
                M_str=str(round(M,3))
                self.textEdit_24.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.5pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:16pt;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:16pt;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:16pt;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:16pt;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:16pt;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:16pt;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:16pt;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:16pt;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:16pt;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:16pt;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:16pt;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt;\">DEMO VERSION.<br /><br /></span><span style=\" font-size:11pt;\">Install full version for description.</span></p></body></html>", None))

        else:

            sigmamd=float(Zgo/((Mga0/Mgm0)+((2*Zgo-Zgj)/Zgj)))
            sigmamd_str=str(round(sigmamd,3))
            x2=float((Zgo-Re)/(1+((2*Zgo-Zgj)/Zgj)))
            if sigmamd < x2:
                sigmamd=float(Re/(-1+(Mga0/Mgm0)))
                sigmamd_str=str(round(sigmamd,3))
                sigmaad=sigmamd*sigmaa
                sigmaad_str=str(round(sigmaad,3))
                sigmam=float(sigmamd/wspolczynnik)
                sigmam_str=str(round(sigmam,3))
                M=float(sigmam*Wg/1000000)
                M_str=str(round(M,3))
                self.textEdit_24.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.5pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:16pt;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:16pt;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:16pt;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:16pt;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:16pt;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:16pt;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:16pt;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:16pt;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:16pt;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:16pt;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:16pt;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt;\">DEMO VERSION.<br /><br /></span><span style=\" font-size:11pt;\">Install full version for description.</span></p></body></html>", None))

                
            else:
                sigmam=float(sigmamd/wspolczynnik)
                sigmam_str=str(round(sigmam,3))
                sigmaad=sigmamd*sigmaa
                sigmaad_str=str(round(sigmaad,3))
                M=float(sigmam*Wg/1000000)
                M_str=str(round(M,3))
                self.textEdit_24.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.5pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:16pt;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:16pt;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:16pt;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:16pt;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:16pt;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:16pt;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:16pt;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:16pt;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:16pt;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:16pt;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:16pt;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt;\">DEMO VERSION.<br /><br /></span><span style=\" font-size:11pt;\">Install full version for description.</span></p></body></html>", None))

        self.textEdit_13.setText(M_str)
                
    def wykres3(self):
        Mgm0 = float(str(self.textEdit_14.toPlainText()).replace(",","."))
        Mga0 = float(str(self.textEdit_27.toPlainText()).replace(",","."))
        wspolczynnik = float(str(self.textEdit_15.toPlainText()).replace(",","."))
        Wg = float(str(self.textEdit_16.toPlainText()).replace(",","."))
        Re = float(str(self.textEdit_18.toPlainText()).replace(",","."))
        Zgo = float(str(self.textEdit_17.toPlainText()).replace(",","."))
        Zgj = float(str(self.textEdit_26.toPlainText()).replace(",","."))
        sigmaa=float(Mga0/Mgm0)
        sigmam=float(Zgo/((Mga0/Mgm0)+((2*Zgo-Zgj)/Zgj)))
        x7=0
        y7=Re
        fig = plt.figure()
        ax = fig.add_subplot(1,1,1)
        ax.text(0, Re, "Re" )
        ax.text(0,Zgo, "Zgo")
        k=float(Zgj/2)
        
        if sigmaa > 0:

            x1=0
            y1=Zgo
            x2=float((Zgo-Re)/(-1+((2*Zgo-Zgj)/Zgj)))
            y2=float(Re-x2)
            y3=0
            x3=Re
            ax.text(k,0, "Zgj/2")
            ax.text(0,k, "Zgj/2")
            ax.text(Re, 0, "Re")
            x=[k,Re,k]
            y=[0,0,k]
            plt.scatter(x,y,color="black")
            x=[0,k,k]
            y=[k,k,0]

            if sigmam > x2: 
                sigmam=float(Re/(1+(Mga0/Mgm0)))

        else:
            
            x1=-Re
            y1=0
            x2=float((Zgo-Re)/(1+((2*Zgo-Zgj)/Zgj)))
            y2=float(Re+x2)
            y3=Zgo
            x3=0
            x=[-k,-Re,-k]
            y=[0,0,k]
            ax.text(-k,0, "-Zgj/2")
            ax.text(0,k, "Zgj/2")
            ax.text(Re, 0, "-Re" )
            plt.scatter(x,y,color="black")
            x=[0,-k,-k]
            y=[k,k,0]
            if sigmam < x2:
                sigmam=float(Re/((Mga0/Mgm0)-1))
                
        plt.plot(x, y,'--', color="gray")
        x=[x1,x2,x3,] 
        y=[y1,y2,y3]
        x4=y4=0                
        x5=sigmam
        y5=sigmaa*sigmam
        ax.text(x5,y5, "Pd")
        x3=[x2,x7]
        y3=[y2,y7]
        x2=[x4,x5]
        y2=[y4,y5]
        plt.plot(x2, y2, '--',color="gray")
        x55=str(round(x5,3))
        y55=str(round(y5,3))
        plt.plot(x3, y3,'--', color="gray")
        plt.plot(x,y,label='Obszar bezpiecznych obciążeń',color='black',linewidth=3)
        plt.xlabel('Naprężenie średnie σ [MPa]')
        plt.ylabel('Naprężenie amplitudalne σ [MPa]')
        plt.title('Wykres Haigha')
        plt.legend()
        x=[0,0,x5,0]
        y=[Re,Zgo,y5,k]
        plt.scatter(x,y, label=' \n   Pd\n\nσm(d)= '+x55+'\nσa(d)= '+y55, color="black")
        ax.legend()
        plt.gca().set_aspect('equal', adjustable='box')
        plt.show()
        
    def obliczenia4(self):
        
        mnoznik = float(str(self.textEdit_31.toPlainText()).replace(",","."))
        momentm = float(str(self.textEdit_28.toPlainText()).replace(",","."))
        momenta = float(str(self.textEdit_29.toPlainText()).replace(",","."))
        wspolczynnik = float(str(self.textEdit_23.toPlainText()).replace(",","."))
        Re = float(str(self.textEdit_19.toPlainText()).replace(",","."))
        Re_str = str(round(Re,3))
        Zgo = float(str(self.textEdit_30.toPlainText()).replace(",","."))
        Zgo_str=str(round(Zgo,3))
        Zgj = float(str(self.textEdit_20.toPlainText()).replace(",","."))
        Mgm0=mnoznik*momentm
        Mga0=mnoznik*momenta
        Mga0_str=str(Mga0)
        Mgm0_str=str(Mgm0)
        sigmamd=float(Zgo/((Mga0/Mgm0)+((2*Zgo-Zgj)/Zgj)))
        sigmamd_str=str(round(sigmamd,3))
        rgp=float((2*Zgo-Zgj)/Zgj)
        rgp_str=str(round(rgp,3))            
        sigmaa=float(Mga0/Mgm0)
        sigmaa_str=str(round(sigmaa,3))
        if sigmaa>0:    
            x2=float((Zgo-Re)/(-1+((2*Zgo-Zgj)/Zgj))) 
            if sigmamd > x2:     
                sigmamd=float(Re/(1+(Mga0/Mgm0)))
                sigmamd_str=str(round(sigmamd,3))
                sigmaad=float(sigmamd*sigmaa)
                sigmaad_str=str(round(sigmaad,3))
                uzyteczna=float(sigmamd/wspolczynnik)
                uzyteczna_str=str(round(uzyteczna,3))
                W=float((Mgm0/uzyteczna)*1000)
                W_str=str(round(W,3))
                Wwstep=float(W*1000000)
                Wwstep_str=str(round(Wwstep,3))
                                    
                self.textEdit_24.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.5pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\">1)</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\">Wyznaczamy wartości amplitudalną i średnią obciążenia mnożąc odpowiednie czyniki funkcji. Zamieniamy jednostki, które ułatwią przeliczenia wskaźnika w dalszej części:</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Calibri,sans-serif\'; font-size:11pt;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\"><br />M</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt; vertical-align:sub;\">a(0)</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\">= "+Mga0_str+" *10</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt; vertical-align:super;\">6</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\"> Nmm</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\"><br />M</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt; vertical-align:sub;\">m(0)</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\">= "+Mgm0_str+" *10</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt; vertical-align:super;\">6</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\"> Nmm</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\"><br /></span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\">2) </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\">Wyznaczamy równanie prostej obciążeniowej :<br /></span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\">σ</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt; vertical-align:sub;\">a</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\">=(M</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt; vertical-align:sub;\">a(0) </span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\">/ M</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt; vertical-align:sub;\">m(0) </span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\">)*σ</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt; vertical-align:sub;\">m </span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\">= "+sigmaa_str+" σ</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt; vertical-align:sub;\">m</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Calibri,sans-serif\'; font-size:11pt; vertical-align:sub;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Calibri,sans-serif\'; font-size:11pt; vertical-align:sub;\"><br /></p>\n"

"<p align=\"right\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Calibri,sans-serif\'; font-size:9pt;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Calibri,sans-serif\'; font-size:11pt;\"><br /></p>\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri,sans-serif\'; font-size:9pt;\">(Prosta ta posiada wartość dodatnią dlatego cały wkyres będzie rysowany po dodatniej stronie wartości na osi &quot;X&quot;.)</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\">3)</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\"> Równanie górnej prostej ograniczającej obliczamy ze wzoru:<br /></span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\">σ</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt; vertical-align:sub;\">a</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\">=Z</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt; vertical-align:sub;\">go </span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\"> -σ</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt; vertical-align:sub;\">m</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\">* (2Z</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt; vertical-align:sub;\">go </span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\">- Z</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt; vertical-align:sub;\">gj</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\">)/Z</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt; vertical-align:sub;\">gj </span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\">= "+Zgo_str+" - "+rgp_str+" σ</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt; vertical-align:sub;\">m</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Calibri,sans-serif\'; font-size:11pt; vertical-align:sub;\"><br /></p>\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri,sans-serif\'; font-size:9pt;\">(W przypadku skręcania podstawiamy  oznaczenia własności materiału dla skręcania: Z</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:9pt; vertical-align:sub;\">so</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:9pt;\">, Z</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:9pt; vertical-align:sub;\">sj</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:9pt;\">.)</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Calibri,sans-serif\'; font-size:11pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\"><br />(W przypadku innych obciążeń, podstawiamy odpowiednie zmienne materiałowe </span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:10pt;\">Z</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:10pt; vertical-align:sub;\">so</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:10pt;\">, Z</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:10pt; vertical-align:sub;\">sj</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:10pt;\">, Z</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:10pt; vertical-align:sub;\">rc</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:10pt;\">, Z</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:10pt; vertical-align:sub;\">rj</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:9pt; vertical-align:sub;\">  </span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:9pt;\">. </span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:10pt;\">To samo dotyczy wykresu.</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:9pt;\">)<br /><br /></span></p></body></html>"

"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\">4)</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\"> Rysujemy proste przerywane na wykresie (X - σ</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt; vertical-align:sub;\">m</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\">; Y - σ</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt; vertical-align:sub;\">a</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\">):<br />    a) prostej obciążeniowej z pkt.2</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\">    b)prostej ograniczającej z pkt.3</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\">    c)prostej od punktu wartości Re na osi X do punktu o wartości Re na osi Y</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Calibri,sans-serif\'; font-size:11pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\">5)</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\"> Prosta obciążeniowa w tym przypadku przecina się z prostą ograniczającą wartościami granicy plastyczności Re, zatem przyrównujemy obie proste w celu uzyskania punktu P</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt; vertical-align:sub;\">d</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\">:</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\"><br /><br /> "+sigmaa_str+" σ</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt; vertical-align:sub;\">m</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\"> = " +Re_str+ " - σ</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt; vertical-align:sub;\">m</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Calibri,sans-serif\'; font-size:11pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\">6)</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\"> Wyliczamy współrzędne punktu P</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt; vertical-align:sub;\">d</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\">:</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Calibri,sans-serif\'; font-size:11pt;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\">σ</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt; vertical-align:sub;\">m(d)</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\">= "+sigmamd_str+" MPa , σ</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt; vertical-align:sub;\">a(d)</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\"> = "+sigmaad_str+" MPa</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Calibri,sans-serif\'; font-size:11pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\">7)</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\">Użyteczna wartość naprężeń wynosi:<br /></span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\"><br />σ</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt; vertical-align:sub;\">m(0)</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\">= σ</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt; vertical-align:sub;\">m(d) </span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\">/ </span><span style=\" font-size:10pt;\">δ</span><span style=\" font-size:9pt;\"> = "+uzyteczna_str+" MPa</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:9pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\">8)</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt; font-weight:600;\">Wartośc wskaźnika</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\">:</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Calibri,sans-serif\'; font-size:11pt;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\">W = M</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt; vertical-align:sub;\">m(0)</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\"> / σ</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt; vertical-align:sub;\">m(0) </span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\">= "+Wwstep_str+" mm</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt; vertical-align:super;\">3</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\"> = "+W_str+" cm</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt; vertical-align:super;\">3</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Calibri,sans-serif\'; font-size:11pt; vertical-align:super;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Calibri,sans-serif\'; font-size:11pt; vertical-align:super;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Calibri,sans-serif\'; font-size:11pt; vertical-align:super;\"><br /></p></body></html>", None))

            else:
                sigmaad=float(sigmamd*sigmaa)
                sigmaad_str=str(round(sigmaad,3))
                uzyteczna=float(sigmamd/wspolczynnik)
                uzyteczna_str=str(round(uzyteczna,3))
                W=float((Mgm0/uzyteczna)*1000)
                W_str=str(round(W,3))
                Wwstep=float(W*1000000)
                Wwstep_str=str(round(Wwstep,3))
                self.textEdit_24.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.5pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\">1)</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\">Wyznaczamy wartości amplitudalną i średnią obciążenia mnożąc odpowiednie czyniki funkcji. Zamieniamy jednostki, które ułatwią przeliczenia wskaźnika w dalszej części:</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Calibri,sans-serif\'; font-size:11pt;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\"><br />M</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt; vertical-align:sub;\">a(0)</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\">= "+Mga0_str+" *10</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt; vertical-align:super;\">6</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\"> Nmm</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\"><br />M</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt; vertical-align:sub;\">m(0)</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\">= "+Mgm0_str+" *10</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt; vertical-align:super;\">6</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\"> Nmm</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\"><br /></span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\">2) </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\">Wyznaczamy równanie prostej obciążeniowej :<br /></span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\">σ</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt; vertical-align:sub;\">a</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\">=(M</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt; vertical-align:sub;\">a(0) </span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\">/ M</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt; vertical-align:sub;\">m(0) </span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\">)*σ</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt; vertical-align:sub;\">m </span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\">= "+sigmaa_str+" σ</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt; vertical-align:sub;\">m</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Calibri,sans-serif\'; font-size:11pt; vertical-align:sub;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Calibri,sans-serif\'; font-size:11pt; vertical-align:sub;\"><br /></p>\n"

"<p align=\"right\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Calibri,sans-serif\'; font-size:9pt;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Calibri,sans-serif\'; font-size:11pt;\"><br /></p>\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri,sans-serif\'; font-size:9pt;\">(Prosta ta posiada wartość dodatnią dlatego cały wkyres będzie rysowany po dodatniej stronie wartości na osi &quot;X&quot;.)</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\">3)</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\"> Równanie górnej prostej ograniczającej obliczamy ze wzoru:<br /></span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\">σ</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt; vertical-align:sub;\">a</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\">=Z</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt; vertical-align:sub;\">go </span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\"> -σ</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt; vertical-align:sub;\">m</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\">* (2Z</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt; vertical-align:sub;\">go </span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\">- Z</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt; vertical-align:sub;\">gj</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\">)/Z</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt; vertical-align:sub;\">gj </span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\">= "+Zgo_str+" - "+rgp_str+" σ</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt; vertical-align:sub;\">m</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Calibri,sans-serif\'; font-size:11pt; vertical-align:sub;\"><br /></p>\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri,sans-serif\'; font-size:9pt;\">(W przypadku skręcania podstawiamy  oznaczenia własności materiału dla skręcania: Z</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:9pt; vertical-align:sub;\">so</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:9pt;\">, Z</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:9pt; vertical-align:sub;\">sj</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:9pt;\">.)</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Calibri,sans-serif\'; font-size:11pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\"><br />(W przypadku innych obciążeń, podstawiamy odpowiednie zmienne materiałowe </span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:10pt;\">Z</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:10pt; vertical-align:sub;\">so</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:10pt;\">, Z</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:10pt; vertical-align:sub;\">sj</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:10pt;\">, Z</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:10pt; vertical-align:sub;\">rc</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:10pt;\">, Z</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:10pt; vertical-align:sub;\">rj</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:9pt; vertical-align:sub;\">  </span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:9pt;\">. </span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:10pt;\">To samo dotyczy wykresu.</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:9pt;\">)<br /><br /></span></p></body></html>"

"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\">4)</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\"> Rysujemy proste przerywane na wykresie (X - σ</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt; vertical-align:sub;\">m</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\">; Y - σ</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt; vertical-align:sub;\">a</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\">):<br />    a) prostej obciążeniowej z pkt.2</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\">    b)prostej ograniczającej z pkt.3</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\">    c)prostej od punktu wartości Re na osi X do punktu o wartości Re na osi Y</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Calibri,sans-serif\'; font-size:11pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\">5)</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\"> Prosta obciążeniowa w tym przypadku przecina się z górną prostą ograniczającą, zatem przyrównujemy obie proste w celu uzyskania punktu P</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt; vertical-align:sub;\">d</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\">:</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\"><br /><br />"+sigmaa_str+" σ</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt; vertical-align:sub;\">m</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\"> = "+Zgo_str+" - "+rgp_str+" σ</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt; vertical-align:sub;\">m</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Calibri,sans-serif\'; font-size:11pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\">6)</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\"> Wyliczamy współrzędne punktu P</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt; vertical-align:sub;\">d</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\">:</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Calibri,sans-serif\'; font-size:11pt;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\">σ</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt; vertical-align:sub;\">m(d)</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\">= "+sigmamd_str+" MPa , σ</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt; vertical-align:sub;\">a(d)</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\"> = "+sigmaad_str+" MPa</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Calibri,sans-serif\'; font-size:11pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\">7)</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\">Użyteczna wartość naprężeń wynosi:<br /></span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\"><br />σ</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt; vertical-align:sub;\">m(0)</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\">= σ</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt; vertical-align:sub;\">m(d) </span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\">/ </span><span style=\" font-size:10pt;\">δ</span><span style=\" font-size:9pt;\"> = "+uzyteczna_str+" MPa</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:9pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\">8)</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt; font-weight:600;\">Wartośc wskaźnika</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\">:</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Calibri,sans-serif\'; font-size:11pt;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\">W = M</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt; vertical-align:sub;\">m(0)</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\"> / σ</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt; vertical-align:sub;\">m(0) </span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\">= "+Wwstep_str+" mm</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt; vertical-align:super;\">3</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\"> = "+W_str+" cm</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt; vertical-align:super;\">3</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Calibri,sans-serif\'; font-size:11pt; vertical-align:super;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Calibri,sans-serif\'; font-size:11pt; vertical-align:super;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Calibri,sans-serif\'; font-size:11pt; vertical-align:super;\"><br /></p></body></html>", None))

        else:
            x2=float((Zgo-Re)/(1+((2*Zgo-Zgj)/Zgj)))
            if sigmamd < x2:
                sigmamd=float(Re/(-1+(Mga0/Mgm0)))
                sigmamd_str=str(round(sigmamd,3))
                sigmaad=float(sigmamd*sigmaa)
                sigmaad_str=str(round(sigmaad,3))
                uzyteczna=float(sigmamd/wspolczynnik)
                uzyteczna_str=str(round(uzyteczna,3))
                W=float((Mgm0/uzyteczna)*1000)
                W_str=str(round(W,3))
                Wwstep=float(W*1000000)
                Wwstep_str=str(round(Wwstep,3))                                    
                self.textEdit_24.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.5pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\">1)</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\">Wyznaczamy wartości amplitudalną i średnią obciążenia mnożąc odpowiednie czyniki funkcji. Zamieniamy jednostki, które ułatwią przeliczenia wskaźnika w dalszej części:</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Calibri,sans-serif\'; font-size:11pt;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\"><br />M</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt; vertical-align:sub;\">a(0)</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\">= "+Mga0_str+" *10</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt; vertical-align:super;\">6</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\"> Nmm</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\"><br />M</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt; vertical-align:sub;\">m(0)</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\">= "+Mgm0_str+" *10</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt; vertical-align:super;\">6</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\"> Nmm</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\"><br /></span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\">2) </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\">Wyznaczamy równanie prostej obciążeniowej :<br /></span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\">σ</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt; vertical-align:sub;\">a</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\">=(M</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt; vertical-align:sub;\">a(0) </span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\">/ M</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt; vertical-align:sub;\">m(0) </span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\">)*σ</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt; vertical-align:sub;\">m </span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\">= "+sigmaa_str+" σ</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt; vertical-align:sub;\">m</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Calibri,sans-serif\'; font-size:11pt; vertical-align:sub;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Calibri,sans-serif\'; font-size:11pt; vertical-align:sub;\"><br /></p>\n"

"<p align=\"right\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Calibri,sans-serif\'; font-size:9pt;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Calibri,sans-serif\'; font-size:11pt;\"><br /></p>\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri,sans-serif\'; font-size:9pt;\">(Prosta ta posiada wartość ujemną dlatego cały wykres będzie rysowany po ujemnej stronie wartości na osi &quot;X&quot;.)</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\">3)</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\"> Równanie górnej prostej ograniczającej obliczamy ze wzoru:<br /></span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\">σ</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt; vertical-align:sub;\">a</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\">=Z</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt; vertical-align:sub;\">go </span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\"> -σ</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt; vertical-align:sub;\">m</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\">* (2Z</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt; vertical-align:sub;\">go </span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\">- Z</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt; vertical-align:sub;\">gj</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\">)/Z</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt; vertical-align:sub;\">gj </span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\">= "+Zgo_str+" - "+rgp_str+" σ</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt; vertical-align:sub;\">m</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Calibri,sans-serif\'; font-size:11pt; vertical-align:sub;\"><br /></p>\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri,sans-serif\'; font-size:9pt;\">(W przypadku skręcania podstawiamy  oznaczenia własności materiału dla skręcania: Z</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:9pt; vertical-align:sub;\">so</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:9pt;\">, Z</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:9pt; vertical-align:sub;\">sj</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:9pt;\">.)</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Calibri,sans-serif\'; font-size:11pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\"><br />(W przypadku innych obciążeń, podstawiamy odpowiednie zmienne materiałowe </span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:10pt;\">Z</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:10pt; vertical-align:sub;\">so</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:10pt;\">, Z</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:10pt; vertical-align:sub;\">sj</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:10pt;\">, Z</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:10pt; vertical-align:sub;\">rc</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:10pt;\">, Z</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:10pt; vertical-align:sub;\">rj</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:9pt; vertical-align:sub;\">  </span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:9pt;\">. </span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:10pt;\">To samo dotyczy wykresu.</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:9pt;\">)<br /><br /></span></p></body></html>"

"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\">4)</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\"> Rysujemy proste przerywane na wykresie (X - σ</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt; vertical-align:sub;\">m</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\">; Y - σ</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt; vertical-align:sub;\">a</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\">):<br />    a) prostej obciążeniowej z pkt.2</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\">    b)prostej ograniczającej z pkt.3</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\">    c)prostej od punktu wartości -Re na osi X do punktu o wartości Re na osi Y</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Calibri,sans-serif\'; font-size:11pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\">5)</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\"> Prosta obciążeniowa w tym przypadku przecina się z prostą ograniczającą wartościami granicy plastyczności Re, zatem przyrównujemy obie proste w celu uzyskania punktu P</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt; vertical-align:sub;\">d</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\">:</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\"><br /><br /> "+sigmaa_str+" σ</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt; vertical-align:sub;\">m</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\"> = " +Re_str+ " - σ</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt; vertical-align:sub;\">m</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Calibri,sans-serif\'; font-size:11pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\">6)</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\"> Wyliczamy współrzędne punktu P</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt; vertical-align:sub;\">d</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\">:</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Calibri,sans-serif\'; font-size:11pt;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\">σ</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt; vertical-align:sub;\">m(d)</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\">= "+sigmamd_str+" MPa , σ</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt; vertical-align:sub;\">a(d)</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\"> = "+sigmaad_str+" MPa</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Calibri,sans-serif\'; font-size:11pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\">7)</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\">Użyteczna wartość naprężeń wynosi:<br /></span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\"><br />σ</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt; vertical-align:sub;\">m(0)</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\">= σ</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt; vertical-align:sub;\">m(d) </span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\">/ </span><span style=\" font-size:10pt;\">δ</span><span style=\" font-size:9pt;\"> = "+uzyteczna_str+" MPa</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:9pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\">8)</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt; font-weight:600;\">Wartośc wskaźnika</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\">:</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Calibri,sans-serif\'; font-size:11pt;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\">W = M</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt; vertical-align:sub;\">m(0)</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\"> / σ</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt; vertical-align:sub;\">m(0) </span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\">= "+Wwstep_str+" mm</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt; vertical-align:super;\">3</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\"> = "+W_str+" cm</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt; vertical-align:super;\">3</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Calibri,sans-serif\'; font-size:11pt; vertical-align:super;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Calibri,sans-serif\'; font-size:11pt; vertical-align:super;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Calibri,sans-serif\'; font-size:11pt; vertical-align:super;\"><br /></p></body></html>", None))
            else:
                sigmaad=float(sigmamd*sigmaa)
                sigmaad_str=str(round(sigmaad,3))
                uzyteczna=float(sigmamd/wspolczynnik)
                uzyteczna_str=str(round(uzyteczna,3))
                W=float((Mgm0/uzyteczna)*1000)
                W_str=str(round(W,3))
                Wwstep=float(W*1000000)
                Wwstep_str=str(round(Wwstep,3))
                self.textEdit_24.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.5pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\">1)</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\">Wyznaczamy wartości amplitudalną i średnią obciążenia mnożąc odpowiednie czyniki funkcji. Zamieniamy jednostki, które ułatwią przeliczenia wskaźnika w dalszej części:</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Calibri,sans-serif\'; font-size:11pt;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\"><br />M</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt; vertical-align:sub;\">a(0)</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\">= "+Mga0_str+" *10</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt; vertical-align:super;\">6</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\"> Nmm</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\"><br />M</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt; vertical-align:sub;\">m(0)</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\">= "+Mgm0_str+" *10</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt; vertical-align:super;\">6</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\"> Nmm</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\"><br /></span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\">2) </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\">Wyznaczamy równanie prostej obciążeniowej :<br /></span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\">σ</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt; vertical-align:sub;\">a</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\">=(M</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt; vertical-align:sub;\">a(0) </span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\">/ M</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt; vertical-align:sub;\">m(0) </span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\">)*σ</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt; vertical-align:sub;\">m </span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\">= "+sigmaa_str+" σ</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt; vertical-align:sub;\">m</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Calibri,sans-serif\'; font-size:11pt; vertical-align:sub;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Calibri,sans-serif\'; font-size:11pt; vertical-align:sub;\"><br /></p>\n"
"<p align=\"right\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Calibri,sans-serif\'; font-size:9pt;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Calibri,sans-serif\'; font-size:11pt;\"><br /></p>\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri,sans-serif\'; font-size:9pt;\">(Prosta ta posiada wartość ujemną dlatego cały wkyres będzie rysowany po ujemnej stronie wartości na osi &quot;X&quot;.)</span></p>\n"

"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\">3)</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\"> Równanie górnej prostej ograniczającej obliczamy ze wzoru:<br /></span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\">σ</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt; vertical-align:sub;\">a</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\">=Z</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt; vertical-align:sub;\">go </span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\"> -σ</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt; vertical-align:sub;\">m</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\">* (2Z</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt; vertical-align:sub;\">go </span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\">- Z</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt; vertical-align:sub;\">gj</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\">)/Z</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt; vertical-align:sub;\">gj </span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\">= "+Zgo_str+" - "+rgp_str+" σ</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt; vertical-align:sub;\">m</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Calibri,sans-serif\'; font-size:11pt; vertical-align:sub;\"><br /></p>\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri,sans-serif\'; font-size:9pt;\">(W przypadku skręcania podstawiamy  oznaczenia własności materiału dla skręcania: Z</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:9pt; vertical-align:sub;\">so</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:9pt;\">, Z</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:9pt; vertical-align:sub;\">sj</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:9pt;\">.)</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Calibri,sans-serif\'; font-size:11pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\"><br />(W przypadku innych obciążeń, podstawiamy odpowiednie zmienne materiałowe </span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:10pt;\">Z</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:10pt; vertical-align:sub;\">so</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:10pt;\">, Z</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:10pt; vertical-align:sub;\">sj</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:10pt;\">, Z</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:10pt; vertical-align:sub;\">rc</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:10pt;\">, Z</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:10pt; vertical-align:sub;\">rj</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:9pt; vertical-align:sub;\">  </span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:9pt;\">. </span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:10pt;\">To samo dotyczy wykresu.</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:9pt;\">)<br /><br /></span></p></body></html>"

"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\">4)</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\"> Rysujemy proste przerywane na wykresie (X - σ</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt; vertical-align:sub;\">m</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\">; Y - σ</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt; vertical-align:sub;\">a</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\">):<br />    a) prostej obciążeniowej z pkt.2</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\">    b)prostej ograniczającej z pkt.3</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\">    c)prostej od punktu wartości -Re na osi X do punktu o wartości Re na osi Y</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Calibri,sans-serif\'; font-size:11pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\">5)</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\"> Prosta obciążeniowa w tym przypadku przecina się z górną prostą ograniczającą, zatem przyrównujemy obie proste w celu uzyskania punktu P</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt; vertical-align:sub;\">d</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\">:</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\"><br /><br />"+sigmaa_str+" σ</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt; vertical-align:sub;\">m</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\"> = "+Zgo_str+" - "+rgp_str+" σ</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt; vertical-align:sub;\">m</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Calibri,sans-serif\'; font-size:11pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\">6)</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\"> Wyliczamy współrzędne punktu P</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt; vertical-align:sub;\">d</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\">:</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Calibri,sans-serif\'; font-size:11pt;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\">σ</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt; vertical-align:sub;\">m(d)</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\">= "+sigmamd_str+" MPa , σ</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt; vertical-align:sub;\">a(d)</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\"> = "+sigmaad_str+" MPa</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Calibri,sans-serif\'; font-size:11pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\">7)</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\">Użyteczna wartość naprężeń wynosi:<br /></span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\"><br />σ</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt; vertical-align:sub;\">m(0)</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\">= σ</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt; vertical-align:sub;\">m(d) </span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\">/ </span><span style=\" font-size:10pt;\">δ</span><span style=\" font-size:9pt;\"> = "+uzyteczna_str+" MPa</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:9pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\">8)</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt; font-weight:600;\">Wartośc wskaźnika</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\">:</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Calibri,sans-serif\'; font-size:11pt;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\">W = M</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt; vertical-align:sub;\">m(0)</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\"> / σ</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt; vertical-align:sub;\">m(0) </span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\">= "+Wwstep_str+" mm</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt; vertical-align:super;\">3</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt;\"> = "+W_str+" cm</span><span style=\" font-family:\'Calibri,sans-serif\'; font-size:11pt; vertical-align:super;\">3</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Calibri,sans-serif\'; font-size:11pt; vertical-align:super;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Calibri,sans-serif\'; font-size:11pt; vertical-align:super;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Calibri,sans-serif\'; font-size:11pt; vertical-align:super;\"><br /></p></body></html>", None))

        self.textEdit_21.setText(W_str)
                
    def wykres4(self):
        mnoznik = float(str(self.textEdit_31.toPlainText()).replace(",","."))
        momentm = float(str(self.textEdit_28.toPlainText()).replace(",","."))
        momenta = float(str(self.textEdit_29.toPlainText()).replace(",","."))
        wspolczynnik = float(str(self.textEdit_23.toPlainText()).replace(",","."))
        Re = float(str(self.textEdit_19.toPlainText()).replace(",","."))
        Zgo = float(str(self.textEdit_30.toPlainText()).replace(",","."))
        Zgj = float(str(self.textEdit_20.toPlainText()).replace(",","."))
        Mgm0=mnoznik*momentm
        Mga0=mnoznik*momenta
        sigmaa=float(Mga0/Mgm0)
        sigmam=float(Zgo/((Mga0/Mgm0)+((2*Zgo-Zgj)/Zgj))) 
        x7=0
        y7=Re
        fig = plt.figure()
        ax = fig.add_subplot(1,1,1)
        ax.text(0, Re, "Re" )
        ax.text(0,Zgo, "Zso")
        k=float(Zgj/2)
        
        if sigmaa > 0:

            x1=0
            y1=Zgo
            x2=float((Zgo-Re)/(-1+((2*Zgo-Zgj)/Zgj)))
            y2=float(Re-x2)
            y3=0
            x3=Re
            ax.text(k,0, "Zsj/2")
            ax.text(0,k, "Zsj/2")
            ax.text(Re, 0, "Re")
            x=[k,Re,k]
            y=[0,0,k]
            plt.scatter(x,y,color="black")
            x=[0,k,k]
            y=[k,k,0]

            if sigmam > x2: 
                sigmam=float(Re/(1+(Mga0/Mgm0)))

        else:
            
            x1=-Re
            y1=0
            x2=float((Zgo-Re)/(1+((2*Zgo-Zgj)/Zgj)))
            y2=float(Re+x2)
            y3=Zgo
            x3=0
            x=[-k,-Re,-k]
            y=[0,0,k]
            ax.text(-k,0, "-Zsj/2")
            ax.text(0,k, "Zsj/2")
            ax.text(Re, 0, "-Re" )
            plt.scatter(x,y,color="black")
            x=[0,-k,-k]
            y=[k,k,0]
            if sigmam < x2:
                sigmam=float(Re/((Mga0/Mgm0)-1))
                
        plt.plot(x, y,'--', color="gray")
        x=[x1,x2,x3,] 
        y=[y1,y2,y3]
        x4=y4=0                
        x5=sigmam
        y5=sigmaa*sigmam
        ax.text(x5,y5, "Pd")
        x3=[x2,x7]
        y3=[y2,y7]
        x2=[x4,x5]
        y2=[y4,y5]
        plt.plot(x2, y2, '--',color="gray")
        x55=str(round(x5,3))
        y55=str(round(y5,3))
        plt.plot(x3, y3,'--', color="gray")
        plt.plot(x,y,label='Obszar bezpiecznych obciążeń',color='black',linewidth=3)
        plt.xlabel('Naprężenie średnie σ [MPa]')
        plt.ylabel('Naprężenie amplitudalne σ [MPa]')
        plt.title('Wykres Haigha')
        plt.legend()
        x=[0,0,x5,0]
        y=[Re,Zgo,y5,k]
        plt.scatter(x,y, label=' \n   Pd\n\nσm(d)= '+x55+'\nσa(d)= '+y55, color="black")
        ax.legend()
        plt.gca().set_aspect('equal', adjustable='box')
        plt.show()
        
if __name__ == "__main__":

    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())



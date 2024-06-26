# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\UI\KnowledgeEditor.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_KnowledgeEditor(object):
    def setupUi(self, KnowledgeEditor):
        KnowledgeEditor.setObjectName("KnowledgeEditor")
        KnowledgeEditor.resize(1142, 837)
        KnowledgeEditor.setMinimumSize(QtCore.QSize(1142, 0))
        KnowledgeEditor.setMaximumSize(QtCore.QSize(1142, 837))
        KnowledgeEditor.setBaseSize(QtCore.QSize(1142, 837))
        self.centralwidget = QtWidgets.QWidget(KnowledgeEditor)
        self.centralwidget.setObjectName("centralwidget")
        self.printAlloysBtn = QtWidgets.QPushButton(self.centralwidget)
        self.printAlloysBtn.setGeometry(QtCore.QRect(10, 90, 281, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.printAlloysBtn.setFont(font)
        self.printAlloysBtn.setObjectName("printAlloysBtn")
        self.resultList = QtWidgets.QListWidget(self.centralwidget)
        self.resultList.setEnabled(True)
        self.resultList.setGeometry(QtCore.QRect(330, 90, 781, 501))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.resultList.setFont(font)
        self.resultList.setObjectName("resultList")
        self.printPropertiesBtn = QtWidgets.QPushButton(self.centralwidget)
        self.printPropertiesBtn.setGeometry(QtCore.QRect(10, 160, 281, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.printPropertiesBtn.setFont(font)
        self.printPropertiesBtn.setObjectName("printPropertiesBtn")
        self.printPossibleValuesBtn = QtWidgets.QPushButton(self.centralwidget)
        self.printPossibleValuesBtn.setGeometry(QtCore.QRect(10, 230, 281, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.printPossibleValuesBtn.setFont(font)
        self.printPossibleValuesBtn.setObjectName("printPossibleValuesBtn")
        self.printDescriptionPropertiesBtn = QtWidgets.QPushButton(
            self.centralwidget
        )
        self.printDescriptionPropertiesBtn.setGeometry(
            QtCore.QRect(10, 300, 281, 61)
        )
        font = QtGui.QFont()
        font.setPointSize(14)
        self.printDescriptionPropertiesBtn.setFont(font)
        self.printDescriptionPropertiesBtn.setObjectName(
            "printDescriptionPropertiesBtn"
        )
        self.printValuesAlloyBtn = QtWidgets.QPushButton(self.centralwidget)
        self.printValuesAlloyBtn.setGeometry(QtCore.QRect(10, 380, 281, 71))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.printValuesAlloyBtn.setFont(font)
        self.printValuesAlloyBtn.setObjectName("printValuesAlloyBtn")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(340, 10, 501, 61))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(340, 680, 571, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(340, 630, 571, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.addButton = QtWidgets.QPushButton(self.centralwidget)
        self.addButton.setGeometry(QtCore.QRect(940, 660, 161, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.addButton.setFont(font)
        self.addButton.setObjectName("addButton")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(440, 750, 501, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(255, 0, 0);")
        self.label_3.setObjectName("label_3")
        self.CheckFullKnowledge = QtWidgets.QPushButton(self.centralwidget)
        self.CheckFullKnowledge.setGeometry(QtCore.QRect(20, 730, 251, 51))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.CheckFullKnowledge.setFont(font)
        self.CheckFullKnowledge.setObjectName("CheckFullKnowledge")
        KnowledgeEditor.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(KnowledgeEditor)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1142, 26))
        self.menubar.setObjectName("menubar")
        KnowledgeEditor.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(KnowledgeEditor)
        self.statusbar.setObjectName("statusbar")
        KnowledgeEditor.setStatusBar(self.statusbar)

        self.retranslateUi(KnowledgeEditor)
        QtCore.QMetaObject.connectSlotsByName(KnowledgeEditor)

    def retranslateUi(self, KnowledgeEditor):
        _translate = QtCore.QCoreApplication.translate
        KnowledgeEditor.setWindowTitle(
            _translate(
                "KnowledgeEditor",
                "MainWindow"
            )
        )
        self.printAlloysBtn.setText(
            _translate(
                "KnowledgeEditor",
                "Виды сплавов алюминия"
            )
        )
        self.printPropertiesBtn.setText(
            _translate(
                "KnowledgeEditor",
                "Свойства"
            )
        )
        self.printPossibleValuesBtn.setText(
            _translate(
                "KnowledgeEditor",
                "Возможные значения"
            )
        )
        self.printDescriptionPropertiesBtn.setText(
            _translate(
                "KnowledgeEditor",
                "Описание свойств\n"
                "вида сплава"
            )
        )
        self.printValuesAlloyBtn.setText(
            _translate(
                "KnowledgeEditor",
                "Значения для вида \n"
                "сплава"
            )
        )
        self.label.setText(
            _translate(
                "KnowledgeEditor",
                "Редактор базы знаний"
            )
        )
        self.label_2.setText(_translate("KnowledgeEditor", "Введите ..."))
        self.addButton.setText(_translate("KnowledgeEditor", "Добавить"))
        self.label_3.setText(
            _translate(
                "KnowledgeEditor",
                "Для удаления объекта из списка дважды кликните по нему"
            )
        )
        self.CheckFullKnowledge.setText(
            _translate(
                "KnowledgeEditor",
                "Проверка полноты знаний"
            )
        )

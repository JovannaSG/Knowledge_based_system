# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\UI\valuesAlloy.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ValuesAlloy(object):
    def setupUi(self, ValuesAlloy):
        ValuesAlloy.setObjectName("ValuesAlloy")
        ValuesAlloy.resize(1200, 600)
        ValuesAlloy.setMinimumSize(QtCore.QSize(1200, 600))
        ValuesAlloy.setMaximumSize(QtCore.QSize(1200, 600))
        self.comboBox = QtWidgets.QComboBox(ValuesAlloy)
        self.comboBox.setGeometry(QtCore.QRect(320, 30, 561, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.propertyList = QtWidgets.QListWidget(ValuesAlloy)
        self.propertyList.setGeometry(QtCore.QRect(20, 100, 550, 450))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.propertyList.setFont(font)
        self.propertyList.setObjectName("propertyList")
        self.pushButton = QtWidgets.QPushButton(ValuesAlloy)
        self.pushButton.setGeometry(QtCore.QRect(1050, 510, 130, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.scrollArea = QtWidgets.QScrollArea(ValuesAlloy)
        self.scrollArea.setGeometry(QtCore.QRect(630, 100, 550, 390))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setMinimumSize(QtCore.QSize(550, 390))
        self.scrollArea.setMaximumSize(QtCore.QSize(550, 390))
        self.scrollArea.setBaseSize(QtCore.QSize(550, 390))
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 527, 388))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 551, 391))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.listWidget = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.listWidget.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.listWidget.setContentsMargins(0, 0, 0, 0)
        self.listWidget.setSpacing(1)
        self.listWidget.setObjectName("listWidget")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.retranslateUi(ValuesAlloy)
        QtCore.QMetaObject.connectSlotsByName(ValuesAlloy)

    def retranslateUi(self, ValuesAlloy):
        _translate = QtCore.QCoreApplication.translate
        ValuesAlloy.setWindowTitle(_translate("ValuesAlloy", "Form"))
        self.pushButton.setText(_translate("ValuesAlloy", "Применить"))

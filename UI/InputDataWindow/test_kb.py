# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\UI\InputDataWindow\knowledgeBase.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_KnowledgeBase(object):
    def setupUi(self, KnowledgeBase):
        KnowledgeBase.setObjectName("KnowledgeBase")
        KnowledgeBase.resize(1080, 572)
        KnowledgeBase.setMinimumSize(QtCore.QSize(1080, 572))
        KnowledgeBase.setMaximumSize(QtCore.QSize(1080, 572))
        KnowledgeBase.setBaseSize(QtCore.QSize(1080, 572))
        self.alloyComboBox = QtWidgets.QComboBox(KnowledgeBase)
        self.alloyComboBox.setGeometry(QtCore.QRect(270, 90, 521, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.alloyComboBox.setFont(font)
        self.alloyComboBox.setObjectName("alloyComboBox")
        self.propertyList = QtWidgets.QListWidget(KnowledgeBase)
        self.propertyList.setGeometry(QtCore.QRect(30, 150, 511, 381))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.propertyList.setFont(font)
        self.propertyList.setObjectName("propertyList")
        self.propertyValuesList = QtWidgets.QListWidget(KnowledgeBase)
        self.propertyValuesList.setGeometry(QtCore.QRect(570, 150, 490, 381))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.propertyValuesList.setFont(font)
        self.propertyValuesList.setObjectName("propertyValuesList")
        self.label = QtWidgets.QLabel(KnowledgeBase)
        self.label.setGeometry(QtCore.QRect(390, 20, 291, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.retranslateUi(KnowledgeBase)
        QtCore.QMetaObject.connectSlotsByName(KnowledgeBase)

    def retranslateUi(self, KnowledgeBase):
        _translate = QtCore.QCoreApplication.translate
        KnowledgeBase.setWindowTitle(_translate("KnowledgeBase", "Просмотр базы знаний"))
        self.label.setText(_translate("KnowledgeBase", "Просмотр базы знаний"))
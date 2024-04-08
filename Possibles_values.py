from PyQt5 import QtWidgets

from UI.test_pv import Ui_PossiblesValues
from db import PROPERTIES


class PossiblesValuesForm(QtWidgets.QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.ui = Ui_PossiblesValues()
        self.ui.setupUi(self)

        # connect signal (when comboBox changed)
        self.ui.propertiesList.currentIndexChanged.connect(self.propertiesListChanged)
        self.ui.listWidget.itemDoubleClicked.connect(self.delElement)

        # buttons
        self.ui.pushButton.clicked.connect(self.addBtn)

        # add values in comboBox
        for i in range(len(PROPERTIES.keys())):
            self.ui.propertiesList.insertItem(i, list(PROPERTIES)[i])

    def updateList(self) -> None:
        self.ui.listWidget.clear()
        self.cur = self.ui.propertiesList.currentText()
        for i in PROPERTIES.keys():
            if i == self.cur:
                for j in range(len(PROPERTIES[i]["значения"])):
                    self.ui.listWidget.insertItem(j, str(PROPERTIES[i]["значения"][j]))

    def checkValues(self, values, inputValue: str) -> bool:
        for ls in values:
            for e in ls:
                if e == inputValue:
                    return False
        return True

    def addBtn(self) -> None:
        print(PROPERTIES[self.ui.propertiesList.currentText()])
        if self.ui.inputLine_2.text() == "" and\
           PROPERTIES[self.ui.propertiesList.currentText()]["тип"] is None:
            QtWidgets.QMessageBox.warning(
                self,
                "Информация",
                "Тип свойства не задан"
            )
            return
        
        if self.ui.inputLine_2.text() != "":
            if self.ui.inputLine_2.text() != "исчислимый" and\
                self.ui.inputLine_2.text() != "перечислимый":
                QtWidgets.QMessageBox.warning(
                    self,
                    "Информация",
                    "Неверный тип свойства"
                )
                return
        
        if not (self.checkValues(PROPERTIES.values(), self.ui.inputLine.text()) and self.ui.inputLine.text() != ""):
            QtWidgets.QMessageBox.warning(
                self,
                "Информация",
                "Элемент уже есть или поле ввода пустое"
            )
            return
        
        PROPERTIES[self.ui.propertiesList.currentText()]["тип"] = self.ui.inputLine_2.text()
        PROPERTIES[self.ui.propertiesList.currentText()]["значения"]\
            .append(self.ui.inputLine.text())
        self.updateList()
        QtWidgets.QMessageBox.about(
            self,
            "Информация",
            "Элемент успешно добавлен"
        )
        self.ui.inputLine.clear()

    def changeTextOnLabel(self) -> None:
        if self.ui.propertiesList.currentText() == "Способ обработки":
            self.ui.label.setText("Введите номер и название способа обработки")
        elif self.ui.propertiesList.currentText() == "Механизм упрочнения":
            self.ui.label.setText("Введите название механизма упрочнения")
        elif self.ui.propertiesList.currentText() == "Основной легирующий элемент":
            self.ui.label.setText("Введите название основного легирующего элемента")
        elif self.ui.propertiesList.currentText() == "Предел прочности":
            self.ui.label.setText("Введите предел прочности")
        elif self.ui.propertiesList.currentText() == "Относительное удлинение после разрыва":
            self.ui.label.setText("Введите величину относительного удлинения")
        else:
            self.ui.label.setText("Введите значение")

    def propertiesListChanged(self) -> None:
        self.ui.listWidget.clear()
        self.ui.inputLine.clear()
        self.changeTextOnLabel()
        self.cur = self.ui.propertiesList.currentText()
        for i in PROPERTIES.keys():
            if i == self.cur:
                for j in range(len(PROPERTIES[i]["значения"])):
                    self.ui.listWidget.insertItem(j, str(PROPERTIES[i]["значения"][j]))

    # checking when deleting
    def checkBtn(self) -> bool:
        dlg = QtWidgets.QMessageBox(self)
        dlg.setWindowTitle("Удаление")
        dlg.setText("Вы хотите удалить элемент?")
        dlg.setStandardButtons(
            QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No
        )
        dlg.setIcon(QtWidgets.QMessageBox.Question)
        button = dlg.exec()

        if button == QtWidgets.QMessageBox.Yes:
            return True
        else:
            return False

    def delElement(self) -> None:
        temp_key = self.ui.propertiesList.currentText()
        if self.checkBtn():
            for el in PROPERTIES[temp_key]["значения"]:
                if el == self.ui.listWidget.currentItem().text():
                    PROPERTIES[temp_key]["значения"].remove(el)
                    QtWidgets.QMessageBox.about(
                        self,
                        "Информация",
                        "Элемент успешно удален"
                    )
            self.updateList()

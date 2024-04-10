import re

from PyQt5 import QtWidgets

from UI.test_pv import Ui_PossiblesValues
from db import PROPERTIES


class PossiblesValuesForm(QtWidgets.QWidget):
    #r"\d+.?\d+ - \d+.?\d+"
    _REGEX_CALC_TYPE = r"[0-9]*\.?[0-9]* - [0-9]+"

    def __init__(self) -> None:
        super().__init__()
        self.ui = Ui_PossiblesValues()
        self.ui.setupUi(self)

        # signals
        self.ui.propertiesList.currentIndexChanged.connect(
            self.propertiesListChanged
        )
        self.ui.listWidget.itemDoubleClicked.connect(self.delElement)
        self.ui.pushButton.clicked.connect(self.addBtn)
        self.ui.propertiesList.currentIndexChanged.connect(self.fillComboBox)

        for i in range(len(PROPERTIES.keys())):
            self.ui.propertiesList.insertItem(i, list(PROPERTIES)[i])

        # add values in comboBox
        self.ui.comboBox.setPlaceholderText("")
        self.ui.comboBox.insertItem(0, "перечислимый")
        self.ui.comboBox.insertItem(1, "исчислимый")
        self.fillComboBox()

    def fillComboBox(self):
        if PROPERTIES[self.ui.propertiesList.currentText()]["тип"] == "исчислимый":
            self.ui.comboBox.setCurrentIndex(1)
        elif PROPERTIES[self.ui.propertiesList.currentText()]["тип"] == "перечислимый":
            self.ui.comboBox.setCurrentIndex(0)
        else:
            self.ui.comboBox.setCurrentIndex(-1)

    def updateList(self) -> None:
        self.ui.listWidget.clear()
        self.cur = self.ui.propertiesList.currentText()
        for i in PROPERTIES.keys():
            if i == self.cur:
                for j in range(len(PROPERTIES[i]["значения"])):
                    self.ui.listWidget.insertItem(
                        j,
                        str(PROPERTIES[i]["значения"][j])
                    )

    def checkValues(self, values: dict, inputValue: str) -> bool:
        for el in values["значения"]:
            if el.lower() == inputValue.lower():
                return True
        return False

    def addBtn(self) -> None:
        if self.ui.inputLine.text() == "":
            QtWidgets.QMessageBox.warning(
                self,
                "Информация",
                "Поле ввода значения пустое"
            )
            return

        if self.checkValues(
            PROPERTIES[self.ui.propertiesList.currentText()],
            self.ui.inputLine.text()
        ):
            QtWidgets.QMessageBox.warning(
                self,
                "Информация",
                "Значение свойства уже существует"
            )
            return

        if self.ui.comboBox.currentText() == "":
            QtWidgets.QMessageBox.warning(
                self,
                "Информация",
                "Не выбран тип свойства"
            )
            return

        if PROPERTIES[self.ui.propertiesList.currentText()]["тип"] == "перечислимый":
            PROPERTIES[self.ui.propertiesList.currentText()]["тип"] = self.ui.comboBox.currentText()
            PROPERTIES[self.ui.propertiesList.currentText()]["значения"]\
                .append(self.ui.inputLine.text())
            self.updateList()
            QtWidgets.QMessageBox.about(
                self,
                "Информация",
                "Элемент успешно добавлен"
            )
        elif PROPERTIES[self.ui.propertiesList.currentText()]["тип"] == "исчислимый":
            regex = re.compile(self._REGEX_CALC_TYPE)
            if not regex.match(self.ui.inputLine.text()):
                QtWidgets.QMessageBox.warning(
                    self,
                    "Информация",
                    "Значение диапозона введено неверно"
                )
            else:
                PROPERTIES[self.ui.propertiesList.currentText()]["тип"] = self.ui.comboBox.currentText()
                if len(PROPERTIES[self.ui.propertiesList.currentText()]["значения"]) == 0:
                    PROPERTIES[self.ui.propertiesList.currentText()]["значения"]\
                        .append(self.ui.inputLine.text())
                else:
                    PROPERTIES[self.ui.propertiesList.currentText()]["значения"][0] = self.ui.inputLine.text()
                self.updateList()
                QtWidgets.QMessageBox.about(
                    self,
                    "Информация",
                    "Элемент успешно добавлен"
                )
        elif PROPERTIES[self.ui.propertiesList.currentText()]["тип"] is None:
            if self.ui.comboBox.currentText() == "перечислимый":
                PROPERTIES[self.ui.propertiesList.currentText()]["тип"] = self.ui.comboBox.currentText()
                PROPERTIES[self.ui.propertiesList.currentText()]["значения"]\
                    .append(self.ui.inputLine.text())
                self.updateList()
                QtWidgets.QMessageBox.about(
                    self,
                    "Информация",
                    "Элемент успешно добавлен"
                )
            if self.ui.comboBox.currentText() == "исчислимый":
                regex = re.compile(self._REGEX_CALC_TYPE)
                if not regex.match(self.ui.inputLine.text()):
                    QtWidgets.QMessageBox.warning(
                        self,
                        "Информация",
                        "Значение диапозона введено неверно"
                    )
                else:
                    PROPERTIES[self.ui.propertiesList.currentText()]["тип"] = self.ui.comboBox.currentText()
                    if len(PROPERTIES[self.ui.propertiesList.currentText()]["значения"]) == 0:
                        PROPERTIES[self.ui.propertiesList.currentText()]["значения"]\
                            .append(self.ui.inputLine.text())
                    else:
                        PROPERTIES[self.ui.propertiesList.currentText()]["значения"][0] = self.ui.inputLine.text()
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
            self.ui.label.setText("Введите диапозон (число - число)")
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
                    self.ui.listWidget.insertItem(
                        j,
                        str(PROPERTIES[i]["значения"][j])
                    )

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

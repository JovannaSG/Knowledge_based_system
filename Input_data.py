from PyQt5 import QtWidgets

from UI.InputDataWindow.test_id import Ui_InputData
from Knowledge_base import KnowledgeBaseForm
from Result_description import ResultDescriptionForm
from db import PROPERTIES, ALLOYS


class InputDataForm(QtWidgets.QWidget):
    _FLAG_ACCEPT_BTN: bool = True
    # _REGEX_CALC_TYPE = r"\d+.?\d+ - \d+.?\d+"
    # _REGEX_REAL_NUMBER = r"\d+[.]\d+"
    # [-+]?[0-9]*\.?[0-9]*

    _result_list: dict

    def __init__(self) -> None:
        super().__init__()
        self.ui = Ui_InputData()
        self.ui.setupUi(self)
        self._result_list = dict()

        # filling property list
        for i in range(len(PROPERTIES)):
            self.ui.propertyList.insertItem(i, list(PROPERTIES)[i])

        # signals
        self.ui.viewKnowledgeBase.clicked.connect(self.showKnowledgeBase)
        self.ui.determineTypeAlloy.clicked.connect(self.showTypeAlloy)
        self.ui.propertyList.itemClicked.connect(self.showInputField)
        self.ui.clearInputValues.clicked.connect(self.clearResultList)

    def clearResultList(self) -> None:
        self._result_list = {}
        self.ui.resultList.clear()

    def showKnowledgeBase(self) -> None:
        self.form = KnowledgeBaseForm()
        self.form.show()

    def showTypeAlloy(self) -> None:
        self.form = ResultDescriptionForm()
        self.form.descrptionResult(self._result_list)
        self.form.show()

    def showInputField(self) -> None:
        # clear layout
        for i in range(self.ui.listWidget_4.count()):
            if self.ui.listWidget_4.itemAt(i).widget() is not None:
                self.ui.listWidget_4.itemAt(i).widget().deleteLater()

        if PROPERTIES[self.ui.propertyList.currentItem().text()] == []:
            return

        # check property type
        if PROPERTIES[self.ui.propertyList.currentItem().text()]["тип"] == "исчислимый":
            self._FLAG_ACCEPT_BTN = False

            input_field = QtWidgets.QLineEdit()
            input_field.setFixedWidth(525)
            input_field.setStyleSheet('font: 12pt "MS Shell Dlg 2"')
            input_field.setPlaceholderText(
                "Введите число из диапозона {}".format(
                    PROPERTIES[self.ui.propertyList.currentItem().text()]["значения"][0]
                )
            )
            input_field.returnPressed.connect(self.addInputFieldResultList)
            self.ui.listWidget_4.addWidget(input_field)
        else:
            self._FLAG_ACCEPT_BTN = True
 
            for prop_value in PROPERTIES[self.ui.propertyList.currentItem().text()]["значения"]:
                radioBtn = QtWidgets.QRadioButton(prop_value)
                radioBtn.setGeometry(200, 150, 120, 40)
                radioBtn.setStyleSheet(
                    "QRadioButton"
                    "{"
                    "font : 24px Arial;"
                    "}"
                )
                radioBtn.toggled.connect(self.addRadioButtonResultList)
                self.ui.listWidget_4.addWidget(radioBtn)

    def compare(self, alloy_name: str, prop_value: str) -> bool:
        for el in ALLOYS[alloy_name]:
            if el[0] == self.ui.propertyList.currentItem().text():
                if el[1] is not None:
                    if el[1] == prop_value:
                        return True
                    else:
                        return False
                else:
                    return False
        return False

    def addInputFieldResultList(self) -> None:
        for i in range(self.ui.listWidget_4.count()):
            w: QtWidgets.QWidget = self.ui.listWidget_4.itemAt(i).widget()
            if w.text() != "":
                try:                
                    _range = PROPERTIES[self.ui.propertyList.currentItem().text()]["значения"][0]\
                        .split(" ")
                    if float(w.text()) < float(_range[0]) or\
                        float(w.text()) > float(_range[2]):
                        QtWidgets.QMessageBox.warning(
                            self,
                            "Информация",
                            "Введенное значение вне диапозона"
                        )
                        return
                except ValueError as e:
                    QtWidgets.QMessageBox.warning(
                        self,
                        "Информация",
                        "Неверно введено число"
                    )
                    return

                self._result_list[self.ui.propertyList.currentItem().text()] = w.text()
                self.printResultList()
            else:
                QtWidgets.QMessageBox.warning(
                    self,
                    "Информация",
                    "Поле не должно быть пустым"
                )

    def addRadioButtonResultList(self) -> None:
        for i in range(self.ui.listWidget_4.count()):
            w: QtWidgets.QWidget = self.ui.listWidget_4.itemAt(i).widget()
            if w.isChecked():
                self._result_list[self.ui.propertyList.currentItem().text()] = w.text()
                break
        self.printResultList()

    def printResultList(self) -> None:
        self.ui.resultList.clear()
        i = 0
        for key in self._result_list.keys():
            self.ui.resultList.insertItem(
                i,
                f"{key}: {self._result_list[key]}"
            )
            i += 1

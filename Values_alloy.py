from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt

from UI.test_va import Ui_ValuesAlloy
from db import PROPERTIES, ALLOYS


class ValuesAlloyForm(QtWidgets.QWidget):
    _FLAG_ACCEPT_BTN: bool = True
    # _REGEX_CALC_TYPE = r"\d+.?\d+ - \d+.?\d+"
    # _REGEX_REAL_NUMBER = r"\d+[.]\d+"

    def __init__(self) -> None:
        super().__init__()
        self.ui = Ui_ValuesAlloy()
        self.ui.setupUi(self)
        self.ui.listWidget.setAlignment(Qt.AlignmentFlag.AlignTop)

        # make layout scrolling
        w = QtWidgets.QWidget()
        w.setLayout(self.ui.listWidget)
        self.ui.scrollArea.setWidget(w)

        # signals
        self.ui.propertyList.itemClicked.connect(self.fillingValuesList)
        self.ui.pushButton.clicked.connect(self.acceptChanges)
        self.ui.comboBox.currentIndexChanged.connect(self.fillingPropertyList)

        # add values in comboBox
        for i in range(len(ALLOYS.keys())):
            self.ui.comboBox.insertItem(i, list(ALLOYS)[i])

    def fillingPropertyList(self) -> None:
        self.ui.propertyList.clear()

        # clear layout
        for i in range(self.ui.listWidget.count()):
            if self.ui.listWidget.itemAt(i).widget() is not None:
                self.ui.listWidget.itemAt(i).widget().deleteLater()

        key = self.ui.comboBox.currentText()
        for i in range(len(ALLOYS[key])):
            self.ui.propertyList.insertItem(i, ALLOYS[key][i][0])

    def fillingValuesList(self) -> None:
        # clear layout
        for i in range(self.ui.listWidget.count()):
            if self.ui.listWidget.itemAt(i).widget() is not None:
                self.ui.listWidget.itemAt(i).widget().deleteLater()

        if PROPERTIES[self.ui.propertyList.currentItem().text()] == []:
            return

        alloy_name = self.ui.comboBox.currentText()
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
            self.ui.listWidget.addWidget(input_field)
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
                radioBtn.setChecked(self.compare(alloy_name, prop_value))
                self.ui.listWidget.addWidget(radioBtn)

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

    def acceptChanges(self):
        alloy_name = self.ui.comboBox.currentText()
        if self._FLAG_ACCEPT_BTN:
            for i in range(self.ui.listWidget.count()):
                w: QtWidgets.QWidget = self.ui.listWidget.itemAt(i).widget()
                if w.isChecked():
                    for el in ALLOYS[alloy_name]:
                        if el[0] == self.ui.propertyList.currentItem().text():
                            el[1] = w.text()
                            QtWidgets.QMessageBox.about(
                                self,
                                "Информация",
                                "Изменения успешно применены"
                            )
                            return
        else:
            for i in range(self.ui.listWidget.count()):
                w: QtWidgets.QWidget = self.ui.listWidget.itemAt(i).widget()
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

                    for el in ALLOYS[alloy_name]:
                        if el[0] == self.ui.propertyList.currentItem().text():
                            el[1] = w.text()
                            QtWidgets.QMessageBox.about(
                                self,
                                "Информация",
                                "Изменения успешно применены"
                            )
                            return
                else:
                    QtWidgets.QMessageBox.warning(
                        self,
                        "Информация",
                        "Поле не должно быть пустым"
                    )

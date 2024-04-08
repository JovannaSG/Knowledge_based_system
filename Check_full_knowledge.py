from PyQt5 import QtWidgets

from UI.test_cfk import Ui_Form
from db import PROPERTIES, ALLOYS


class CheckFullKwnoledgeForm(QtWidgets.QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        # signals
        self.ui.listWidget_3.itemClicked.connect(self.showEmptyProps)

        # filling alloy list
        flag = False
        for alloy_key in ALLOYS.keys():
            for prop in ALLOYS[alloy_key]:
                if prop[1] is None:
                    self.ui.listWidget_3.addItem(alloy_key)
                    flag = True
                    break

        for prop_key in PROPERTIES.keys():
            if PROPERTIES[prop_key]["значения"] == []:
                self.ui.listWidget.addItem(prop_key)
                flag = True

        if flag:
            self.ui.label.setText("Есть незаполненные поля")

    def showEmptyProps(self) -> None:
        self.ui.listWidget_4.clear()
        cur_item = self.ui.listWidget_3.currentItem().text()
        for prop in ALLOYS[cur_item]:
            if prop[1] is None:
                self.ui.listWidget_4.addItem(prop[0])

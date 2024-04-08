from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt

from UI.test_dpoa import Ui_Form
from db import PROPERTIES, ALLOYS


class DescriptionPropertiesAlloyForm(QtWidgets.QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        # signals
        self.ui.listWidget.itemClicked.connect(self.fillingPropertyList)
        self.ui.pushButton.clicked.connect(self.addAllProps)
        self.ui.acceptBtn.clicked.connect(self.acceptChanges)

        # filling alloy list
        for i in range(len(ALLOYS)):
            self.ui.listWidget.addItem(list(ALLOYS)[i])

    def fillingPropertyList(self) -> None:
        self.ui.listWidget_2.clear()
        key = self.ui.listWidget.currentItem().text()
        properties_keys = list(PROPERTIES)            
        for k in properties_keys:
            item = QtWidgets.QListWidgetItem(k)
            for el in ALLOYS[key]:
                if k == el[0]:
                    item.setCheckState(Qt.CheckState.Checked)
                    break
            else:
                item.setCheckState(Qt.CheckState.Unchecked)
            self.ui.listWidget_2.addItem(item)

    def addAllProps(self) -> None:
        for i in range(self.ui.listWidget_2.count()):
            self.ui.listWidget_2.item(i).setCheckState(Qt.CheckState.Checked)

    def acceptChanges(self) -> None:
        alloy_name = self.ui.listWidget.currentItem().text()
        to_del_list = list()
        to_add_list = list()
        for i in range(self.ui.listWidget_2.count()):
            flag = True
            for el in ALLOYS[alloy_name]:
                if self.ui.listWidget_2.item(i).text() == el[0]:
                    flag = False
                    if self.ui.listWidget_2.item(i).checkState() == Qt.CheckState.Unchecked:
                        to_del_list.append(el)
            if flag:
                if self.ui.listWidget_2.item(i).checkState() == Qt.CheckState.Checked:
                    to_add_list.append(self.ui.listWidget_2.item(i).text())

        # del props
        for el in to_del_list:
            if el in ALLOYS[alloy_name]:
                ALLOYS[alloy_name].remove(el)

        # add props
        for el in to_add_list:
            ALLOYS[alloy_name].append([el, None])

        QtWidgets.QMessageBox.about(
            self,
            "Информация",
            "Изменения успешно применены"
        )

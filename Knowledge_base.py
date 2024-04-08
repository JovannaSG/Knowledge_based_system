from PyQt5 import QtWidgets

from UI.InputDataWindow.test_kb import Ui_KnowledgeBase
from db import PROPERTIES, ALLOYS


class KnowledgeBaseForm(QtWidgets.QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.ui = Ui_KnowledgeBase()
        self.ui.setupUi(self)

        # signals
        self.ui.alloyComboBox.currentIndexChanged.connect(
            self.onAlloyComboBoxChanged
        )
        self.ui.propertyList.itemClicked.connect(
            self.fillingPropertyValuesList
        )

        # filling alloyComboBox
        for i in range(len(ALLOYS.keys())):
            self.ui.alloyComboBox.insertItem(i, list(ALLOYS)[i])

    def onAlloyComboBoxChanged(self) -> None:
        self.ui.propertyList.clear()
        self.ui.propertyValuesList.clear()
        key = self.ui.alloyComboBox.currentText()
        for i in range(len(ALLOYS[key])):
            self.ui.propertyList.insertItem(i, ALLOYS[key][i][0])

    def fillingPropertyValuesList(self) -> None:
        self.ui.propertyValuesList.clear()
        prop_key = self.ui.propertyList.currentItem().text()
        alloy_key = self.ui.alloyComboBox.currentText()
        for i in range(len(ALLOYS[alloy_key])):
            if ALLOYS[alloy_key][i][0] == prop_key:
                self.ui.propertyValuesList.insertItem(
                    i,
                    str(ALLOYS[alloy_key][i][1])
                )
                break

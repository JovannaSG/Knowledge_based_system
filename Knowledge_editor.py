from PyQt5 import QtWidgets

from UI.test_ui import Ui_KnowledgeEditor
from Possibles_values import PossiblesValuesForm
from Description_properties_of_alloy import DescriptionPropertiesAlloyForm
from Values_alloy import ValuesAlloyForm
from Check_full_knowledge import CheckFullKwnoledgeForm
from db import DB, PROPERTIES, ALLOYS


class Example(QtWidgets.QMainWindow):
    # _add_alloy_flag = False
    # _add_prop_flag = False

    def __init__(self) -> None:
        super().__init__()
        self.ui = Ui_KnowledgeEditor()
        self.ui.setupUi(self)

        # connect signals to buttons
        self.ui.printAlloysBtn.clicked.connect(self.printAlloys)
        self.ui.printPropertiesBtn.clicked.connect(self.printProperties)
        self.ui.printPossibleValuesBtn.clicked.connect(
            self.printPossiblesValues
        )
        self.ui.printDescriptionPropertiesBtn.clicked.connect(
            self.printDescriptionProperties
        )
        self.ui.printValuesAlloyBtn.clicked.connect(self.printValuesAlloy)
        self.ui.addButton.clicked.connect(self.add)
        self.ui.CheckFullKnowledge.clicked.connect(self.isFullKnowledge)
        self.ui.resultList.itemDoubleClicked.connect(self.delElement)

    # check when deleting
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

    # for removal functional
    def delElement(self) -> None:
        temp_key = ""
        if self.checkBtn():
            if self.ui.label_2.text() == "Введите название сплава алюминия":   
                for el in ALLOYS:
                    if el == self.ui.resultList.currentItem().text():
                        temp_key = el
                del ALLOYS[temp_key]
                QtWidgets.QMessageBox.about(
                    self,
                    "Информация",
                    "Элемент успешно удален"
                )
                self.printAlloys()

            if self.ui.label_2.text() == "Введите название свойства":
                for el in PROPERTIES:
                    if el == self.ui.resultList.currentItem().text():
                        temp_key = el
                del PROPERTIES[temp_key]
                DB.saveDataDB(PROPERTIES, "props")
                QtWidgets.QMessageBox.about(
                    self,
                    "Информация",
                    "Элемент успешно удален"
                )
                self.printProperties()

    def printAlloys(self) -> None:
        self.ui.label_2.setText("Введите название сплава алюминия")
        self.ui.lineEdit.clear()
        self.ui.resultList.clear()
        for i in range(len(ALLOYS.keys())):
            self.ui.resultList.insertItem(i, list(ALLOYS)[i])

    def printProperties(self) -> None:
        self.ui.label_2.setText("Введите название свойства")
        self.ui.lineEdit.clear()
        self.ui.resultList.clear()
        for i in range(len(PROPERTIES)):
            self.ui.resultList.insertItem(i, list(PROPERTIES)[i])

    def printPossiblesValues(self) -> None:
        self.form = PossiblesValuesForm()
        self.form.show()

    def printDescriptionProperties(self) -> None:
        self.dpoa_form = DescriptionPropertiesAlloyForm()
        self.dpoa_form.show()

    def printValuesAlloy(self) -> None:
        self.va_form = ValuesAlloyForm()
        self.va_form.show()

    def add(self) -> None:
        # adding new alloy
        if self.ui.label_2.text() == "Введите название сплава алюминия":   
            if self.ui.lineEdit.text() != "":
                ALLOYS[self.ui.lineEdit.text()] = []
                QtWidgets.QMessageBox.about(
                    self,
                    "Информация",
                    "Элемент успешно добавлен"
                )
                self.ui.resultList.clear()
                for i in range(len(ALLOYS.keys())):
                    self.ui.resultList.insertItem(i, list(ALLOYS)[i])
                self.ui.lineEdit.clear()
            else:
                QtWidgets.QMessageBox.warning(
                    self,
                    "Информация",
                    "Поле не должно быть пустым"
                )

        #adding new property
        if self.ui.label_2.text() == "Введите название свойства":
            if self.ui.lineEdit.text() != "":
                PROPERTIES[self.ui.lineEdit.text()] = {
                    "тип": None,
                    "значения": []
                }
                self.ui.resultList.clear()
                for i in range(len(PROPERTIES)):
                    self.ui.resultList.insertItem(i, list(PROPERTIES)[i])
                QtWidgets.QMessageBox.about(
                    self,
                    "Информация",
                    "Элемент успешно добавлен"
                )
                self.ui.lineEdit.clear()
            else:
                QtWidgets.QMessageBox.warning(
                    self,
                    "Информация",
                    "Поле не должно быть пустым"
                )

    def isFullKnowledge(self) -> None:
        self.form = CheckFullKwnoledgeForm()
        self.form.show()

    # on close mainWindow
    def closeEvent(self, event) -> None:
        DB.saveDataDB(ALLOYS, "alloys")
        DB.saveDataDB(PROPERTIES, "props")
        event.accept()

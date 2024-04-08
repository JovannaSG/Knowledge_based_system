from PyQt5 import QtWidgets

from UI.selection_window import Ui_selectionWindow
from Knowledge_editor import Example
from Input_data import InputDataForm


class SelectionWindowForm(QtWidgets.QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.ui = Ui_selectionWindow()
        self.ui.setupUi(self)

        # signals
        self.ui.openKnowledgeEditorWindow.clicked.connect(
            self.openKnowledgeEditor
        )
        self.ui.openInputDataWindow.clicked.connect(self.openInputData)

    def openKnowledgeEditor(self) -> None:
        self.form = Example()
        self.form.show()

    def openInputData(self) -> None:
        self.form = InputDataForm()
        self.form.show()

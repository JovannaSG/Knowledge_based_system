import sys

from PyQt5 import QtWidgets

from db import DB
from Selection_window import SelectionWindowForm


"""
TODO: убрать вывод пустых свойств в решателе задач - МОЖНО УБРАТЬ
TODO: переделать вывод строк changeTextOnLabel() Possibles_values.py
"""


if __name__ == "__main__":
    DB.fillingDB()
    app = QtWidgets.QApplication([])
    # app.setStyle("Windows")
    application = SelectionWindowForm()
    application.show()

    sys.exit(app.exec())

import sys

from PyQt5 import QtWidgets

from db import DB
from Selection_window import SelectionWindowForm


"""
TODO: убрать вывод пустых свойств в решателе задач - МОЖНО УБРАТЬ
TODO: добавить флаги для добавления сплавов и свойств - ОСТАЛОСЬ ТЕСТИТЬ
TODO: переделать вывод строк "Введите ..."
"""


if __name__ == "__main__":
    DB.fillingDB()
    app = QtWidgets.QApplication([])
    # app.setStyle("Windows")
    application = SelectionWindowForm()
    application.show()

    sys.exit(app.exec())

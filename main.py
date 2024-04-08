import sys

from PyQt5 import QtWidgets

from db import DB
from Selection_window import SelectionWindowForm


"""
TODO: что будет если попробую ввести новый диапозон для свойства
TODO: убрать вывод пустых свойств
TODO: не выводит незаполненные свойства при проверк полноты знаний
"""


if __name__ == "__main__":
    DB.fillingDB()
    app = QtWidgets.QApplication([])
    # app.setStyle("Windows")
    application = SelectionWindowForm()
    application.show()

    sys.exit(app.exec())

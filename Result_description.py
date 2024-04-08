from PyQt5 import QtWidgets

from UI.test_rd import Ui_Result
from db import PROPERTIES, ALLOYS


class ResultDescriptionForm(QtWidgets.QWidget):
    _right_alloys: dict
    _wrong_alloys: dict

    def __init__(self) -> None:
        super().__init__()
        self.ui = Ui_Result()
        self.ui.setupUi(self)
        self._right_alloys = dict()
        self._wrong_alloys = dict()

    def descrptionResult(self, result_list: dict) -> None:
        c = len(result_list)

        if c == 0:
            self.printAnswer()
            return

        for key in ALLOYS.keys():
            i = 0
            right = list()
            wrong = list()
            for el in ALLOYS[key]:
                if el[0] in result_list.keys():
                    if str(el[1]) == str(result_list[el[0]]):
                        right.append(el)
                        i += 1
                    else:
                        wrong.append(el)
                else:
                    wrong.append(el)
            if i == c:
                self._right_alloys[key] = right
            else:
                self._wrong_alloys[key] = wrong
        self.printAnswer()

    def printAnswer(self) -> None:
        if self._right_alloys == {}:
            s = "Вид сплава не определён.\n"
            s += "Сплав не является сплавом алюминия или знания об этом виде сплава алюминия не занесены в систему.\n"
            s += "Обратитесь к эксперту для разрешения проблемы.\n"
            s += "Все виды сплавов опровергнуты по следующим причинам:\n"
            for alloy in ALLOYS.keys():
                if alloy not in self._right_alloys:
                    s += f"\nВид сплава «{alloy}» опровергнут, так как\n"
                    for value in ALLOYS[alloy]:
                        s += f"значение «{value[1]}» свойства «{value[0]}» не соответствует описанию вида сплава\n"
        else:
            s = "Подходящие виды сплавов:\n"
            for key in self._right_alloys.keys():
                s += f"«{key}»\n"
                #for value in self._right_alloys[key]:
                #    s += f"\t{value}\n"
            s += "\nДругие виды сплавов опровергнуты по следующим причинам:\n"
            for alloy in ALLOYS.keys():
                if alloy not in self._right_alloys:
                    s += f"\nВид сплава «{alloy}» опровергнут, так как\n"
                    for value in ALLOYS[alloy]:
                        s += f"значение «{value[1]}» свойства «{value[0]}» не соответствует описанию вида сплава\n"
        self.ui.textEdit.setText(s)

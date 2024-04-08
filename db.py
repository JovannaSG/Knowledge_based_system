import json


PROPERTIES = dict()
ALLOYS = dict()


class DB():
    @staticmethod
    def fillingDB() -> None:
        with open("DB/props1.json", "r", encoding="utf-8") as f:
            props = json.load(f)
            for el in props:
                PROPERTIES[el] = props[el]

        with open("DB/alloys.json", "r", encoding="utf-8") as f:
            alloys = json.load(f)
            for el in alloys:
                ALLOYS[el] = alloys[el]

    @staticmethod
    def saveDataDB(data: dict, file_name: str) -> None:
        with open(f"DB/{file_name}.json", "w", encoding="utf-8") as jf:
            json.dump(data, jf, ensure_ascii=False)


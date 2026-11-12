# -*- coding: utf-8 -*-
from pathlib import Path

import pytest
from src.Types import DataType
from src.JsonDataReader import JsonDataReader

DATA_FILE = Path(__file__).parent.parent / "data" / "data.json"


class TestJsonDataReader:

    @pytest.fixture()
    def file_and_data_content(self) -> tuple[str, DataType]:
        text = """
        {
            "Иванов Константин Дмитриевич": {
                "математика": 91,
                "химия": 100
            },
            "Петров Петр Семенович": {
                "русский язык": 87,
                "литература": 78
            }
        }
        """

        data = {
            "Иванов Константин Дмитриевич": [
                ("математика", 91), ("химия", 100)
            ],
            "Петров Петр Семенович": [
                ("русский язык", 87), ("литература", 78)
            ]
        }
        return text, data

    @pytest.fixture()
    def filepath_and_data(self,
                          file_and_data_content: tuple[str, DataType],
                          tmpdir) -> tuple[str, DataType]:
        p = tmpdir.mkdir("datadir").join("my_data.json")
        p.write_text(file_and_data_content[0], encoding='utf-8')
        return str(p), file_and_data_content[1]

    def test_read(self, filepath_and_data: tuple[str, DataType]) -> None:
        file_content = JsonDataReader().read(filepath_and_data[0])
        assert file_content == filepath_and_data[1]

    def test_read_empty_file(self, tmpdir) -> None:
        p = tmpdir.mkdir("emptydir").join("empty.json")
        p.write_text("{}", encoding='utf-8')
        assert JsonDataReader().read(str(p)) == {}

    def test_read_real_data_file(self) -> None:
        students = JsonDataReader().read(str(DATA_FILE))
        assert "Иванов Иван Иванович" in students
        assert ("математика", 67) in students["Иванов Иван Иванович"]

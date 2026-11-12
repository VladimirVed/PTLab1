# -*- coding: utf-8 -*-
import json

from Types import DataType
from DataReader import DataReader


class JsonDataReader(DataReader):

    def read(self, path: str) -> DataType:
        with open(path, encoding='utf-8') as file:
            content: dict[str, dict[str, int]] = json.load(file)
        return {
            student: [(subject, int(score))
                      for subject, score in subjects.items()]
            for student, subjects in content.items()
        }

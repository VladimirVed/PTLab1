# -*- coding: utf-8 -*-
from Types import DataType

PASSING_SCORE = 61


class CalcDebts:

    def __init__(self, data: DataType) -> None:
        self.data: DataType = data

    def calc(self) -> int:
        return sum(
            1 for subjects in self.data.values()
            if any(score < PASSING_SCORE for _, score in subjects)
        )

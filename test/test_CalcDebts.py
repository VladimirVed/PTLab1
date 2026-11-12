# -*- coding: utf-8 -*-
import pytest
from src.Types import DataType
from src.CalcDebts import CalcDebts


class TestCalcDebts:

    @pytest.fixture()
    def data(self) -> DataType:
        return {
            "Абрамов Петр Сергеевич": [
                ("математика", 80),
                ("русский язык", 76),
                ("программирование", 100)
            ],
            "Петров Игорь Владимирович": [
                ("математика", 60),
                ("русский язык", 80),
                ("программирование", 78),
                ("литература", 97)
            ],
            "Сидоров Иван Петрович": [
                ("математика", 61),
                ("химия", 45)
            ]
        }

    def test_init_calc_debts(self, data: DataType) -> None:
        calc_debts = CalcDebts(data)
        assert data == calc_debts.data

    def test_calc(self, data: DataType) -> None:
        assert CalcDebts(data).calc() == 2

    def test_boundary_score_is_not_debt(self) -> None:
        data: DataType = {"Иванов Иван Иванович": [("химия", 61)]}
        assert CalcDebts(data).calc() == 0

    def test_no_debts(self) -> None:
        data: DataType = {
            "Иванов Иван Иванович": [("химия", 61), ("физика", 100)]
        }
        assert CalcDebts(data).calc() == 0

    def test_empty_data(self) -> None:
        assert CalcDebts({}).calc() == 0

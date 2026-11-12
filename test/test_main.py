# -*- coding: utf-8 -*-
from src.main import get_path_from_arguments, get_reader
import pytest


@pytest.fixture()
def correct_arguments_string() -> tuple[list[str], str]:
    return ["-p", "/home/user/file.txt"], "/home/user/file.txt"


@pytest.fixture()
def noncorrect_arguments_string() -> list[str]:
    return ["/home/user/file.txt"]


def test_get_path_from_correct_arguments(
        correct_arguments_string: tuple[list[str], str]) -> None:
    path = get_path_from_arguments(correct_arguments_string[0])
    assert path == correct_arguments_string[1]


def test_get_path_from_noncorrect_arguments(
        noncorrect_arguments_string: list[str]) -> None:
    with pytest.raises(SystemExit) as e:
        get_path_from_arguments(noncorrect_arguments_string[0])
    assert e.type == SystemExit


def test_get_reader_for_text_file() -> None:
    assert type(get_reader("data/data.txt")).__name__ == "TextDataReader"


def test_get_reader_for_json_file() -> None:
    assert type(get_reader("data/data.json")).__name__ == "JsonDataReader"


def test_get_reader_for_uppercase_extension() -> None:
    assert type(get_reader("DATA.JSON")).__name__ == "JsonDataReader"


def test_get_reader_for_unknown_format() -> None:
    with pytest.raises(ValueError):
        get_reader("data/data.xml")

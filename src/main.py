# -*- coding: utf-8 -*-
import argparse
import sys

from CalcRating import CalcRating
from DataReader import DataReader
from JsonDataReader import JsonDataReader
from TextDataReader import TextDataReader

READERS: dict[str, type[DataReader]] = {
    ".json": JsonDataReader,
    ".txt": TextDataReader,
}


def get_path_from_arguments(args) -> str:
    parser = argparse.ArgumentParser(description="Path to datafile")
    parser.add_argument("-p", dest="path", type=str, required=True,
                        help="Path to datafile")
    args = parser.parse_args(args)
    return args.path


def get_reader(path: str) -> DataReader:
    for extension, reader_class in READERS.items():
        if path.lower().endswith(extension):
            return reader_class()
    raise ValueError(f"Unsupported data file format: {path}")


def main():
    path = get_path_from_arguments(sys.argv[1:])

    reader = get_reader(path)
    students = reader.read(path)
    print("Students: ", students)

    rating = CalcRating(students).calc()
    print("Rating: ", rating)


if __name__ == "__main__":
    main()

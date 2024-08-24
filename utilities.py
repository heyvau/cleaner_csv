import json
import csv
import pandas as pd
from pathlib import Path


def abs_path(func):
    def wrapper(*args, **kwargs):
        filename = kwargs.get("filename")
        kwargs["filename"] = Path(__file__).resolve().parent / filename
        try:
            return func(*args, **kwargs)
        except FileNotFoundError:
            print(f"Die Datei '{filename}' konnte nicht gefunden werden.")
    return wrapper


class FileReader:
    @staticmethod
    @abs_path
    def read_csv(filename: str, sep: str = ",") -> pd.DataFrame:
        """
        A function returns data as pandas dataframe from a given CSV file.
        """
        return pd.read_csv(filename, sep=sep)


    @staticmethod
    @abs_path
    def read_json(filename: str) -> dict:
        """
        A function returns data as dict from a given JSON file.
        """
        with open(filename, mode="r", encoding="utf-8") as f:
                return json.load(f)

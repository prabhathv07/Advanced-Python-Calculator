from pathlib import Path
import pandas as pd

class HistoryManager:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.__init__()
        return cls._instance

    def __init__(self):
        self.history = pd.DataFrame(columns=["Operation", "Result"])
        self.history_file = Path("history.csv")

    def add_record(self, operation: str, result: float) -> None:
        new_record = pd.DataFrame([[operation, result]], columns=["Operation", "Result"])
        if self.history.empty:
            self.history = new_record
        else:
            self.history = pd.concat([self.history, new_record], ignore_index=True)

    def save_history(self) -> None:
        self.history.to_csv(self.history_file, index=False)

    def load_history(self) -> None:
        if self.history_file.exists():
            self.history = pd.read_csv(self.history_file)

    def clear_history(self) -> None:
        self.history = pd.DataFrame(columns=["Operation", "Result"])

    def reset(self) -> None:
        self.clear_history()
        if self.history_file.exists():
            self.history_file.unlink()

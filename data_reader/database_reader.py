import pandas as pd
from .reader import Reader


class DatabaseReader(Reader):
    def __init__(self, file_path):
        self.database_path = ''
        self.emails = []
        self.file_path = file_path


    def read(self):
        try:
            df = pd.read_excel(self.file_path)
            df = df.drop_duplicates(subset=['Email'])
            self.emails = df['Email'].tolist()
        except FileNotFoundError:
            print('File not found')
        except Exception:
            print('File is not in xlsx format')

    def get_data(self):
        return self.emails


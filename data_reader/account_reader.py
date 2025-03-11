from data_reader.reader import Reader

class Account:
    def __init__(self, email, password):
        self.email = email
        self.password = password


class AccountReader(Reader):
    def __init__(self, file_path):
        self.accounts = []
        self.file_path = file_path


    def read(self):
        try:
            with open(self.file_path, "r", encoding="utf-8") as file:
                for line in file:
                    line = line.strip()
                    if ":" in line:
                        email, password = line.split(":", 1)
                        self.accounts.append(Account(email, password))
                    else:
                        print(f"⚠ Некорректная строка: {line}")

            return self.accounts

        except FileNotFoundError:
            print(f"❌ Файл {self.file_path} не найден")
            return []
        except Exception as e:
            print(f"❌ Ошибка при чтении файла: {e}")
            return []


    def get_data(self):
        return self.accounts

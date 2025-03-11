from abc import ABC, abstractmethod

class Reader(ABC):
    @abstractmethod
    def read(self):
        """Метод для чтения данных."""
        pass

    def get_data(self):
        """Метод для получения данных."""
        pass

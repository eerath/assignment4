# Calculation File

# Import abstract method and operations 
from abc import ABC, abstractmethod 
from app.operations import Operation

# Create calculation class with ABC abstract method
class Calculation(ABC):
    def __init__(self, a: float, b: float) -> None:
        self.a: float = a
        self.b: float = b

        @abstractmethod
        def execute(self) -> float: 
            pass
        def __str__(self) -> str:
            result = self.execute()
            operation_name = self.__class__.__name__.replace('Calculation', '')
            return f"{self.__class__.__name__}: {self.a} {operation_name} {self.b} = {result}"
        def __repr__(self) -> str:
            return f"{self.__class__.__name__}(a={self.a}, b={self.b})"


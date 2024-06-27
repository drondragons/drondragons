import abc


__all__ = [
    "StaticClass",
]


class StaticClass(abc.ABC):
    """
    Абстрактный статический класс
    """
    
    def __new__(cls) -> None:
        """
        Предотвращает создание экземпляра класса

        Raises:
            TypeError: исключение для предотвращения создания экземпляра класса
        """
        
        raise TypeError(f"Недопустимо создание экземпляра класса {cls.__name__}!")
import datetime

from ..static_class import StaticClass


__all__ = [
    "Greeting",
]


class Greeting(StaticClass):
    """
    Класс для получения приветствия в зависимости от времени суток
    """
    
    WAVING_HAND = """<img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Hand%20gestures/Waving%20Hand.png" alt="Waving Hand" width="40" height="40"/>"""
    
    GREETINGS = {i: "Доброе утро" for i in range(4, 12)}
    GREETINGS.update({i: "Добрый день" for i in range(12, 18)})
    GREETINGS.update({i: "Добрый вечер" for i in range(18, 22)})
    GREETINGS.update({i: "Доброй ночи" for i in range(22, 24)})
    GREETINGS.update({i: "Доброй ночи" for i in range(0, 4)})
    
    @classmethod
    def __get_greeting(cls, hour: int) -> str:
        """
        Возвращает приветствие в зависимости от заданного часа дня
        
        Args:
            hour (int): час дня, для которого нужно получить приветствие

        Returns:
            str: приветствие в виде строки
        """
        return cls.GREETINGS[hour]
    
    @classmethod
    def greeting(cls) -> str:
        """
        Возвращает приветствие в зависимости от текущего времени суток
        
        Returns:
            str: приветствие в виде строки
        """
        return cls.__get_greeting(datetime.datetime.now().hour)
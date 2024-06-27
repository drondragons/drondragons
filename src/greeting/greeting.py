import datetime

from ..static_class import StaticClass


__all__ = [
    "Greeting",
]


class Greeting(StaticClass):
    """
    Класс для получения приветствия в зависимости от времени суток
    """
    
    BASE_URL = """https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/"""
    
    IMG_SETTINGS = """width="40" height="40" align="center" """
    
    WAVING_HAND = f"""<img src="{BASE_URL}Hand%20gestures/Waving%20Hand.png" alt="Waving Hand" {IMG_SETTINGS}/>"""
    
    MORNING = f"""<img src="{BASE_URL}Travel%20and%20places/Sunset.png" alt="Morning" {IMG_SETTINGS}/>"""
    AFTERNOON = f"""<img src="{BASE_URL}Travel%20and%20places/Cityscape.png" alt="Afternoon" {IMG_SETTINGS}/>"""
    EVENING = f"""<img src="{BASE_URL}Travel%20and%20places/Cityscape%20at%20Dusk.png" alt="Evening" {IMG_SETTINGS}/>"""
    NIGHT = f"""<img src="{BASE_URL}Travel%20and%20places/Night%20with%20Stars.png" alt="Night" {IMG_SETTINGS}/>"""
    
    @classmethod
    def __initialize_greetings(cls) -> None:
        """
        Инициализация приветствий
        """
        cls.greetings = {i: f"{cls.MORNING} Доброе утро" for i in range(4, 12)}
        cls.greetings.update({i: f"{cls.AFTERNOON} Добрый день" for i in range(12, 18)})
        cls.greetings.update({i: f"{cls.EVENING} Добрый вечер" for i in range(18, 22)})
        cls.greetings.update({i: f"{cls.NIGHT} Доброй ночи" for i in range(22, 24)})
        cls.greetings.update({i: f"{cls.NIGHT} Доброй ночи" for i in range(0, 4)})
    
    @classmethod
    def __get_greeting(cls, hour: int) -> str:
        """
        Возвращает приветствие в зависимости от заданного часа дня
        
        Args:
            hour (int): час дня, для которого нужно получить приветствие

        Returns:
            str: приветствие в виде строки
        """
        if not hasattr(cls, "greetings"):
            cls.__initialize_greetings()
        return cls.greetings[hour]
    
    @classmethod
    def greeting(cls) -> str:
        """
        Возвращает приветствие в зависимости от текущего времени суток
        
        Returns:
            str: приветствие в виде строки
        """
        return cls.__get_greeting(datetime.datetime.now().hour)
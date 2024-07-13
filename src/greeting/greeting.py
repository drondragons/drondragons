import datetime
import zoneinfo

from ..static_class import StaticClass


__all__ = [
    "Greeting",
]


class Greeting(StaticClass):
    """
    Класс для получения приветствия в зависимости от времени суток
    """
    
    BASE_URL = """https://raw.githubusercontent.com/"""
    URL = BASE_URL + """Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/"""
    
    IMG_SETTINGS = """width="40" height="40" align="center" """
    
    HAND_DIR = """Hand%20gestures/"""
    TIME_DIR = """Travel%20and%20places/"""
    
    @classmethod
    def __create_emoji(cls, title: str, alt_title: str) -> str:
        """
        Создание html img тэг

        Args:
            title (str): название файла с эмодзи
            alt_title (str): название эмодзи при ошибке

        Returns:
            str: html img тэг
        """
        return f"""<img src="{cls.URL}{title}" alt="{alt_title}" {cls.IMG_SETTINGS}/>"""
    
    @classmethod
    def __create_hand_emoji(cls, filename: str, alt_title: str) -> str:
        """
        Создание эмодзи рук

        Args:
            filename (str): название файла с эмодзи
            alt_title (str): название эмодзи при ошибке

        Returns:
            str: html img тэг
        """
        return cls.__create_emoji(cls.HAND_DIR + filename, alt_title)
    
    @classmethod
    def __create_time_emoji(cls, filename: str, alt_title: str) -> str:
        """
        Создание эмодзи времени

        Args:
            filename (str): название файла с эмодзи
            alt_title (str): название эмодзи при ошибке

        Returns:
            str: html img тэг
        """
        return cls.__create_emoji(cls.TIME_DIR + filename, alt_title)
    
    @classmethod
    def __initialize_greetings(cls) -> None:
        """
        Инициализация приветствий
        """
        cls.waving_hand = cls.__create_hand_emoji("Waving%20Hand.png", "Waving Hand")
        
        cls.night = cls.__create_time_emoji("Night%20with%20Stars.png", "Night")
        cls.morning = cls.__create_time_emoji("Sunset.png", "Morning")
        cls.evening = cls.__create_time_emoji("Cityscape%20at%20Dusk.png", "Evening")
        cls.afternoon = cls.__create_time_emoji("Cityscape.png", "Afternoon")
        
        cls.greetings = {i: f"{cls.morning} Доброе утро" for i in range(4, 12)}
        cls.greetings.update({i: f"{cls.afternoon} Добрый день" for i in range(12, 18)})
        cls.greetings.update({i: f"{cls.evening} Добрый вечер" for i in range(18, 22)})
        cls.greetings.update({i: f"{cls.night} Доброй ночи" for i in range(22, 24)})
        cls.greetings.update({i: f"{cls.night} Доброй ночи" for i in range(0, 4)})
    
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
        Возвращает приветствие в зависимости от текущего времени суток по Москве
        
        Returns:
            str: приветствие в виде строки
        """
        time_zone = zoneinfo.ZoneInfo("Europe/Moscow")
        return cls.__get_greeting(datetime.datetime.now(time_zone).hour)
import allure
import random
import unittest
import unittest.mock

from src.greeting.greeting import Greeting


@allure.feature("Greeting Tests")
class TestGreeting(unittest.TestCase):
    
    def __test_greeting(self, hours: list, expected_greeting: str) -> None:
        random.shuffle(hours)
        for hour in hours:
            with unittest.mock.patch("datetime.datetime") as mock_datetime:
                mock_datetime.now.return_value.hour = hour
                self.assertEqual(Greeting.greeting(), expected_greeting)
            with allure.step(f"Testing hour: {hour}"):
                pass
            
    @allure.story("Morning test")
    def test_morning_greeting(self) -> None:
        self.__test_greeting(list(range(4, 12)), "Доброе утро")
            
    @allure.story("Afternoon test")
    def test_afternoon_greeting(self) -> None:
        self.__test_greeting(list(range(12, 18)), "Добрый день")
    
    @allure.story("Evening test")
    def test_evening_greeting(self) -> None:
        self.__test_greeting(list(range(18, 22)), "Добрый вечер")
        
    @allure.story("Night test")
    def test_night_greeting(self) -> None:
        self.__test_greeting(list(range(22, 24)) + list(range(0, 4)), "Доброй ночи")
        
        
if __name__ == "__main__":
    unittest.main()
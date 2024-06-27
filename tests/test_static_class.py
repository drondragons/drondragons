import allure
import unittest

from src.static_class.static_class import StaticClass


@allure.feature("StaticClass Tests")
class TestStaticClass(unittest.TestCase):
    
    @allure.story("Instantiate StaticClass")
    def test_instantiate_static_class(self) -> None:
        with self.assertRaises(TypeError):
            StaticClass()
            
            
if __name__ == "__main__":
    unittest.main()
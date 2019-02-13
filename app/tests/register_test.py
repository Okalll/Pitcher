import unittest
from app.models import Register

class RegisterTest(unittest.TestCase):
    register_all=[]
    """
    Test class to test the behaviour of the register class
    """
    def setUp(self):
        """
        Set up method that will run before every Test
        """
        self.new_register=Register("tuitoek","sjtoke@gmail.com","ssjtk123","sjtk123")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_register,Register))

    def save_register(self):
        Register.register_all.append(self)

    @classmethod
    def clear_reviews(cls):
        Review.register_all.clear()

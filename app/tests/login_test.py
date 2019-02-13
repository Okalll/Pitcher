import unittest
from app.models import Login

class LoginTest(unittest.TestCase):
    """
    Test class to test the behaviour of the login class
    """
    def setUp(self):
        """
        Set up method that will run before every Test
        """
        self.new_login=Login("tuitoek","sjtk123")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_login,Login))

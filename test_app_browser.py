import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class FlaskSeleniumTestCase(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()  # You may need to specify the path to your chromedriver executable here
        self.driver.get('http://localhost:5000')  # Assuming your Flask app is running locally on port 5000

    def tearDown(self):
        self.driver.quit()

    def test_index(self):
        assert 'Hello, World!' in self.driver.page_source

    def test_greet(self):
        self.driver.get('http://localhost:5000/greet/John')
        assert 'Hello, John! Welcome to the Exciting Flask App.' in self.driver.page_source

    def test_quote(self):
        self.driver.get('http://localhost:5000/quote')
        assert 'The only way to do great work is to love what you do. - Steve Jobs' in self.driver.page_source

    def test_random_number(self):
        self.driver.get('http://localhost:5000/random')

        assert self.driver.find_element(By.XPATH ,'//div').text.isdigit()



if __name__ == '__main__':
    unittest.main()

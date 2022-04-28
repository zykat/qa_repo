import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

# class TestMePlease(unittest.TestCase):
#     def test_1(self):
#         # Initialisation
#         driver = webdriver.Chrome()
#         driver.set_window_size(1024, 768)
#
#         # test
#         driver.get("https://mail.ru")
#
#         # destroy driver instance
#         driver.close()
#
# if __name__ == "__main__":
#     unittest.main()

class TestMePlease(unittest.TestCase):
    def setUp(self)-> None:
        self.driver = webdriver.Chrome()
        self.driver.set_window_size(1024, 768)

    def test_1(self):
        self.driver.get("https://selenium.dev/about/")
        doc_link = self.driver.find_element(By.CSS_SELECTOR,"a[href='/documentation']").click()
        self.assertEqual(self.driver.title, "The Selenium Browser Automation Project | Selenium")
        self.assertEqual(self.driver.current_url, "https://www.selenium.dev/documentation/")
        time.sleep(3)

    def test_2(self):
        self.driver.maximize_window()
        self.driver.get("https://www.selenium.dev/documentation/")
        self.driver.execute_script("window.scrollTo(3,2500);")
        time.sleep(3)

    @unittest.skip("skip test")
    def test_3(self):
        self.driver.get("https://www.getbooststrap.com")
        self.assertEqual(34, "")

    def tearDown(self)-> None:
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
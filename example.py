import time
from cgi import test
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class ZonaTelecomLoginTest:
    WEBSITE_URL = 'https://www.zonatelecom.ru/'

    def __init__(self) -> None:
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        
    def _open_website(self) -> None:
        self.driver.get(self.WEBSITE_URL)
        self.driver.maximize_window()

    def authorize_by_phone(self, phone: str) -> None:
        self._open_website()
        time.sleep(3)

        self.driver.find_element(by=By.XPATH, value='//*[@id="__next"]/div[2]/div[1]/div/div[2]/div/div/button').click()
        time.sleep(2)
        self.driver.find_element(by=By.XPATH, value='//*[@id="__next"]/div[2]/div[3]/div/div/div/div/a').click()
        time.sleep(2)
        self.driver.find_element(by=By.XPATH, value='/html/body/div[2]/div[2]/div[3]/div/div/div/form/div/div/div').click()
        time.sleep(2)

        for number in [*phone]:
            self.driver.find_element(by=By.XPATH, value='/html/body/div[2]/div[2]/div[3]/div/div/div/form/div/div/div/input').send_keys(number)

        self.driver.find_element(by=By.XPATH, value='/html/body/div[2]/div[2]/div[3]/div/div/div/form/button').click()

        time.sleep(2)
        mouse = self.driver.find_element(by=By.XPATH, value='/html/body/div[2]/div[2]/div[3]/div/div/div/h3')

        if mouse.text == 'Вход или регистрация':
            print('Тест ' + mouse.text + ' - ✅')
        else:
            self.driver.save_screenshot('error_01.png')
            print('Тест ' + self.driver.title + ' - ❌')


tester = ZonaTelecomLoginTest()
tester.authorize_by_phone("79915501002")

time.sleep(5)
import unittest
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import TimeoutException

class MyTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_step_1(self):
        self.driver.get("https://netpeak.ua")
        self.assertEqual("Раскрутка сайта, продвижение сайтов: Netpeak Украина — интернет-маркетинг для бизнеса",  self.driver.title)


    def test_step_2(self):
        self.driver.get("https://netpeak.ua")
        self.driver.find_element_by_link_text("Карьера").click()
        self.assertEqual("Работа в Netpeak: обращение руководителя, видео и презентация о карьере в Нетпик Украина", self.driver.title)


    def test_step_3(self):
        self.driver.get("https://career.netpeak.ua/")
        self.driver.find_element_by_link_text("Я хочу работать в Netpeak").click()
        self.assertEqual("Заполнение анкеты на вакансию — Netpeak Украина", self.driver.title)

    def test_step_4(self):
        driver = self.driver
        driver.get("https://career.netpeak.ua/hiring/")
        file_input = driver.find_element_by_name("up_file")

        path_img = os.path.abspath("img_fox.png")
        file_input.send_keys(path_img)

        elem = driver.find_element_by_id("up_file_name")

        try:
            wait = WebDriverWait(elem, 10).until(EC.text_to_be_present_in_element((By.CLASS_NAME, "control-label"), "Ошибка: неверный формат файла (разрешённые форматы: doc, docx, pdf, txt, odt, rtf)."))

            self.assertTrue(wait)
        except (NoAlertPresentException, TimeoutException) as py_ex:
            print("Test step 4: (TimeoutException, NoAlertPresentException)")

    def test_step_5(self):
        driver = self.driver
        driver.get("https://career.netpeak.ua/hiring/")

        # step 5
        driver.find_element_by_id("inputName").send_keys("Maxim")
        driver.find_element_by_id("inputLastname").send_keys("Shyrokostup")
        driver.find_element_by_id("inputEmail").send_keys("un@gmail.com")

        select_day = Select(driver.find_element_by_name("bd"));
        select_day.select_by_index(2)
        select_month = Select(driver.find_element_by_name("bm"))
        select_month.select_by_index(2)
        select_year = Select(driver.find_element_by_name("by"))
        select_year.select_by_index(23)

        driver.find_element_by_id("inputPhone").send_keys("380970000001")

        # step 6
        driver.find_element_by_id("submit").click();

        # step 7
        fields = driver.find_element_by_xpath("//p[contains(text(), 'Все поля являются обязательными для заполнения')]")
        attribute = fields.value_of_css_property("color")

        self.assertIn( "(255, 0, 0", attribute)

    def test_step_8(self):
        driver = self.driver
        driver.get("https://career.netpeak.ua/hiring/")
        driver.find_element_by_xpath("//div[@class='logo-block']/a[@href]").click()

        self.assertEqual( "Раскрутка сайта, продвижение сайтов: Netpeak Украина — интернет-маркетинг для бизнеса", driver.title)



    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
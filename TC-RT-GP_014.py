# Тест-кейс: TC-RT-GP_014
#
# Описание: Проверить, что при нажатии на ссылку меню "Помощь" открывается окно с полем для запроса. При вводе
# запроса и нажании кнопки "Найти", открывается страница с результатами поиска.
#
# Ссылка на тест-кейс: https://docs.google.com/spreadsheets/d/1PE9EcK4a1cdgjxku7rX65zSYG03LKn5U/edit#gid=494636941

import time

from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_TC_RT_GP_14(selenium):
   selenium.get('https://rostov.rt.ru/')

   time.sleep(10)

   confirm_region_button_xpath = '/html/body/div[2]/div/div/header/div[1]/div[1]/div/div[2]/div[5]/div/div/div[2]/div[3]/button[1]'
   confirm_region_button = selenium.find_element(By.XPATH, confirm_region_button_xpath)
   confirm_region_button.click()

   time.sleep(5)

   cookies_button_xpath = '/html/body/div[2]/div/div/div[1]/div[13]/div/div/div/div/div/div/div[2]/button'
   cookies_button = selenium.find_element('xpath', cookies_button_xpath)
   cookies_button.click()

   time.sleep(5)

   burger_2_button_xpath = '/html/body/div[2]/div/div/header/div[1]/div[1]/div/div[2]/div[3]/div/div/div/div/div/div[1]/a[1]'
   burger_2_button = selenium.find_element('xpath', burger_2_button_xpath)
   burger_2_button.click()

   time.sleep(15)

   input_password_xpath = '/html/body/div[2]/div/div/main/div/div/div/div/div[3]/div[1]/div/section/div/div/div/div[1]/div[1]/div[1]/div/div/input'
   input_password = selenium.find_element(By.XPATH, input_password_xpath)
   input_password.send_keys('Сменить номер телефона')

   time.sleep(5)

   burger_button_xpath = '/html/body/div[2]/div/div/main/div/div/div/div/div[3]/div[1]/div/section/div/div/div/div[1]/div[1]/div[1]/div/button'
   burger_button = selenium.find_element('xpath', burger_button_xpath)
   burger_button.click()

   time.sleep(5)

   h3_search_result_xpath = '//*[@id="block-b2spomoschformapoiskanastranicerezultatovpoiska"]/div/div/div/div/h3'
   h3_search_result = selenium.find_element('xpath', h3_search_result_xpath)
   assert h3_search_result.text == 'Результаты поиска'

   selenium.save_screenshot('screenshots/TC-RT-GP_014.png')

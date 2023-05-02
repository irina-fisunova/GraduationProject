# Тест-кейс: TC-RT-GP_014
#
# Описание: Проверить, что при нажатии на ссылку меню "Помощь" открывается окно с полем для запроса. При вводе
# запроса и нажании кнопки "Найти", открывается страница с результатами поиска.
#
# Ссылка на тест-кейс: https://docs.google.com/spreadsheets/d/1PE9EcK4a1cdgjxku7rX65zSYG03LKn5U/edit#gid=494636941

import time
from selenium.webdriver.common.by import By
from settings import close_confirm_and_cookies
def test_TC_RT_GP_14(selenium):
   selenium.get('https://rostov.rt.ru/')

   close_confirm_and_cookies(selenium)

   help_link_xpath = '/html/body/div[2]/div/div/header/div[1]/div[1]/div/div[2]/div[3]/div/div/div/div/div/div[1]/a[1]'
   help_link = selenium.find_element('xpath', help_link_xpath)
   help_link.click()

   time.sleep(15)

   input_request_xpath = '/html/body/div[2]/div/div/main/div/div/div/div/div[3]/div[1]/div/section/div/div/div/div[1]/div[1]/div[1]/div/div/input'
   input_request = selenium.find_element(By.XPATH, input_request_xpath)
   input_request.send_keys('Сменить номер телефона')

   time.sleep(5)

   search_button_xpath = '/html/body/div[2]/div/div/main/div/div/div/div/div[3]/div[1]/div/section/div/div/div/div[1]/div[1]/div[1]/div/button'
   search_button = selenium.find_element('xpath', search_button_xpath)
   search_button.click()

   time.sleep(5)

   h3_search_result_xpath = '//*[@id="block-b2spomoschformapoiskanastranicerezultatovpoiska"]/div/div/div/div/h3'
   h3_search_result = selenium.find_element('xpath', h3_search_result_xpath)
   assert h3_search_result.text == 'Результаты поиска'

   selenium.save_screenshot('screenshots/TC-RT-GP_014.png')

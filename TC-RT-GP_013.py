# Тест-кейс: TC-RT-GP_013
#
# Описание: Проверить, что при нажатии на кнопку "Нет, изменить" открывается окно со списком регионов
# и полем поиска.
#
# Ссылка на тест-кейс: https://docs.google.com/spreadsheets/d/1PE9EcK4a1cdgjxku7rX65zSYG03LKn5U/edit#gid=822676627

import time
from settings import is_exist
from selenium.webdriver.common.by import By

def test_TC_RT_GP_013(selenium):
   selenium.get('https://rostov.rt.ru/')

   time.sleep(10)

   selenium.save_screenshot('screenshots/TC-RT-GP_013_before.png')

   change_region_button_xpath = '/html/body/div[2]/div/div/header/div[1]/div[1]/div/div[2]/div[5]/div/div/div[2]/div[3]/button[2]'
   change_region_button = selenium.find_element(By.XPATH, change_region_button_xpath)
   change_region_button.click()

   time.sleep(2)

   change_region_xpath = '/html/body/div[2]/div/div/header/div[1]/div[2]/div[2]'
   assert is_exist(selenium, By.XPATH, change_region_xpath) == True

   selenium.save_screenshot('screenshots/TC-RT-GP_013_after.png')


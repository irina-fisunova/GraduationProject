# Тест-кейс: TC-RT-GP_012
#
# Описание: Проверить, что при нажатии на кнопку "Продолжить" в компоненте подтверждения регина,
# окно закрывается.
#
# Ссылка на тест-кейс: https://docs.google.com/spreadsheets/d/1PE9EcK4a1cdgjxku7rX65zSYG03LKn5U/edit#gid=161490945

import time
from settings import is_exist
from selenium.webdriver.common.by import By

def test_TC_RT_GP_012(selenium):
   selenium.get('https://rostov.rt.ru/')

   time.sleep(5)

   selenium.save_screenshot('screenshots/TC-RT-GP_012_before.png')

   confirm_region_button_xpath = '/html/body/div[2]/div/div/header/div[1]/div[1]/div/div[2]/div[5]/div/div/div[2]/div[3]/button[1]'
   confirm_region_button = selenium.find_element(By.XPATH, confirm_region_button_xpath)
   confirm_region_button.click()

   time.sleep(2)

   confirm_region = '/html/body/div[2]/div/div/header/div[1]/div[1]/div/div[2]/div[5]/div'
   assert is_exist(selenium, By.ID, confirm_region) == False

   selenium.save_screenshot('screenshots/TC-RT-GP_012_after.png')






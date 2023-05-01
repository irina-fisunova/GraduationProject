# Тест-кейс: TC-RT-GP_011
#
# Описание:
#
# Ссылка на тест-кейс:

import time

from selenium.common import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_TC_RT_GP_011(selenium):
   selenium.get('https://rostov.rt.ru/')

   time.sleep(15)

   burger_2_button_xpath = '/html/body/div[2]/div/div/footer/div[1]/div[3]/div/div/div/div[1]/div/div/div'
   burger_2_button = selenium.find_element('xpath', burger_2_button_xpath)

   actions = ActionChains(selenium)
   actions.move_to_element(burger_2_button)
   actions.click(burger_2_button).perform()

   time.sleep(15)


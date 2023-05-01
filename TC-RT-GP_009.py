# Тест-кейс: TC-RT-GP_009
#
# Описание: Проверить, что при наведении мышки на пункт главного меню "Пакет услуг" и выборе из выпадающего списка
# элемента "Мобильная связь" происходит переход на страницу "Мобильная связь". При нажатии на логотип осуществляется
# переход на главную страницу сайта.
#
# Ссылка на тест-кейс: https://docs.google.com/spreadsheets/d/1PE9EcK4a1cdgjxku7rX65zSYG03LKn5U/edit#gid=1211459387

import time

from selenium.common import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_TC_RT_GP_009(selenium):
   selenium.get('https://rostov.rt.ru/')

   menu_item_css = 'body > div.dialog-off-canvas-main-canvas > div > div > header > div.header__inner.main-navigation > div.header__p-nav.ntwrap > div > div.region.region-head-menu > div.main-nav.rtk-tabs > div > div:nth-child(1)'
   menu_item = selenium.find_element(By.CSS_SELECTOR, menu_item_css)

   actions = ActionChains(selenium)
   actions.move_to_element(menu_item)
   actions.perform()

   time.sleep(2)

   mobile_link_xpath = '/html/body/div[3]/div/div/header/div[1]/div[3]/div/div[1]/div[2]/div[1]/div/div/div/div[2]/div/div/div[2]/a'
   mobile_link =  selenium.find_element('xpath', mobile_link_xpath)
   mobile_link.click()

   time.sleep(2)

   selenium.save_screenshot('screenshots/TC-RT-GP_009_1.png')

   time.sleep(2)

   logo_xpath = '/html/body/div[2]/div/div/header/div[1]/div[1]/div/div[1]/div[1]/div/a'
   logo = selenium.find_element('xpath', logo_xpath)
   logo.click()

   time.sleep(10)

   selenium.save_screenshot('screenshots/TC-RT-GP_009_2.png')
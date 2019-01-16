import unittest
from time import sleep
from threading import Thread

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


from selenium import webdriver


class MyLoginTestCase(unittest.TestCase):

  #Navigate to Login page

    def setUp(self):
        self.driver = webdriver.Chrome(
            executable_path='/Users/a123/Docs/python_workspace/untitled45/browser_driver/chromedriver')
        self.driver.get('http://local.school.portnov.com:4520/#/login')


        #sleep(300)
        self.driver.implicitly_wait(130)




    def test_login(self):
        # Sign in
        driver = self.driver
        driver.find_element_by_id('mat-input-0').send_keys('umoha@jerapah993r.gq')
        driver.find_element_by_id('mat-input-1').send_keys('12345')

        driver.find_element_by_css_selector('button[type="submit"]').click()

        driver.implicitly_wait(150)
        #sleep(200)
        #element = WebDriverWait(driver, 100).until(
        #    EC.presence_of_element_located((By.XPATH, "//header/div/h3"))
        #)

        welcome_text = driver.find_element_by_xpath('//header/div/h3').text
        driver.implicitly_wait(60)
        self.assertEqual('Anna Ivanova', welcome_text)
        if welcome_text == 'Anna Ivanova':
            print('User has been logged in!')
        driver.implicitly_wait(60)
        #Teacher

        driver.find_element_by_xpath('//a[3]/div/div[2]/h5').click()
        driver.implicitly_wait(60)
        driver.find_element_by_xpath('//mat-card/div/a/button').click()
        driver.implicitly_wait(60)
        driver.find_element_by_xpath('(//div/div[2]/div)[1]').click()
       # driver.find_element_by_xpath('(//span[text()="A005"]/..)[10]').click()
        driver.find_element_by_xpath('(//span[text()="005"]/..)[3]').click()
        driver.find_element_by_xpath('//mat-list-option[1]/div/mat-pseudo-checkbox').click()
        driver.find_element_by_xpath('(//div/div[2]/div)[2]').click()
        driver.implicitly_wait(60)
        driver.find_element_by_xpath("//span[normalize-space()='SQL Auto Quiz']").click()
        driver.find_element_by_xpath('//mat-card/form/div[4]/button').click()
        driver.find_element_by_xpath('//mat-list-item/div/div[2]/h5').click()
        driver.find_element_by_xpath('//div[2]/button[2]').click()

        #Login as student

        driver.find_element_by_xpath('(//input)[1]').send_keys('paym@email2an.ga')
        driver.find_element_by_xpath('(//input)[2]').send_keys('12345')
        driver.find_element_by_css_selector('button[type="submit"]').click()
        driver.find_element_by_xpath('//mat-list/a[2]/div/div[2]/h5').click()
        driver.find_element_by_xpath('(//span[text()="Go To Assessment"])[1]').click()
        driver.find_element_by_xpath('//*[@id="mat-checkbox-1"]/label/div').click()
        driver.find_element_by_xpath('//form/div[2]/button').click()
        driver.find_element_by_xpath('(//div[2]/button)[2]').click()
        driver.find_element_by_xpath('//mat-list/a[3]/div/div[2]/h5').click()

        result = driver.find_element_by_xpath('//table/tbody/tr[6]/td[@class="result"]/span').text
        expected_result = 'FAILED'
        self.assertEqual(expected_result, result)


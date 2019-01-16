import unittest
from selenium.webdriver.common.keys import Keys

from selenium import webdriver


class MyLoginTestCase(unittest.TestCase):

  #Navigate to Login page

    def setUp(self):
        self.driver = webdriver.Chrome(
            executable_path='/Users/a123/Docs/python_workspace/untitled45/browser_driver/chromedriver')
        self.driver.get('http://local.school.portnov.com:4520/#/login')




    def test_login(self):

        #Sign in
        driver = self.driver
        driver.find_element_by_id('mat-input-0').send_keys('umoha@jerapah993r.gq')
        driver.find_element_by_id('mat-input-1').send_keys('12345')
        driver.find_element_by_css_selector('button[type="submit"]').click()

        driver.implicitly_wait(100)




        welcome_text = driver.find_element_by_xpath('//header/div/h3').text
        self.assertEqual('Anna Ivanova', welcome_text)
        if welcome_text == 'Anna Ivanova':
            print('User has been logged in!')

            #Select "Quizzes"

        driver.find_element_by_xpath('//a[4]/div/div[2]/h5').click()
        quiz_list = driver.find_element_by_xpath('//mat-card/h4').text
        self.assertEqual('List of Quizzes', quiz_list)

        #Push "Create New Quiz" button

        driver.find_element_by_xpath('//mat-card/div[2]/a/button/span').click()
        quiz_form = driver.find_element_by_xpath('//*[@id="mat-input-2"]').text
        self.assertEqual('', quiz_form)


        #Input "Title Of The Quiz"

        driver.find_element_by_xpath('//*[@id="mat-input-2"]').send_keys('SQA/3Text 3Single 3Multiple ShowStopper')
        driver.find_element_by_xpath('//form/div/button/span/mat-icon').click()
        driver.find_element_by_css_selector('div.mat-radio-label-content').click()
        driver.find_element_by_css_selector('div>textarea.mat-input-element').send_keys('1.1')
        #Show stopper
        driver.find_element_by_xpath('//*[@id="mat-checkbox-1"]/label/div').click()


        driver.find_element_by_xpath('//form/div/button/span/mat-icon').click()
        driver.find_element_by_xpath('(//mat-radio-button/label/div)[8]').click()
        driver.find_element_by_xpath('(//textarea)[2]').send_keys('1.2')


        driver.find_element_by_xpath('//form/div/button/span/mat-icon').click()
        driver.find_element_by_xpath('(//mat-radio-button/label/div)[14]').click()
        driver.find_element_by_xpath('(//textarea)[3]').send_keys('1.3')
       #
        driver.find_element_by_xpath('//form/div/button/span/mat-icon').click()
        driver.find_element_by_xpath('(//mat-radio-button/label/div)[22]').click()
        driver.find_element_by_xpath('(//textarea)[4]').send_keys('2.1')
        driver.find_element_by_xpath('(//textarea)[5]').send_keys('01')
        driver.find_element_by_xpath('(//textarea)[6]').send_keys('02')
        driver.find_element_by_xpath('(//mat-radio-button/label/div)[25]').click()

        driver.find_element_by_xpath('//form/div/button/span/mat-icon').click()
        driver.find_element_by_xpath('(//mat-radio-button/label/div)[32]').click()

        driver.find_element_by_xpath('(//textarea)[7]').send_keys('2.2')
        driver.find_element_by_xpath('(//textarea)[8]').send_keys('01')
        driver.find_element_by_xpath('(//textarea)[9]').send_keys('02')

        driver.find_element_by_xpath('(//mat-radio-button/label/div)[35]').click()


        #######
        driver.find_element_by_xpath('//form/div/button/span/mat-icon').click()
        driver.find_element_by_xpath('(//mat-radio-button/label/div)[42]').click()

        driver.find_element_by_xpath('(//textarea)[10]').send_keys('2.3')
        driver.find_element_by_xpath('(//textarea)[11]').send_keys('01')
        driver.find_element_by_xpath('(//textarea)[12]').send_keys('02')

        driver.find_element_by_xpath('(//mat-radio-button/label/div)[45]').click()

        ########

        driver.find_element_by_xpath('//form/div/button/span/mat-icon').click()
        driver.find_element_by_xpath('(//mat-radio-button/label/div)[54]').click()

        driver.find_element_by_xpath('(//textarea)[13]').send_keys('3.1')
        driver.find_element_by_xpath('(//textarea)[14]').send_keys('01')
        driver.find_element_by_xpath('(//textarea)[15]').send_keys('02')

        driver.find_element_by_xpath('//*[@id="mat-checkbox-11"]/label/div').click()

        ########

        driver.find_element_by_xpath('//form/div/button/span/mat-icon').click()
        driver.find_element_by_xpath('(//mat-radio-button/label/div)[60]').click()

        driver.find_element_by_xpath('(//textarea)[16]').send_keys('3.2')
        driver.find_element_by_xpath('(//textarea)[17]').send_keys('01')
        driver.find_element_by_xpath('(//textarea)[18]').send_keys('02')

        driver.find_element_by_xpath('//*[@id="mat-checkbox-14"]/label/div').click()


        ##########
        driver.find_element_by_xpath('//form/div/button/span/mat-icon').click()
        driver.find_element_by_xpath('(//mat-radio-button/label/div)[66]').click()

        driver.find_element_by_xpath('(//textarea)[19]').send_keys('3.2')
        driver.find_element_by_xpath('(//textarea)[20]').send_keys('01')
        driver.find_element_by_xpath('(//textarea)[21]').send_keys('02')

        driver.find_element_by_xpath('//*[@id="mat-checkbox-17"]/label/div').click()

        ####
        driver.find_element_by_xpath("//div[@class='form-controls']/div/button[2]").click()









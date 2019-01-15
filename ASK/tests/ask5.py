import unittest
from selenium import webdriver



class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(
            executable_path='/Users/a123/ask_automation/ASK/browsers/chromedriver')
        self.driver.get('http://local.school.portnov.com:4520/#/registration')

    # def test_ask6(self):

    ##Last name - Alphanumerical & Sp char (Happy path)


    #     driver = self.driver
    #     driver.find_element_by_id("mat-input-0").send_keys('Ivan')
    #     driver.find_element_by_id('mat-input-1').send_keys('iV@#7')
    #     driver.find_element_by_id('mat-input-2').send_keys('ivanobv@gmail.com')
    #     driver.find_element_by_id('mat-input-3').send_keys('A007')
    #     driver.find_element_by_id('mat-input-4').send_keys('12345')
    #     driver.find_element_by_id('mat-input-5').send_keys('12345')
    #     driver.find_element_by_css_selector('button[type="submit"]').click()
    #     registrated = driver.find_element_by_xpath('//mat-card/h4').text
    #
    #
    #
    #     self.assertEqual('Registration', registrated)
    #
    #



    # def test_ask14(self):

    ## Last Name - Single char

    #     driver = self.driver
    #     driver.find_element_by_id("mat-input-0").send_keys('Ivan')
    #     driver.find_element_by_id('mat-input-1').send_keys('I')
    #     driver.find_element_by_id('mat-input-2').send_keys('ivanobv@gmail.com')
    #     driver.find_element_by_id('mat-input-3').send_keys('A007')
    #     driver.find_element_by_id('mat-input-4').send_keys('12345')
    #     driver.find_element_by_id('mat-input-5').send_keys('12345')
    #     driver.find_element_by_css_selector('button[type="submit"]').click()
    #     registrated = driver.find_element_by_xpath('//mat-card/h4').text
    #
    #
    #     self.assertEqual('Registration', registrated)




    # def test_ask7(self):

    ##	Last Name - Zero character input / Required field
    #     driver = self.driver
    #     driver.find_element_by_id("mat-input-0").send_keys('Ivan')
    #     driver.find_element_by_id('mat-input-1').send_keys('')
    #     driver.find_element_by_id('mat-input-2').send_keys('ivanobv@gmail.com')
    #     driver.find_element_by_id('mat-input-3').send_keys('A007')
    #     driver.find_element_by_id('mat-input-4').send_keys('12345')
    #     driver.find_element_by_id('mat-input-5').send_keys('12345')
    #     driver.find_element_by_css_selector('button[type="submit"]').click()
    #     error = driver.find_element_by_xpath('//mat-error[@class="mat-error ng-star-inserted"]').text
    #
    #
    #     self.assertEqual('This field is required', error)




    # def test_ask17(self):

    ##Last Name - Max Character
    #     driver = self.driver
    #
    #     driver.find_element_by_id("mat-input-0").send_keys('I')
    #     driver.find_element_by_id('mat-input-1').send_keys('ghaghghghjaggjhjgjgjghahaghghghjaggjhjgjgjghaghghghjaggjhjgjgjghaghghghjaggjhjgjgjkkkhaghghghjaggjhjgjgjghaghghghjaggjhjgjgjghaghghghjaggdfhjsjhjgjgjkkkhaghghghjaggjhjgjgjghaghghghjaggjhjgjgjghaghghghjaggjhjgjgjkkkghghghjaggjhjgjgjghaghghghjaggjhjgjgjkkk')
    #     driver.find_element_by_id('mat-input-2').send_keys('ivanobv@gmail.com')
    #     driver.find_element_by_id('mat-input-3').send_keys('A007')
    #     driver.find_element_by_id('mat-input-4').send_keys('12345')
    #     driver.find_element_by_id('mat-input-5').send_keys('12345')
    #     driver.find_element_by_css_selector('button[type="submit"]').click()
    #     registrated = driver.find_element_by_xpath('//mat-card/h4').text
    #
    #
    #     self.assertEqual('Registration', registrated)



    # def test_ask18(self):

    ##	Last Name - Max character +1
    #     driver = self.driver
    #
    #
    #     driver.find_element_by_id("mat-input-0").send_keys(
    #         'I')
    #     driver.find_element_by_id('mat-input-1').send_keys('ghaghghghjaggjhjgjgjghahaghghghjaggjhjgjgjghaghghghjaggjhjgjgjghaghmghghjaggjhjgjgjkkkhaghghghjaggjhjgjgjghaghghghjaggjhjgjgjghaghghghjaggdfhjsjhjgjgjkkkhaghghghjaggjhjgjgjghaghghghjaggjhjgjgjghaghghghjaggjhjgjgjkkkghghghjaggjhjgjgjghaghghghjaggjhjgjgjkkk')
    #     driver.find_element_by_css_selector('input[placeholder="Email"]').send_keys('ivanobv@gmail.com')
    #     driver.find_element_by_id('mat-input-3').send_keys('A007')
    #     driver.find_element_by_id('mat-input-4').send_keys('12345')
    #     driver.find_element_by_id('mat-input-5').send_keys('12345')
    #     driver.find_element_by_css_selector('button[type="submit"]').click()
    #     driver.implicitly_wait(2)
    #
    #     #error = driver.find_element_by_css_selector('.mat-snack-bar-container.ng-tns-c13-16.ng-trigger.ng-trigger-state.error.mat-snack-bar-center.ng-star-inserted').text
    #
    #     error = driver.find_element_by_css_selector('snack-bar-container>simple-snack-bar').text
    #
    #     self.assertEqual("Data too long for column 'name' at row 1\nX", error)
    #


    # def test_ask8(self):
    # # Last name - Leading space
    #
    #  driver = self.driver
    #  driver.find_element_by_id("mat-input-0").send_keys('Ivan')
    #  driver.find_element_by_id('mat-input-1').send_keys(' Ivanov')
    #
    #  error = driver.find_element_by_xpath('//div/mat-error').text
    #  self.assertEqual('Whitespaces are not allowed', error)
    #

    # def test_ask21(self):
    # #Last name - trailing space
    #
    #  driver = self.driver
    #  driver.find_element_by_id("mat-input-0").send_keys('Ivan ')
    #  driver.find_element_by_id('mat-input-1').send_keys('Ivanov ')
    #
    #  error = driver.find_element_by_xpath('//div/mat-error').text
    #  self.assertEqual('Whitespaces are not allowed', error)

    # def test_ask21(self):
    # #Last name - space inside
    #
    #  driver = self.driver
    #  driver.find_element_by_id("mat-input-0").send_keys('Iv an')
    #  driver.find_element_by_id('mat-input-1').send_keys('Ivanov')
    #
    #  error = driver.find_element_by_xpath('//div/mat-error').text
    #  self.assertEqual('Whitespaces are not allowed', error)
    #











if __name__ == '__main__':
    unittest.main()

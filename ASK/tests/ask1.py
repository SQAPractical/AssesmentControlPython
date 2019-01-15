import unittest
from selenium import webdriver

#Create User with 5 Alphanumerical & Special characters First name

class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(
            executable_path='/Users/a123/ask_automation/ASK/browsers/chromedriver')
        self.driver.get('http://local.school.portnov.com:4520/#/registration')

    # def test_ask2(self):

    ##First name - Alphanumerical & Special char (Happy path)
    #     driver = self.driver
    #     driver.find_element_by_id("mat-input-0").send_keys('iV@#7')
    #     driver.find_element_by_id('mat-input-1').send_keys('Ivanov')
    #     driver.find_element_by_id('mat-input-2').send_keys('ivanobv@gmail.com')
    #     driver.find_element_by_id('mat-input-3').send_keys('A007')
    #     driver.find_element_by_id('mat-input-4').send_keys('12345')
    #     driver.find_element_by_id('mat-input-5').send_keys('12345')
    #     driver.find_element_by_css_selector('button[type="submit"]').click()
    #     registrated = driver.find_element_by_xpath('//mat-card/h4').text
    #     #print(registrated)
    #
    #
    #     self.assertEqual('Registration', registrated)
    #
    #
    # def test_ask13(self):

    ##First Name - Single char
    #     driver = self.driver
    #     driver.find_element_by_id("mat-input-0").send_keys('I')
    #     driver.find_element_by_id('mat-input-1').send_keys('Ivanov')
    #     driver.find_element_by_id('mat-input-2').send_keys('ivanobv@gmail.com')
    #     driver.find_element_by_id('mat-input-3').send_keys('A007')
    #     driver.find_element_by_id('mat-input-4').send_keys('12345')
    #     driver.find_element_by_id('mat-input-5').send_keys('12345')
    #     driver.find_element_by_css_selector('button[type="submit"]').click()
    #     registrated = driver.find_element_by_xpath('//mat-card/h4').text
    #     # print(registrated)
    #
    #     self.assertEqual('Registration', registrated)

    # def test_ask3(self):

    ##	First Name - Zero character input / Required field
    #     driver = self.driver
    #     driver.find_element_by_id("mat-input-0").send_keys('')
    #     driver.find_element_by_id('mat-input-1').send_keys('Ivanov')
    #     driver.find_element_by_id('mat-input-2').send_keys('ivanobv@gmail.com')
    #     driver.find_element_by_id('mat-input-3').send_keys('A007')
    #     driver.find_element_by_id('mat-input-4').send_keys('12345')
    #     driver.find_element_by_id('mat-input-5').send_keys('12345')
    #     driver.find_element_by_css_selector('button[type="submit"]').click()
    #     error = driver.find_element_by_xpath('//mat-error[@class="mat-error ng-star-inserted"]').text
    #
    #
    #     self.assertEqual('This field is required', error)


    # def test_ask15(self):

    ##First Name - Max Character
    #     driver = self.driver
    #
    #     driver.find_element_by_id("mat-input-0").send_keys('ghaghghghjaggjhjgjgjghahaghghghjaggjhjgjgjghaghghghjaggjhjgjgjghaghghghjaggjhjgjgjkkkhaghghghjaggjhjgjgjghaghghghjaggjhjgjgjghaghghghjaggdfhjsjhjgjgjkkkhaghghghjaggjhjgjgjghaghghghjaggjhjgjgjghaghghghjaggjhjgjgjkkkghghghjaggjhjgjgjghaghghghjaggjhjgjgjkkk')
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

    # def test_ask16(self):

    ##	First Name - Max character +1
    #     driver = self.driver
    #
    #
    #     driver.find_element_by_id("mat-input-0").send_keys(
    #         'ghaghghghjaggjhjgjgjghahaghghghjaggjhjgjgjghaghghghjaggjhjgjgjghaghmghghjaggjhjgjgjkkkhaghghghjaggjhjgjgjghaghghghjaggjhjgjgjghaghghghjaggdfhjsjhjgjgjkkkhaghghghjaggjhjgjgjghaghghghjaggjhjgjgjghaghghghjaggjhjgjgjkkkghghghjaggjhjgjgjghaghghghjaggjhjgjgjkkk')
    #     driver.find_element_by_id('mat-input-1').send_keys('I')
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



    # def test_ask4(self):


    # #First Name - Leading space
    #  driver = self.driver
    #  driver.find_element_by_id("mat-input-0").send_keys(' Ivan')
    #  driver.find_element_by_id('mat-input-1').send_keys('Ivanov')
    #
    #  error = driver.find_element_by_xpath('//div/mat-error').text
    #  self.assertEqual('Whitespaces are not allowed', error)
    #

    # def test_ask19(self):



    ##First Name - Leading space
    #  driver = self.driver
    #  driver.find_element_by_id("mat-input-0").send_keys('Ivan ')
    #  driver.find_element_by_id('mat-input-1').send_keys('Ivanov')
    #
    #  error = driver.find_element_by_xpath('//div/mat-error').text
    #  self.assertEqual('Whitespaces are not allowed', error)

    # def test_ask20(self):

    #
    # #First Name - Space characters inside
    #  driver = self.driver
    #  driver.find_element_by_id("mat-input-0").send_keys('Iv an')
    #  driver.find_element_by_id('mat-input-1').send_keys('Ivanov')
    #
    #  error = driver.find_element_by_xpath('//div/mat-error').text
    #  self.assertEqual('Whitespaces are not allowed', error)
    #











if __name__ == '__main__':
    unittest.main()

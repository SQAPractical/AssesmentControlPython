import unittest
from selenium.webdriver.common.keys import Keys

from selenium import webdriver


class MyLoginTestCase(unittest.TestCase):



    def setUp(self):
        self.driver = webdriver.Chrome(
            executable_path='/Users/a123/Docs/python_workspace/untitled45/browser_driver/chromedriver')
        self.driver.get('http://local.school.portnov.com:4520/#/login')




    def test_valid_login(self):
        driver = self.driver
        driver.find_element_by_id('mat-input-0').send_keys('daria.brestle@gmail.com')
        driver.find_element_by_id('mat-input-1').send_keys('qweaz321')
        driver.find_element_by_css_selector('button[type="submit"]').click()

        driver.implicitly_wait(20)

        welcome_text = driver.find_element_by_xpath('//div[2]/h3').text
        self.assertEqual('DashKA Brestle', welcome_text)
        if welcome_text == 'DashKA Brestle':
            print('User has been logged in!')




    def test_invalid_password(self):
        driver = self.driver
        driver.find_element_by_id('mat-input-0').send_keys('daria.brestle@gmail.com')
        driver.find_element_by_id('mat-input-1').send_keys('qweaz321000')
        driver.find_element_by_css_selector('button[type="submit"]').click()


        driver.implicitly_wait(2)
        error_text = driver.find_element_by_css_selector('.mat-simple-snackbar.ng-tns-c14-5.ng-trigger.ng-trigger-contentFade.ng-star-inserted').text
        #error_text = driver.find_element_by_xpath('/html/body/div[1]').text
        #error_text = driver.find_element_by_css_selector('div.cdk-visually-hidden[aria-atomic="true"]').text


        self.assertEqual('Authentication failed. User not found or password does not match\nX', error_text)
        if error_text == 'Authentication failed. User not found or password does not match\nX':
            print('Authentication failed. User not found or password does not match!')

    def test_invalid_email(self):
        driver = self.driver
        driver.find_element_by_id('mat-input-0').send_keys('darya.brestle@gmail.com')
        driver.find_element_by_id('mat-input-1').send_keys('qweaz321')
        driver.find_element_by_css_selector('button[type="submit"]').click()


        driver.implicitly_wait(2)
        error_text = driver.find_element_by_css_selector('.mat-simple-snackbar.ng-tns-c14-5.ng-trigger.ng-trigger-contentFade.ng-star-inserted').text
        #error_text = driver.find_element_by_xpath('/html/body/div[1]').text
        #error_text = driver.find_element_by_css_selector('div.cdk-visually-hidden[aria-atomic="true"]').text


        self.assertEqual('Authentication failed. User not found or password does not match\nX', error_text)
        if error_text == 'Authentication failed. User not found or password does not match\nX':
            print('Authentication failed. User not found or password does not match!')






    def test_empty_password_loging(self):
        driver = self.driver
        driver.find_element_by_id('mat-input-0').send_keys('daria.brestle@gmail.com')
        driver.find_element_by_css_selector('button[type="submit"]').click()

        driver.implicitly_wait(2)
        error_text = driver.find_element_by_css_selector(
            '.mat-error.ng-star-inserted').text
        # error_text = driver.find_element_by_xpath('/html/body/div[1]').text
        # error_text = driver.find_element_by_css_selector('div.cdk-visually-hidden[aria-atomic="true"]').text

        self.assertEqual('This field is required', error_text)
        if error_text == 'This field is required':
            print('Password field is required!')



    def test_password_in_bullet(self):
        driver = self.driver
        driver.find_element_by_id('mat-input-1').send_keys('qweaz321000')
        type = driver.find_element_by_id('mat-input-1').get_property('type')
        self.assertEqual('password', type)
        if type == 'password':
            print('Password is shown in bullets.')




    def test_copy_is_disabled(self):
        driver = self.driver
        driver.find_element_by_id('mat-input-1').send_keys('qweaz321000')
        driver.find_element_by_id('mat-input-1').send_keys(Keys.CONTROL, 'a')
        value = driver.find_element_by_id('mat-input-1').send_keys(Keys.CONTROL, 'c')
        self.assertEqual(None, value)
        if value == None:
            print(value)




    def test_cut_is_disabled(self):
        driver = self.driver
        driver.find_element_by_id('mat-input-1').send_keys('qweaz321000')
        driver.find_element_by_id('mat-input-1').send_keys(Keys.CONTROL, 'a')
        value = driver.find_element_by_id('mat-input-1').send_keys(Keys.CONTROL, 'x')
        self.assertEqual(None, value)
        if value == None:
            print(value)


    def tearDown(self):
        driver = self.driver
        driver.quit()

if __name__ == '__main__':
    unittest.main()

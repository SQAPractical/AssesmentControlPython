import unittest
from selenium import webdriver

#Create User with 5 Alphanumerical & Special characters First name

class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(
            executable_path='/Users/a123/ask_automation/ASK/browsers/chromedriver')
        self.driver.get('http://local.school.portnov.com:4520/#/registration')

    def test_ask860(self):

    #Email - ANCII letters (Happy Path)
        driver = self.driver
        driver.find_element_by_id("mat-input-0").send_keys('Firstname')
        driver.find_element_by_id('mat-input-1').send_keys('Lastname')
        driver.find_element_by_id('mat-input-2').send_keys('Firstname.Lastname@domain.name')
        driver.find_element_by_id('mat-input-3').send_keys('A01')
        driver.find_element_by_id('mat-input-4').send_keys('12345')
        driver.find_element_by_id('mat-input-5').send_keys('12345')
        driver.find_element_by_css_selector('button[type="submit"]').click()
        registrated = driver.find_element_by_xpath('//mat-card/h4').text



        self.assertEqual('Registration', registrated)


    def test_ask861(self):
        # Email - All Upper case
        driver = self.driver
        driver.find_element_by_id("mat-input-0").send_keys('Firstname')
        driver.find_element_by_id('mat-input-1').send_keys('Lastname')
        driver.find_element_by_id('mat-input-2').send_keys('FIRSTNAME.LASTNAME@DOMAIN.NAME')
        driver.find_element_by_id('mat-input-3').send_keys('A01')
        driver.find_element_by_id('mat-input-4').send_keys('12345')
        driver.find_element_by_id('mat-input-5').send_keys('12345')
        driver.find_element_by_css_selector('button[type="submit"]').click()
        registrated = driver.find_element_by_xpath('//mat-card/h4').text

        self.assertEqual('Registration', registrated)

    def test_ask862(self):
        # Email -  ASCII printable characters  `~$!#%^&*_-+={}|'?/ in local-part
        driver = self.driver
        driver.find_element_by_id("mat-input-0").send_keys('Firstname')
        driver.find_element_by_id('mat-input-1').send_keys('Lastname')
        driver.find_element_by_id('mat-input-2').send_keys("$!#%^&*_-+={}|'?/@domain.name")
        driver.find_element_by_id('mat-input-3').send_keys('A01')
        driver.find_element_by_id('mat-input-4').send_keys('12345')
        driver.find_element_by_id('mat-input-5').send_keys('12345')
        driver.find_element_by_css_selector('button[type="submit"]').click()
        registrated = driver.find_element_by_xpath('//mat-card/h4').text

        self.assertEqual('Registration', registrated)

    def test_ask863(self):
        # Email - numbers in local-part
        driver = self.driver
        driver.find_element_by_id("mat-input-0").send_keys('Firstname')
        driver.find_element_by_id('mat-input-1').send_keys('Lastname')
        driver.find_element_by_id('mat-input-2').send_keys("1234567890@domain.name")
        driver.find_element_by_id('mat-input-3').send_keys('A01')
        driver.find_element_by_id('mat-input-4').send_keys('12345')
        driver.find_element_by_id('mat-input-5').send_keys('12345')
        driver.find_element_by_css_selector('button[type="submit"]').click()
        registrated = driver.find_element_by_xpath('//mat-card/h4').text

        self.assertEqual('Registration', registrated)


    def test_ask864(self):
        # Email - numbers in domain name
        driver = self.driver
        driver.find_element_by_id("mat-input-0").send_keys('Firstname')
        driver.find_element_by_id('mat-input-1').send_keys('Lastname')
        driver.find_element_by_id('mat-input-2').send_keys("Firsname.Lastname@domain1234567890.name")
        driver.find_element_by_id('mat-input-3').send_keys('A01')
        driver.find_element_by_id('mat-input-4').send_keys('12345')
        driver.find_element_by_id('mat-input-5').send_keys('12345')
        driver.find_element_by_css_selector('button[type="submit"]').click()
        registrated = driver.find_element_by_xpath('//mat-card/h4').text

        self.assertEqual('Registration', registrated)




    def test_ask879(self):
        # Email - 64 characters in local-part with 63 characters in first part of domain name and 63 characters in last part of domain name
        driver = self.driver
        driver.find_element_by_id("mat-input-0").send_keys('Firstname')
        driver.find_element_by_id('mat-input-1').send_keys('Lastname')
        driver.find_element_by_id('mat-input-2').send_keys("1234567890123456789012345678901234567890123456789012345678901234@domain123456789012345678901234567890123456789012345678901234567.nameeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee")
        driver.find_element_by_id('mat-input-3').send_keys('A01')
        driver.find_element_by_id('mat-input-4').send_keys('12345')
        driver.find_element_by_id('mat-input-5').send_keys('12345')
        driver.find_element_by_css_selector('button[type="submit"]').click()
        registrated = driver.find_element_by_xpath('//mat-card/h4').text

        self.assertEqual('Registration', registrated)




    def test_ask878(self):
        # Email - 64 characters in last part of domain name
        driver = self.driver
        driver.find_element_by_id("mat-input-0").send_keys('Firstname')
        driver.find_element_by_id('mat-input-1').send_keys('Lastname')
        driver.find_element_by_id('mat-input-2').send_keys("Firstname.Lastname@domain.nameeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee")
        driver.find_element_by_id('mat-input-3').send_keys('A01')
        driver.find_element_by_id('mat-input-4').send_keys('12345')
        driver.find_element_by_id('mat-input-5').send_keys('12345')
        error = driver.find_element_by_xpath('//div/mat-error').text


        self.assertEqual('Should be a valid email address', error)


    def test_ask876(self):
        # Email - 65 characters in local-part
        driver = self.driver
        driver.find_element_by_id("mat-input-0").send_keys('Firstname')
        driver.find_element_by_id('mat-input-1').send_keys('Lastname')
        driver.find_element_by_id('mat-input-2').send_keys("12345678901234567890123456789012345678901234567890123456789012345@domain.name")
        driver.find_element_by_id('mat-input-3').send_keys('A01')
        driver.find_element_by_id('mat-input-4').send_keys('12345')
        driver.find_element_by_id('mat-input-5').send_keys('12345')
        error = driver.find_element_by_xpath('//div/mat-error').text


        self.assertEqual('Should be a valid email address', error)




    def test_ask877(self):
        # Email - 64 characters in first part of domain name
        driver = self.driver
        driver.find_element_by_id("mat-input-0").send_keys('Firstname')
        driver.find_element_by_id('mat-input-1').send_keys('Lastname')
        driver.find_element_by_id('mat-input-2').send_keys("Firstname.Lastname@domain1234567890123456789012345678901234567890123456789012345678.name")
        driver.find_element_by_id('mat-input-3').send_keys('A01')
        driver.find_element_by_id('mat-input-4').send_keys('12345')
        driver.find_element_by_id('mat-input-5').send_keys('12345')
        error = driver.find_element_by_xpath('//div/mat-error').text


        self.assertEqual('Should be a valid email address', error)

    def test_ask868(self):
    # Email - Cyrillic letters in local-part
     driver = self.driver
     driver.find_element_by_id("mat-input-0").send_keys('Firstname')
     driver.find_element_by_id('mat-input-1').send_keys('Lastname')
     driver.find_element_by_id('mat-input-2').send_keys("Firstname.Lastnamе@domain.name")
     driver.find_element_by_id('mat-input-3').send_keys('A01')
     driver.find_element_by_id('mat-input-4').send_keys('12345')
     driver.find_element_by_id('mat-input-5').send_keys('12345')
     error = driver.find_element_by_xpath('//div/mat-error').text

     self.assertEqual('Should be a valid email address', error)




    def test_ask869(self):
    # Email -  ASCII printable characters  <@,">[()] in local-part
        driver = self.driver
        driver.find_element_by_id("mat-input-0").send_keys('Firstname')
        driver.find_element_by_id('mat-input-1').send_keys('Lastname')
        driver.find_element_by_id('mat-input-2').send_keys('''<@,">[()]@domain.name
Group name = A01''')
        driver.find_element_by_id('mat-input-3').send_keys('A01')
        driver.find_element_by_id('mat-input-4').send_keys('12345')
        driver.find_element_by_id('mat-input-5').send_keys('12345')
        error = driver.find_element_by_xpath('//div/mat-error').text

        self.assertEqual('Should be a valid email address', error)

    def test_ask870(self):
        # Email -  ASCII printable characters  $!#%^&*_-+={}|'?/ in domain name
        driver = self.driver
        driver.find_element_by_id("mat-input-0").send_keys('Firstname')
        driver.find_element_by_id('mat-input-1').send_keys('Lastname')
        driver.find_element_by_id('mat-input-2').send_keys("Firstname.Lastname@do$!#%^&*_-+={}|'?/ main.name")
        driver.find_element_by_id('mat-input-3').send_keys('A01')
        driver.find_element_by_id('mat-input-4').send_keys('12345')
        driver.find_element_by_id('mat-input-5').send_keys('12345')
        error = driver.find_element_by_xpath('//div/mat-error').text

        self.assertEqual('Should be a valid email address', error)

    def test_ask871(self):
        # Email - space character in local-part
        driver = self.driver
        driver.find_element_by_id("mat-input-0").send_keys('Firstname')
        driver.find_element_by_id('mat-input-1').send_keys('Lastname')
        driver.find_element_by_id('mat-input-2').send_keys("""Firstname Lastname@domain.name
Group name = A01""")
        driver.find_element_by_id('mat-input-3').send_keys('A01')
        driver.find_element_by_id('mat-input-4').send_keys('12345')
        driver.find_element_by_id('mat-input-5').send_keys('12345')
        error = driver.find_element_by_xpath('//div/mat-error').text

        self.assertEqual('Should be a valid email address', error)

    def test_ask872(self):
        # Email - space character in domain name
        driver = self.driver
        driver.find_element_by_id("mat-input-0").send_keys('Firstname')
        driver.find_element_by_id('mat-input-1').send_keys('Lastname')
        driver.find_element_by_id('mat-input-2').send_keys("""Firstname.Lastname@do main.name""")
        driver.find_element_by_id('mat-input-3').send_keys('A01')
        driver.find_element_by_id('mat-input-4').send_keys('12345')
        driver.find_element_by_id('mat-input-5').send_keys('12345')
        error = driver.find_element_by_xpath('//div/mat-error').text

        self.assertEqual('Should be a valid email address', error)
    def test_ask874(self):
        # Email - two @@ characters in row
        driver = self.driver
        driver.find_element_by_id("mat-input-0").send_keys('Firstname')
        driver.find_element_by_id('mat-input-1').send_keys('Lastname')
        driver.find_element_by_id('mat-input-2').send_keys("""FirstnameLastname@@domain.name""")
        driver.find_element_by_id('mat-input-3').send_keys('A01')
        driver.find_element_by_id('mat-input-4').send_keys('12345')
        driver.find_element_by_id('mat-input-5').send_keys('12345')
        error = driver.find_element_by_xpath('//div/mat-error').text

        self.assertEqual('Should be a valid email address', error)

    def test_ask875(self):
        # Email - without @ character
        driver = self.driver
        driver.find_element_by_id("mat-input-0").send_keys('Firstname')
        driver.find_element_by_id('mat-input-1').send_keys('Lastname')
        driver.find_element_by_id('mat-input-2').send_keys("""Firstname.Lastname.domain.name""")
        driver.find_element_by_id('mat-input-3').send_keys('A01')
        driver.find_element_by_id('mat-input-4').send_keys('12345')
        driver.find_element_by_id('mat-input-5').send_keys('12345')
        error = driver.find_element_by_xpath('//div/mat-error').text

        self.assertEqual('Should be a valid email address', error)
if __name__ == '__main__':
    unittest.main()

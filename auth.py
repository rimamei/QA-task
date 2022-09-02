import unittest
import time
from selenium import webdriver 
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class TestLogin(unittest.TestCase): 

    def setUp(self): 
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
        
    def test_a_success_login(self): 
        browser = self.browser
        browser.get("http://barru.pythonanywhere.com/daftar")
        time.sleep(3)
        browser.find_element(By.XPATH,"/html/body/div/div[2]/form/input[1]").send_keys("test.qa@yopmail.com")
        time.sleep(1)
        browser.find_element(By.CSS_SELECTOR,"input#password").send_keys("qa12345")
        time.sleep(1)
        browser.find_element(By.ID,"signin_login").click()
        time.sleep(2)

        response_data = browser.find_element(By.ID,"swal2-title").text
        response_message = browser.find_element(By.ID,"swal2-content").text

        self.assertIn('Welcome Test', response_data)
        self.assertEqual(response_message, 'Anda Berhasil Login')

    def test_b_failed_with_empty_password(self): 
        browser = self.browser
        browser.get("http://barru.pythonanywhere.com/daftar")
        time.sleep(3)
        browser.find_element(By.XPATH,"/html/body/div/div[2]/form/input[1]").send_keys("test.qa@yopmail.com")
        time.sleep(1)
        browser.find_element(By.CSS_SELECTOR,"input#password").send_keys("")
        time.sleep(1)
        browser.find_element(By.ID,"signin_login").click()
        time.sleep(2)

        response_data = browser.find_element(By.ID,"swal2-title").text
        response_message = browser.find_element(By.ID,"swal2-content").text

        self.assertIn('not found', response_data)
        self.assertEqual(response_message, 'Email atau Password Anda Salah')

    def test_c_failed_with_empty_email_and_password(self): 
        browser = self.browser
        browser.get("http://barru.pythonanywhere.com/daftar")
        time.sleep(3)
        browser.find_element(By.XPATH,"/html/body/div/div[2]/form/input[1]").send_keys("")
        time.sleep(1)
        browser.find_element(By.CSS_SELECTOR,"input#password").send_keys("")
        time.sleep(1)
        browser.find_element(By.ID,"signin_login").click()
        time.sleep(2)

        response_data = browser.find_element(By.ID,"swal2-title").text
        response_message = browser.find_element(By.ID,"swal2-content").text

        self.assertIn('Oops...', response_data)
        self.assertEqual(response_message, 'Gagal Login!')

    def test_d_failed_with_wrong_email_and_password(self): 
        browser = self.browser
        browser.get("http://barru.pythonanywhere.com/daftar")
        time.sleep(3)
        browser.find_element(By.XPATH,"/html/body/div/div[2]/form/input[1]").send_keys("test.qa1@yopmail.com")
        time.sleep(1)
        browser.find_element(By.CSS_SELECTOR,"input#password").send_keys("098765")
        time.sleep(1)
        browser.find_element(By.ID,"signin_login").click()
        time.sleep(2)

        response_data = browser.find_element(By.ID,"swal2-title").text
        response_message = browser.find_element(By.ID,"swal2-content").text

        self.assertIn("User's not found", response_data)
        self.assertEqual(response_message, 'Email atau Password Anda Salah')

    def test_e_failed_with_empty_email_and_wrong_password(self): 
        browser = self.browser
        browser.get("http://barru.pythonanywhere.com/daftar")
        time.sleep(3)
        browser.find_element(By.XPATH,"/html/body/div/div[2]/form/input[1]").send_keys("")
        time.sleep(1)
        browser.find_element(By.CSS_SELECTOR,"input#password").send_keys("098765")
        time.sleep(1)
        browser.find_element(By.ID,"signin_login").click()
        time.sleep(2)

        response_data = browser.find_element(By.ID,"swal2-title").text
        response_message = browser.find_element(By.ID,"swal2-content").text

        self.assertIn('Oops...', response_data)
        self.assertEqual(response_message, 'Gagal Login!')
    
    def test_f_register(self): 
        browser = self.browser
        browser.get("http://barru.pythonanywhere.com/daftar")
        time.sleep(3)
        browser.find_element(By.ID,"signUp").click()
        time.sleep(1)
        browser.find_element(By.ID,"name_register").send_keys("name test")
        time.sleep(1)
        browser.find_element(By.ID,"email_register").send_keys("test.qa2@yopmail.com") # use an email hasn't register yet
        time.sleep(1)
        browser.find_element(By.ID,"password_register").send_keys("12345")
        time.sleep(2)
        browser.find_element(By.ID,"signup_register").click()
        time.sleep(2)

        response_data = browser.find_element(By.ID,"swal2-title").text
        response_message = browser.find_element(By.ID,"swal2-content").text

        self.assertIn('berhasil', response_data)
        self.assertEqual(response_message, 'created user!')
    
    def test_f_register_failed_with_used_email(self): 
        browser = self.browser
        browser.get("http://barru.pythonanywhere.com/daftar")
        time.sleep(3)
        browser.find_element(By.ID,"signUp").click()
        time.sleep(1)
        browser.find_element(By.ID,"name_register").send_keys("name test")
        time.sleep(1)
        browser.find_element(By.ID,"email_register").send_keys("test.qa@yopmail.com")
        time.sleep(1)
        browser.find_element(By.ID,"password_register").send_keys("12345")
        time.sleep(2)
        browser.find_element(By.ID,"signup_register").click()
        time.sleep(2)

        response_data = browser.find_element(By.ID,"swal2-title").text
        response_message = browser.find_element(By.ID,"swal2-content").text

        self.assertIn('Oops...', response_data)
        self.assertEqual(response_message, 'Gagal Register!')

    def tearDown(self): 
        self.browser.close() 

if __name__ == "__main__": 
    unittest.main()
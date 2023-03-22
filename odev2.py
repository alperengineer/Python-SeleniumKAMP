from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


class Test_Sauce:  
    
    def kullaniciAdiYok(self):
       chromeDriver=webdriver.Chrome()
       chromeDriver.get("https://saucedemo.com")
       loginButton=chromeDriver.find_element(By.XPATH,"//*[@id='login-button']")
       loginButton.click()
       sleep(3)
       errorName=chromeDriver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/div[1]/div/div/form/div[3]/h3")
       sleep(3)
       resultlogin=errorName.text=="Epic sadface: Username is required"
       print(resultlogin)

    def sifreYok(self):
        chromeDriver=webdriver.Chrome()
        chromeDriver.get("https://saucedemo.com")
        inputName=chromeDriver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/div[1]/div/div/form/div[1]/input")
        inputName.send_keys("Alperen Oğuz")
        sleep(3)
        loginButton=chromeDriver.find_element(By.XPATH,"//*[@id='login-button']")
        loginButton.click()
        errorPassword=chromeDriver.find_element(By.XPATH,"/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3")
        resultPassword=errorPassword.text=="Epic sadface: Password is required"
        print(resultPassword)
    
    def userLocked(self):
        chromeDriver=webdriver.Chrome()
        chromeDriver.get("https://saucedemo.com")
        inputName=chromeDriver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/div[1]/div/div/form/div[1]/input")
        inputPassword=chromeDriver.find_element(By.ID,"password")
        loginButton=chromeDriver.find_element(By.XPATH,"//*[@id='login-button']")
        inputName.send_keys("locked_out_user")
        inputPassword.send_keys("secret_sauce")
        loginButton.click()
        errorLocked=chromeDriver.find_element(By.XPATH,"/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3")
        print(errorLocked.text=="Epic sadface: Sorry, this user has been locked out.")
    
    def x(self):
        chromeDriver=webdriver.Chrome()
        chromeDriver.get("https://saucedemo.com")
        loginButton=chromeDriver.find_element(By.XPATH,"//*[@id='login-button']")
        loginButton.click()
        sleep(3)
        x=chromeDriver.find_element(By.XPATH,"/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3/button")
        x.click()
   
    def basariliGiris(self):
        chromeDriver=webdriver.Chrome()
        chromeDriver.get("https://saucedemo.com")
        inputName=chromeDriver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/div[1]/div/div/form/div[1]/input")
        inputPassword=chromeDriver.find_element(By.ID,"password")
        loginButton=chromeDriver.find_element(By.XPATH,"//*[@id='login-button']")
        inputName.send_keys("standard_user")
        inputPassword.send_keys("secret_sauce")
        loginButton.click()
    
    def urun(self):
        chromeDriver=webdriver.Chrome()
        chromeDriver.get("https://saucedemo.com")
        inputName=chromeDriver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/div[1]/div/div/form/div[1]/input")
        inputPassword=chromeDriver.find_element(By.ID,"password")
        loginButton=chromeDriver.find_element(By.XPATH,"//*[@id='login-button']")
        inputName.send_keys("standard_user")
        inputPassword.send_keys("secret_sauce")
        loginButton.click()
        sleep(3)
        urun=chromeDriver.find_elements(By.CLASS_NAME,"inventory_item")
        sleep(3)
        print(f"Sitede {len(urun)} tane ürün bulunmaktadır.")




testSauce=Test_Sauce()
testSauce.kullaniciAdiYok()
testSauce.sifreYok()
testSauce.userLocked()
testSauce.x()
testSauce.basariliGiris()
testSauce.urun()

while True:
    continue
from re import U
from turtle import right
import pyautogui
import selenium
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#C:\Program Files (x86)\chromedriver.exe
driver = webdriver.Chrome('C:\Program Files (x86)\ChromeDriver Selenium\chromedriver.exe')
driver.get('https://www.getepic.com/sign-in')
time.sleep(10)
Button = driver.find_element_by_xpath('//button[@routerlink="/sign-in/parent"]')
Button.click()
time.sleep(5)
Loginbuttonemail = driver.find_element_by_id('email')
Loginbuttonemail.click()
time.sleep(2)
Loginbuttonemail.send_keys('ablopablofernandez@gmail.com')
time.sleep(2)
Loginbuttonepass = driver.find_element_by_id('password')
Loginbuttonepass.click()
time.sleep(3)
Loginbuttonepass.send_keys('flipflip12345')
time.sleep(2)
Loginbuttonemail.send_keys(u'\ue007')
time.sleep(3)
profileselect = driver.find_element_by_xpath('/html/body/app-root/epic-web-app/div/div/epic-profile-select/div/div/div/epic-profile-selector-with-buddy/div/div[2]/div/avatar-icon/div')
profileselect.click()
time.sleep(3)
driver.get('https://www.getepic.com/app/read/73360')
time.sleep(2)
pagenext = driver.find_element_by_xpath('//html/body')
def nextpage():
    pyautogui.press("right")


for i in range(22):
    nextpage()
    time.sleep(60)

    



time.sleep(10)




driver.quit()
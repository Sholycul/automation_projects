from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC




class InternetSpeedTwitterBot():
    def __init__(self):
        self.get_up_speed = 0
        self.get_down_speed = 0
        self.path = r"C:\Users\FIDO\PycharmProjects\chromedriver-win32\chromedriver-win32\chromedriver.exe"
        self.driver = webdriver.Chrome(service=Service(executable_path=self.path))


    def get_internet_speed(self):
        self.driver.get("https://fast.com/")
        sleep(30)

        show_more_info = self.driver.find_element(By.ID, "show-more-details-link")
        show_more_info.click()

        down = self.driver.find_element(By.ID, "down-mb-value").text
        up = self.driver.find_element(By.ID, "up-mb-value").text
        self.get_down_speed = float(down)
        self.get_up_speed = float(up)

        
    def tweet_at_provider(self):
        self.driver.get("https://twitter.com/home")
        sleep(10)
        email_input = self.driver.find_element(By.XPATH, "//*[@id='layers']/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input")
        email_input.send_keys("09059538784")
        sleep(1)
        email_input.send_keys(Keys.ENTER)
        sleep(5)
        try:
            # pass_input = self.driver.find_element(By.XPATH, "//*[@id=\"react-root\"]/div/div/div/main/div/div/div/div[2]/div[2]/div[1]/div/div/div/div[2]/div/label/div/div[2]/div[1]/input")
            pass_input = self.driver.find_element(By.NAME, "password")
            pass_input.send_keys("?2fdHxgY6Ppau_u")
            pass_input.send_keys(Keys.ENTER)
        except NoSuchElementException:
            username = self.driver.find_element(By.XPATH, "//*[@id='layers']/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input")
            username.send_keys("sholy_cul")  #Your Username here in case Twitter asks for username before asking password
            username.send_keys(Keys.ENTER)
            sleep(5)
            pass_input = self.driver.find_element(By.XPATH, "//*[@id='layers']/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input")
            pass_input.send_keys("?2fdHxgY6Ppau_u")
            pass_input.send_keys(Keys.ENTER)

        sleep(30)

        input = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div/div/div/div')
        input.click()

        sleep(5)
        # span = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[1]/div[2]/div/div/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div/div/div/div/div/div/span/span')

        tweet = (f"Message by BOT: My Current Internet Speed is {self.get_down_speed}mb Download and {self.get_up_speed}mb Upload \n#networking")
        input.send_keys(tweet)
        sleep(10)
        input.send_keys(Keys.CONTROL + Keys.ENTER)
        sleep(15)

    def open_new_tab(self):
        self.driver.execute_script("window.open('');")

    def retweet(self):
        self.driver.get("https://twitter.com/Sholy_Cul/status/1751030268666810560?s=20")
        sleep(15)
        # email_input = self.driver.find_element(By.XPATH, "//*[@id='layers']/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input")
        # email_input.send_keys("09059538784")
        # sleep(1)
        # email_input.send_keys(Keys.ENTER)
        # sleep(5)
        # try:
        #     # pass_input = self.driver.find_element(By.XPATH, "//*[@id=\"react-root\"]/div/div/div/main/div/div/div/div[2]/div[2]/div[1]/div/div/div/div[2]/div/label/div/div[2]/div[1]/input")
        #     pass_input = self.driver.find_element(By.NAME, "password")
        #     pass_input.send_keys("?2fdHxgY6Ppau_u")
        #     pass_input.send_keys(Keys.ENTER)
        # except NoSuchElementException:
        #     username = self.driver.find_element(By.XPATH, "//*[@id='layers']/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input")
        #     username.send_keys("sholy_cul")  #Your Username here in case Twitter asks for username before asking password
        #     username.send_keys(Keys.ENTER)
        #     sleep(5)
        #     pass_input = self.driver.find_element(By.XPATH, "//*[@id='layers']/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input")
        #     pass_input.send_keys("?2fdHxgY6Ppau_u")
        #     pass_input.send_keys(Keys.ENTER)

        re_tweet = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/section/div/div/div[1]/div/div/article/div/div/div[3]/div[6]/div/div/div[2]/div/div/div[1]/svg")
        re_tweet.click()
        sleep(30)
        login = self.driver.find_element(By.LINK_TEXT, "Log in")
        login.click()

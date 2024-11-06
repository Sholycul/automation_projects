# from dotenv import dotenv_values
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException

# Define the required internet speed thresholds
UP = 20  # Minimum upload speed in Mbps
DOWN = 20  # Minimum download speed in Mbps

# secrets = dotenv_values('.env')
# Load environment variables (you need to set these in your environment)
# TWITTER_EMAIL = secrets['TWITTER_EMAIL']
# TWITTER_PASSWORD = secrets['TWITTER_PASSWORD']
# TWITTER_USERNAME = secrets['TWITTER_USERNAME']

TWITTER_EMAIL = '09059538784'
TWITTER_PASSWORD = '?2fdHxgY6Ppau_u'
TWITTER_USERNAME = 'sholy_cul'

# URLs and browser options
SPEED_TEST = "https://www.speedtest.net/"
TWITTER_URL = "https://twitter.com/"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)


# Define a class for the Internet Speed Twitter Bot
class InternetSpeedTwitterBot():
    def __init__(self, speed_up, speed_down):
        self.up = speed_up
        self.down = speed_down
        self.get_up_speed = 0
        self.get_down_speed = 0

    # Method to get internet speed
    def get_internet_speed(self):
        # Initialize the Selenium web driver
        driver = webdriver.Chrome(options=chrome_options)
        try:
            driver.get(SPEED_TEST)

            # Find and click the speed test button
            initiate_speed_button = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located(
                    (By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a'))
            )
            initiate_speed_button.click()

            # Wait for the speed test to complete (adjust time.sleep as needed)
            time.sleep(50)

            # Get the download and upload speeds
            down_speed = driver.find_element(By.XPATH,
                                             '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div['
                                             '3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text
            up_speed = driver.find_element(By.XPATH,
                                           '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div['
                                           '3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text
            self.get_down_speed = float(down_speed)
            self.get_up_speed = float(up_speed)

            print(f"Down = {self.get_down_speed}/ UP = {self.get_up_speed}")

        except (NoSuchElementException, TimeoutException) as e:
            print(f"Error getting internet speed: {str(e)}")
        finally:
            driver.quit()

    # Method to tweet at the internet service provider
    def tweet_at_provider(self):
        self.get_internet_speed()

        if self.get_up_speed < self.up or self.get_down_speed < self.down:
            driver = webdriver.Chrome(options=chrome_options)
            try:
                driver.get(TWITTER_URL)

                # Find and click the sign-in button
                sign_in_button = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH,
                                                    '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/div['
                                                    '1]/div/div[3]/div[5]/a'))
                )
                sign_in_button.click()

                # Enter email and navigate to the Username input if it appears
                email = WebDriverWait(driver, 20).until(
                    EC.presence_of_element_located((By.XPATH,
                                                    '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div['
                                                    '2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div['
                                                    '2]/div/input'))
                )
                email.send_keys(TWITTER_USERNAME)
                email.send_keys(Keys.ENTER)

                # Enter the password
                password = WebDriverWait(driver, 15).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, 'input[name*=password]'))
                )
                password.send_keys(TWITTER_PASSWORD)
                password.send_keys(Keys.ENTER)

                # Compose the tweet message
                message = f"Hey Internet Provider, why is my internet speed DOWN: {self.get_down_speed} Mbps/" \
                          f"UP: {self.get_up_speed} Mbps, when I pay for DOWN: {self.down} Mbps/UP: {self.up} Mbps?"

                # Find the tweet input box and send the message
                text = WebDriverWait(driver, 20).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, 'div[aria-label="Tweet text"]'))
                )
                text.send_keys(message)

                # Find and click the post button
                post_button = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div'
                                                          '/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/'
                                                          'div[2]/div[2]/div/div/div[2]/div[3]/div/span/span'))
                )
                post_button.click()
                print(f"Tweet Done: {message}")

            except (NoSuchElementException, TimeoutException) as e:
                print(f"Error tweeting at the provider: {str(e)}")

            finally:
                driver.quit()

        if self.get_up_speed >= self.up and self.get_down_speed >= self.down:
            print(f"Download Speed: {self.get_down_speed} Mbps")
            print(f"Upload Speed: {self.get_up_speed} Mbps")


# Create an instance of the bot and call the tweet_at_provider method
bot = InternetSpeedTwitterBot(UP, DOWN)
bot.tweet_at_provider()
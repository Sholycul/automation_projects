from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep
from dotenv import load_dotenv
import os

load_dotenv()


email = os.getenv('email')
password = os.getenv('password')
to_mail1 = os.getenv('to_mail1')
to_mail = os.getenv('to_mail')
USER1 = os.getenv('USER1')
PASSWORD1 = os.getenv('PASSWORD1')
CODEB = os.getenv('CODEB')
URL = os.getenv('URL')
USER = os.getenv('USER')
PASSWORD = os.getenv('PASSWORD')
CODE1 = os.getenv('CODE1')
CODE2 = os.getenv('CODE2')

path = r"C:\Users\FIDO\PycharmProjects\chromedriver-win32\chromedriver-win32\chromedriver.exe"


def book_it():
    sleep(2)
    book = driver.find_element(By.XPATH, '//*[@id="form.actions.426f6f6b206163636f6d6d6f646174696f6e"]')
    book.click()
    sleep(5)
    ac_series = driver.find_element(By.NAME, 'ac_series')
    ac_series.send_keys(CODE1)

    ac_number = driver.find_element(By.NAME, 'ac_number')
    ac_number.send_keys(CODEB)

    sleep(5)

    create_ticket = driver.find_element(By.NAME, 'SUBMIT')
    create_ticket.click()

    update = driver.find_element(By.XPATH, '//*[@id="kofa-body"]/div[2]/div[5]/div/div/div[1]/div/div')
    return update.text


def send_email(message):
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=email, password=password)
        connection.sendmail(from_addr=email, to_addrs=to_mail, msg=f"Subject: Congrats ooo\n\n You got space\n")


driver = webdriver.Chrome(service=Service(executable_path=path))
driver.get(URL)
sleep(2)

user = driver.find_element(By.NAME, 'form.login')
user.send_keys(USER1)
passwd = driver.find_element(By.NAME, 'form.password')
passwd.send_keys(PASSWORD1)

login = driver.find_element(By.NAME, 'SUBMIT')
login.click()

sleep(5)
drop_down = driver.find_element(By.PARTIAL_LINK_TEXT, 'My Data')
drop_down.click()

accomodation_data = driver.find_element(By.LINK_TEXT, 'Accommodation Data')
accomodation_data.click()

uppd = book_it()

update_content = uppd
# gotten_space = False

for i in range(10):
    upd = book_it()
    if update_content == upd:
        print(upd)
    else:
        send_email(upd)
        break
    sleep(5)

driver.quit()
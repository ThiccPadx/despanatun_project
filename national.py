import os
import time
from selenium import webdriver
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
import subprocess
from python_anticaptcha import AnticaptchaClient, ImageToTextTask

api_key = 'ef216bf070e2a8184781f66c90f1f44d'
# captcha_fp = open('examples/captcha_ms.jpeg', 'rb')
# client = AnticaptchaClient(api_key)
# task = ImageToTextTask(captcha_fp)
# job = client.createTask(task)
# job.join()
# print(job.get_captcha_text())


# If it doesn't work, install mpg123
# sudo apt install mpg123


# log file location
logfile = "/home/cgev/Desktop/log.txt"

# webdriver file location
webdriverfile = "/home/cgev/PycharmProjects/despanatun_script/chromedriver"

# Max page load wait time
delay = 10

# Alert audio file
alert = "alert.mp3"


def playAlert():
    os.system("mpg123 " + alert)
def bash(bashCommand):
    output = subprocess.check_output(['bash', '-c', bashCommand])
def say(text):
    bash("spd-say " + text)
def log(text):
    #bash("spd-say " + text)
    bash("echo '" + text + "' >> " + logfile)
    bash("date '+%H:%M:%S' >> " + logfile)


# Uncomment to check if alerting works
#playAlert()

options = Options()
options.add_argument("user-data-dir=selenium")
browser = webdriver.Chrome(webdriverfile, 0, options)
print("Make sure website is reachable and language is selected to English")
input("Press Enter when ready")
browser.set_page_load_timeout(delay)
bash("echo >> " + logfile)
bash("echo Started at: >> " + logfile)
bash("date '+%H:%M:%S' >> " + logfile)
while (1 < 2):
    try:
        # Open Web page
        browser.get('https://secure.e-konsulat.gov.pl/Uslugi/RejestracjaTerminu.aspx?IDUSLUGI=1&IDPlacowki=134')

        if ("Przekroczyłeś dopuszczalną" in browser.page_source):
            log("Too many attempts ")
            say("Too many attempts")
            continue
        # Check if the page did load
        if not ("System Zdalnej Rejestracji" in browser.title):
            log("Website didnt load")
            continue

        # Run anticaptcha
        box = browser.find_element_by_id("cp_Captcha_ctl01_tbAnswer")
        box.send_keys(Keys.LEFT_CONTROL + Keys.LEFT_SHIFT + '6')
        time.sleep(20)

        # Click Continue button
        cont = browser.find_element_by_id('cp_btnDalej')
        cont.click()
        if ("Invalid image verification" in browser.page_source):
            log("Captcha failed")
            continue
        if ("Your application has been cancelled" in browser.page_source):
            log("Caught by website ")
            continue
        if ("Przekroczyłeś dopuszczalną" in browser.page_source):
            log("Too many attempts ")
            say("Too many attempts")
            continue
        try:
            # Get drop-down list
            select = Select(browser.find_element_by_id('cp_cbRodzajUslugi'))
        except NoSuchElementException:
            log("Couldn't load website")
            say("Couldn't load website")
            continue


        # Select from drop down list
        select.select_by_visible_text('National visa - students')

        # Check place availability
        if ("Lack of available dates" in browser.page_source):
            log("Lack of available dates")
        if ("Date of appointment" in browser.page_source):
            playAlert()
            log("Place found!!!")
            # Get drop-down list with dates
            select = Select(browser.find_element_by_id('cp_cbDzien'))
            # Pick first available date
            select.select_by_index(1)
            input("Press Enter to continue")
    except TimeoutException:
        log("Website timeout")
        say("Website timeout")

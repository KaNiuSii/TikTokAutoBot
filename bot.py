import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager as CM

def load_cookies(driver, cookie_file):
    with open(cookie_file, 'r') as cookiesfile:
        cookies = json.load(cookiesfile)
        for cookie in cookies:
            if 'sameSite' not in cookie or cookie['sameSite'] not in ["Strict", "Lax", "None"]:
                cookie['sameSite'] = "None"
            driver.add_cookie(cookie)

def check_exists_by_xpath(driver, xpath):
    try:
        driver.find_element_by_xpath(xpath)
    except NoSuchElementException:
        return False
    return True

def upload(bot, video_path):
    bot.get('https://www.tiktok.com/creator-center/upload')
    wait = WebDriverWait(bot, 100)
    iframe = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "iframe[data-tt='Upload_index_iframe']")))
    bot.switch_to.frame(iframe)


    file_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[type='file']")))
    file_input.send_keys(video_path)
    bot.switch_to.default_content()

    iframe = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "iframe[data-tt='Upload_index_iframe']")))
    bot.switch_to.frame(iframe)
    
    caption = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div/div/div/div[2]/div[2]/div[2]/div[1]/div/div[2]/div/div/div[1]/input')))

    bot.implicitly_wait(5)
    ActionChains(bot).move_to_element(caption).click(
        caption).perform()
    
    for _ in range(3):
        ActionChains(bot).move_to_element(caption).click(caption).perform()
        ActionChains(bot).send_keys(Keys.BACKSPACE).perform()
        

    with open(r"caption.txt", "r") as f:
        tags = [line.strip() for line in f]

    for tag in tags:
        ActionChains(bot).move_to_element(caption).click(
        caption).perform()
        ActionChains(bot).send_keys(tag).perform()
        time.sleep(2)
        ActionChains(bot).send_keys(Keys.RETURN).perform()
        time.sleep(1)

    time.sleep(1)
    bot.execute_script("window.scrollTo(150, 400);")

    post = WebDriverWait(bot, 100).until(
        EC.visibility_of_element_located(
            (By.XPATH, '//*[@id="root"]/div/div/div/div[2]/div[2]/div[2]/div[8]/div[2]/button')))
    bot.execute_script("arguments[0].scrollIntoView();", post)
    post.click()

    bot.switch_to.default_content()
    time.sleep(1)

def run(video_path):
    options = webdriver.ChromeOptions()
    options.add_argument("--disable-blink-features=AutomationControlled") 
    
    options.add_experimental_option("excludeSwitches", ["enable-automation"]) 
    
    options.add_experimental_option("useAutomationExtension", False)
    print()
    print('\033[96m ' + '*** Keep in mind that it sometimes gets bugged due to random errors, if any thing happend, or somethings off, restart it ***' + ' \033[0m')
    while True:
        time.sleep(1)
        service = Service(CM().install())
        bot = webdriver.Chrome(service=service, options=options)
        bot.set_window_size(1680, 900)
        bot.delete_all_cookies()
        bot.get('https://www.tiktok.com/login/phone-or-email/email')
        print('\033[95m ' + '*** login please ***' + ' \033[0m')
        time.sleep(3)
        curr = bot.current_url

        while 'https://www.tiktok.com/login' in curr:
            curr = bot.current_url
            time.sleep(1)
        print('\033[95m ' + '*** loged in, if not in upload go there manually ***' + ' \033[0m')
        bot.refresh()
        time.sleep(2)
        upload(bot, video_path)
        time.sleep(5)
    bot.quit()

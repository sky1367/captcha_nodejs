#天下登入頁面
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
import datetime
from PIL import Image
from newModel import predict


def run_chrome(filename):
    path=r"C:\Users\Student\Desktop\chromedriver.exe"
    driver=webdriver.Chrome(path)
    driver.maximize_window()
    driver.get("https://www.sanmin.com.tw/Member/Login/?ReturnUrl=%2fmember%2findex")

    account = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'Account'))
    )
    account.click()
    account.clear()
    account.send_keys("帳號")

    password = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'pwd'))
    )
    password.click()
    password.clear()
    password.send_keys("密碼")


    # 網頁截圖
    driver.save_screenshot(filename)
    element = driver.find_element(By.ID, 'CaptchaImg')
    location = element.location
    size = element.size
    device_pixel_ratio = int(driver.execute_script('return window.devicePixelRatio'))
    coordinate = refine_coordinate(location, size, device_pixel_ratio)
    time.sleep(2)
    # 裁切得到captcha image
    img = crop_image(FULL_IMG, coordinate)
    img = img.resize((WIDTH, HEIGHT), Image.Resampling.LANCZOS)
    # convert rgba to rgb
    img = img.convert('RGB')
    # captcha的名字用current_time儲存
    current_time = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
    img_name = current_time + '.jpg'
    # 存在./public/img/
    img.save(FOLDER + img_name, "JPEG")
    # 執行model predict，得到預測的captcha內容
    captcha_ans = predict("./public/img/" + img_name)

    # print("captcha_ans: " + captcha_ans)
    captcha = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.NAME, 'HumanPass'))
    )
    captcha.send_keys(captcha_ans)
    # captcha.send_keys(Keys.RETURN)
    # captcha = WebDriverWait(driver, 10).until(
    #     EC.presence_of_element_located((By.ID, 'HumanPass'))
    # )
    # captcha.click()
    # captcha.clear()
    # captcha.send_keys('7458')

    time.sleep(2)
    element_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'btn-blue'))
    )
    element_button.click()
    time.sleep(4)

    driver.quit()
    # <button type="submit" class="fillorange f-left">登入</button>

# 以下皆為裁切使用到的function
# 來自: https://github.com/maxmilian/thsrc_captcha
FULL_IMG = "sanmin.png"
WIDTH = 140
HEIGHT = 48
FOLDER = "./public/img/"

def refine_coordinate(location, size, ratio):
    # Mac Retina 把截圖會把解析度變為 2 倍，需要考慮 ratio
    left = location['x'] * ratio
    right = left + size['width'] * ratio
    top = location['y'] * ratio
    bottom = top + size['height'] * ratio
    return (left, top, right, bottom)

def crop_image(filename, coordinate):
    img = Image.open(filename)
    img = img.crop(coordinate)
    return img


if __name__ == '__main__':
    filename = "sanmin.png"
    run_chrome(filename)
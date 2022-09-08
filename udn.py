import time
import datetime
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from PIL import Image

from newModel import predict


def run_chrome(filename):
    path=r"C:\Users\Student\Desktop\chromedriver.exe"
    driver=webdriver.Chrome(path)

    driver.get("https://udndata.com/ndapp/Index")
    driver.maximize_window()

    element_input = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.NAME, 'pUserID'))
    )
    element_input.send_keys('帳號')
    # time.sleep(5)
    element_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, 'pPassword'))
    )
    element_input.send_keys('密碼')

    # 網頁截圖
    driver.save_screenshot(filename)
    element = driver.find_element(By.CSS_SELECTOR, 'img#img')
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
    element_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, 'pCode'))
    )
    element_input.send_keys(captcha_ans)
    time.sleep(2)

    element_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, 'button'))
    )
    element_button.click()
    time.sleep(4)

    driver.quit()
    return location, size, device_pixel_ratio
    

# 以下皆為裁切使用到的function
# 來自: https://github.com/maxmilian/thsrc_captcha
FULL_IMG = "udn.png"
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
    filename = "udn.png"
    run_chrome(filename)
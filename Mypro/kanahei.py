from selenium import webdriver
from time import sleep
import requests
import datetime
import socket

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
options.add_experimental_option('useAutomationExtension', False)
options.add_experimental_option("prefs", {
                                "profile.password_manager_enabled": False, "credentials_enable_service": False})
options.add_argument('--headless')  # 背景執行

driverPath = "C:\\Users\\ykinf\\chromedriver.exe"
browser = webdriver.Chrome(executable_path=driverPath, options=options)


def lineNotify_message(token, msg):
    headers = {
        "Authorization": "Bearer "+token,
        "Content-Type": "application/x-www-form-urlencoded"
    }
    payload = {'message': msg}
    r = requests.post("https://notify-api.line.me/api/notify",
                      headers=headers, params=payload)

    return r.status_code


def lineNotify_image(token, msg, image_path):
    headers = {
        "Authorization": "Bearer "+token,
        # "Content-Type":"application/x-www-form-urlencoded"
    }
    payload = {'message': msg}
    files = {'imageFile': open(image_path, 'rb')}
    r = requests.post("https://notify-api.line.me/api/notify",
                      headers=headers, params=payload, files=files)

    return r.status_code


requests.adapters.DEFAULT_RETRIES = 5
s = requests.session()
s.keep_alive = False
url = 'https://kanaheis-small-animals.jp/'
browser.get(url)

today = datetime.date.today()
tomonth = today.month
now = today.day
'''
today = '2021-06-15'
tomonth = 6
now = 15
'''

token = 'XFnL0h8DmJ7Veaw00UPm2540HnxUAaEAPSEnAeyawW6'


data = browser.find_elements_by_class_name('content_special_date')
for i in data[0:1]:
    date = i.text.replace('.', '-')

    if tomonth < 10:
        date = date.replace('-', '-0')
        if now >= 10:
            date = date.replace('0' + str(now), str(now))
    else:
        if now < 10:
            date = date.replace('-', '-0').replace('0' +
                                                   str(tomonth), str(tomonth))
    print(date)
    print(today)

    if date == today:
        data1 = browser.find_elements_by_xpath("//li//a[@class='clearfix']")
        for i in data1[0:1]:
            web = i.get_attribute("href")
            print(web)

            strScript = 'window.open("'+web+'");'
            browser.execute_script(strScript)
            # sleep(3)
            windows = browser.window_handles  # get all windows in your browser
            # -1 means the latest page(i.e.the page you just open)
            browser.switch_to.window(windows[-1])
            table = browser.find_element_by_class_name('mainvisual')
            browser.execute_script(
                'var q=document.documentElement.scrollTop='+str(int(table.rect['y'])))
            browser.execute_script(
                'var q=document.documentElement.scrollLeft='+str(int(table.rect['x'])))
        image_path = (r'C:\Users\ykinf\Onedrive\桌面\python課堂作業\cap_kanahei.png')
        message = '【卡娜赫拉】最新動態:'+web
        table.screenshot('./cap_kanahei.png')
        lineNotify_image(token, message, image_path)
        browser.quit()
    else:
        message = '【卡娜赫拉】今天沒有動態'
        lineNotify_message(token, message)
        browser.quit()

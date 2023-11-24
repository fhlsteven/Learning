# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import json
from selenium.webdriver.common.by import By
import time
import urllib.request
import os
from selenium.webdriver.common.keys import Keys

from urllib import parse

DWONLOAD_DATA = []

def get_diver():
    d = DesiredCapabilities.CHROME
    d['goog:loggingPrefs'] = {'performance':'ALL'}

    # ChromeOptions 配置相关
    options = webdriver.ChromeOptions()
    options.add_argument("--mute-audio")
    options.add_argument('--ignore-certificate-errors')
    
    # 不同版本用不同的方法
    # options.add_experimental_option('perfLoggingPrefs', {'enableNetwork': True})
    # driver = webdriver.Chrome(options=options)

    driver = webdriver.Chrome(chrome_options=options, desired_capabilities=d)
    return driver


def main_proc():
    base_url = "http://www.yuetingba.cn/book/detail/3a012d27-cd3c-d1ed-f907-9eeba6531208/1000"
    driver = get_diver()
    driver.get(base_url)

    #logs = driver.get_log("performance")

    btns = driver.find_elements(by=By.CSS_SELECTOR,value='.col-md-3>div')

    if btns:
        time.sleep(5)
        i = 0
        for btn in btns:
            single_proc(btn, driver)
            i = i+1
            if i%4==0:
                driver.execute_script("arguments[0].scrollIntoView();", btn)
                i = 0
    else:
        driver.quit()    

def save_log(all_data):
    with open('./log/log.json',"a+", encoding='utf-8') as f:
        json.dump(all_data, f, indent=4, ensure_ascii=False)

def is_exists(name):
    for d in DWONLOAD_DATA:
        if name in d:
            DWONLOAD_DATA.remove(d)
            return True
    return False

def single_proc(btn, driver):
    name = btn.text    
    if is_exists(name): 
        print('已下载：'+ name)
        return
    else:
        print(name)
    aeles = btn.find_elements(by=By.TAG_NAME,value='a')    
    if len(aeles)>0:
        aeles[2].click()
        time.sleep(20)
    else:
        print('err ' + str(len(aeles)))
        return
    
    proc_log(driver, name)

def proc_log(driver, name):
    for x in driver.get_log('performance'):
        logjson = json.loads(x["message"])["message"]
        if (logjson['method'] == "Network.responseReceived"):
            params = logjson['params']           
            try:
                requestUrl = params['response']['url']
                if 'myfiles/host/listen' in requestUrl and '.mp3' in requestUrl:                    
                    save_log([name, parse.unquote(requestUrl)])
                    download(requestUrl, name)                    
            except Exception as ex:
                print(params)
                print(ex)

def download(url, name):
    name = name + '_' +url.rsplit('/',1)[1]  
    urllib.request.urlretrieve(url=url, filename='./file/{0}'.format(name))
    time.sleep(10)

'''
    logjson = json.loads(log["message"])["message"]
    if logjson['method'] == 'Network.responseReceived':
        params = logjson['params']
        try:
            requestUrl = params['response']['url']
            if "/bdsp/album/pay" in requestUrl:
                requestId = params['requestId']
                response_body = driver.execute_cdp_cmd('Network.getResponseBody', {'requestId': requestId})
                _content = json.loads(response_body["body"])
            else:
                continue
        except:
            requestUrl = "None"
            logger.info("没找到requestUrl：{}".format(requestUrl))
            continue
    else:
        continue
        
_content = "None"
'''

if __name__ == '__main__':
    DWONLOAD_DATA = os.listdir('./file')
    main_proc()
    time.sleep(100)

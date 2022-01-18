from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import chromedriver_autoinstaller
import subprocess
import shutil
import pyperclip

from time import sleep
import datetime
from playsound import playsound
# try:
#     shutil.rmtree(r"c:\chrometemp")  #쿠키 / 캐쉬파일 삭제
# except FileNotFoundError:
#     pass

# subprocess.Popen(r'C:\Program Files\Google\Chrome\Application\chrome.exe --remote-debugging-port=9222 --user-data-dir="C:\chrometemp"') # 디버거 크롬 구동


option = Options()
option.add_experimental_option("debuggerAddress", "127.0.0.1:9222")

chrome_ver = chromedriver_autoinstaller.get_chrome_version().split('.')[0]
try:
    driver  = webdriver.Chrome(executable_path='C:/Users/82104/Downloads/chromedriver_win32/chromedriver.exe', options=option)
except:
    print('뭐가 없나보네..')

driver.implicitly_wait(10)

url = 'https://visithalla.jeju.go.kr/reservation/firstComeStep.do?courseSeq=&visitDt=2022.01.06&cmpaCnt=1'
login_url = 'https://kauth.kakao.com/oauth/authorize?response_type=code&client_id=c33d7a9f924177b1d467aff2ceab7a86&redirect_uri=https%3A%2F%2Fvisithalla.jeju.go.kr%2Fsns%2FkkoInfoProc.do&state=494064760400514241610169482888591557955'
cur_url = 'https://visithalla.jeju.go.kr/reservation/firstComeStep.do?courseSeq=&amp;visitDt=2022.01.06&amp;cmpaCnt=1'

driver.get(cur_url)

while True:

    #select course
    driver.find_element_by_xpath('//option[@value="242"]').click()
    date = driver.find_element_by_id('visitDt')
    date.click()
    #select Date
    driver.find_element_by_xpath('//a[@class="ui-state-default"]').click()
    driver.find_element_by_link_text('8').click()
    sleep(1)
    #select start time
    driver.find_element_by_xpath('//option[@value="TIME3"]').click()
    driver.find_element_by_xpath('//option[@value="TIME1"]').click()
    sleep(2)

    #current rest count
    cur_text = driver.find_element_by_css_selector("#current_num > strong").text

    cur_people = cur_text.split('/')[0][-3:]

    cur_time = datetime.datetime.now()
    print(f'{cur_time} : {cur_people}')
    if 150 < int(cur_people) < 800 :
        try:
            playsound("sound.mp3")
        except:
            print('소리가안나 빨리 예약해야해 !!')



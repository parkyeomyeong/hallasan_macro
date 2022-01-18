from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver  = webdriver.Chrome(executable_path='C:/Users/82104/Downloads/chromedriver_win32/chromedriver.exe')
url = 'https://visithalla.jeju.go.kr/reservation/firstComeStep.do?courseSeq=&visitDt=2022.01.06&cmpaCnt=1'
driver.get(url)

kakao_login_button_xpath = '//a[@class="btn btn-kakao"]'
kakao_login_button = driver.find_element_by_xpath(kakao_login_button_xpath)
kakao_login_button.click()

#login
kakao_email = 'jeho0978@naver.com'
password = 'pym76094380'

# driver.find_element_by_id('id_email_2').send_keys(kakao_email)
# driver.find_element_by_id('id_password_3').send_keys(password)

# #enter press
# driver.find_element_by_id('id_password_3').send_keys(keys.ENTER)


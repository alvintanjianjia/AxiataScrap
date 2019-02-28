from selenium import webdriver

PROXY = '45.225.138.118:53281'

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--proxy-server=%s' % PROXY)

chrome = webdriver.Chrome(chrome_options=chrome_options, executable_path='C:/Users/AC408/chromedriver.exe')









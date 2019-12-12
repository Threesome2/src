from selenium import webdriver
from time import sleep
# import xlrd
import random
import os
import time
import sys
sys.path.append("..")
# import email_imap as imap
# import json
import re
# from urllib import request, parse
from selenium.webdriver.support.ui import Select
# import base64
import Chrome_driver
import email_imap as imap
import name_get
import db
import selenium_funcs
import Submit_handle


'''
GETAROUND
Auto
'''



def web_submit(submit,chrome_driver,debug=0):
    # test
    if debug == 1:
        site = 'https://adpgtrack.com/click/5b73d90a6c42607b3b6c4322/146827/199595/subaccount'
        submit['Site'] = site
    print('222222222222222222222222')
    # sleep(3)
    chrome_driver.get(submit['Site'])
    # sleep(300)    
    print(submit['Site'])
    name = name_get.gen_one_word_digit(lowercase=False)
    chrome_driver.maximize_window()
    chrome_driver.refresh()
    print('Loading finished')
    Excel_name = 'health'    
    # chrome_driver.find_element_by_xpath('//*[@id="site-header"]/div/div/a[1]').click()
    # i = 0
    # while True:
    #     try:
    #         chrome_driver.find_element_by_xpath('//*[@id="list-lead-form"]/div[1]/select')
    #         print('find selecter')
    #         break
    #     except:
    #         i+=1
    #         if i >= 5:
    #             break
    # year
    sleep(5)
    selenium_funcs.scroll_and_find(chrome_driver,'//*[@id="list-lead-form"]/div[1]/select')
    sleep(2)
    num = random.randint(2010,2018) 
    s1 = Select(chrome_driver.find_element_by_xpath('//*[@id="list-lead-form"]/div[1]/select'))
    s1.select_by_value(str(num)) 
    # firstname
    chrome_driver.find_element_by_xpath('//*[@id="list-lead-form"]/div[2]/div[1]/div/input').send_keys(submit[Excel_name]['firstname'])
    # lastname
    chrome_driver.find_element_by_xpath('//*[@id="list-lead-form"]/div[2]/div[2]/div/input').send_keys(submit[Excel_name]['lastname'])
    # email
    chrome_driver.find_element_by_xpath('//*[@id="list-lead-form"]/div[3]/div/input').send_keys(submit[Excel_name]['email'])
    # phone
    chrome_driver.find_element_by_xpath('//*[@id="list-lead-form"]/div[4]/div/input').send_keys((submit[Excel_name]['homephone']).split('.')[0])
    # zip
    submit[Excel_name]['zip'] = Submit_handle.get_zip(submit[Excel_name]['zip'])
    chrome_driver.find_element_by_xpath('//*[@id="postal-code"]').send_keys((submit[Excel_name]['zip']))
    # selector
    num = random.randint(1,15)
    s1 = Select(chrome_driver.find_element_by_xpath('//*[@id="list-lead-form"]/div[7]/div/select'))
    s1.select_by_index(num)     
    # button
    chrome_driver.find_element_by_xpath('//*[@id="list-lead-form"]/button').click()
    sleep(15)
    db.update_plan_status(2,submit['ID'])        
    chrome_driver.close()
    chrome_driver.quit()  
    return 1  




 



if __name__=='__main__':
    submit = db.get_one_info()
    chrome_driver = Chrome_driver.get_chrome()
    print(submit)
    web_submit(submit,chrome_driver)

'''
cpagrip
Get the Best Nutella Package!
http://zh.moneymethods.net/click.php?c=7&key=bbcprqa35ns2a5f44z14k2k3
Uspd
'''

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
import random

'''
10015,123Casino 50 Free Spins (UK),Ukpd
'''



def web_submit(submit,chrome_driver,debug=0):
    # test
    if debug == 1:
        site = 'https://track.amcmpn.com/click?pid=664&offer_id=18151'
        submit['Site'] = site
    chrome_driver.get(submit['Site'])
    chrome_driver.maximize_window()    
    chrome_driver.refresh()    
    # sleep(2000)
    # chrome_driver.find_element_by_xpath('').click()
    # chrome_driver.find_element_by_xpath('').send_keys(submit['Uspd']['state'])

    # firstname
    chrome_driver.find_element_by_xpath('//*[@id="user_add_form"]/div/div/div[2]/input').send_keys(submit['Ukpd']['firstname'])    
    # email    
    chrome_driver.find_element_by_xpath('//*[@id="inputEmail"]').send_keys(submit['Ukpd']['email'])

    # comfirm1
    chrome_driver.find_element_by_xpath('//*[@id="user_add_form"]/div/div/div[13]/div/label/span').click()
    # comfirm2
    chrome_driver.find_element_by_xpath('//*[@id="user_add_form"]/div/div/div[14]/div/label/span').click()
    # claim button
    chrome_driver.find_element_by_xpath('//*[@id="user_add_form"]/div/div/button[2]').click()    
    sleep(10)
    try:
        chrome_driver.find_element_by_xpath('//*[@id="congratspopup"]/div/div/div/div/button').click()
    except:
        pass
    sleep(20)
    chrome_driver.close()
    chrome_driver.quit()
    return  



def test():
    Mission_list = ['10000']
    Excel_name = ['Ukpd','']
    Email_list = ['hotmail.com','outlook.com','yahoo.com','aol.com','gmail.com']
    submit = db.read_one_excel(Mission_list,Excel_name,Email_list)
    print(submit)
    # date_of_birth = Submit_handle.get_auto_birthday(submit['Uspd']['date_of_birth'])
    # print(date_of_birth)
    web_submit(submit,1)
    # print(submit['Uspd'])
    # print(submit['Uspd']['state'])
    # print(submit['Uspd']['city'])
    # print(submit['Uspd']['zip'])
    # print(submit['Uspd']['date_of_birth'])
    # print(submit['Uspd']['ssn'])

 

def test1():
	num_gender = random.randint(0,1)
	print(num_gender)


if __name__=='__main__':
    test()
    print('......')

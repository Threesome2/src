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

def web_submit(submit,chrome_driver,debug=0):
    # test
    if debug == 1:
        site = 'http://resslead.o18.click/c?o=715556&m=1846&a=39977'
        submit['Site'] = site
    chrome_driver.get(submit['Site'])
    chrome_driver.maximize_window()    
    chrome_driver.refresh()
    sleep(5000)


def test():
    # db.email_test()
    # date_of_birth = Submit_handle.get_auto_birthday('')         
    Mission_list = ['10026']
    Excel_name = ['health','']
    Email_list = ['hotmail.com','outlook.com','yahoo.com','aol.com','gmail.com']
    submit = db.read_one_excel(Mission_list,Excel_name,Email_list)
    print(submit)
    submit['Mission_Id'] = '10026'
    chrome_driver = Chrome_driver.get_chrome(submit)
    web_submit(submit,chrome_driver,1)


if __name__=='__main__':
    test()

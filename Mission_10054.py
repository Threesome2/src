'''
Adsmain
Trusted Health Quotes
https://track.amcmpn.com/click?pid=668&offer_id=19917
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





def web_submit(submit,chrome_driver,debug=0):
    # test
    # Excel_10054 = 'Data2000'
    Excel_10054 = 'health'    
    if debug == 1:
        site = 'https://track.amcmpn.com/click?pid=668&offer_id=19917'
        submit['Site'] = site
    try:
        chrome_driver.get(submit['Site'])
    except:
        pass
    chrome_driver.maximize_window() 
    chrome_driver.refresh()
    # click
    sleep(2)
    try:
        chrome_driver.find_element_by_xpath('//*[@id="zip-form"]/div[1]/button').click()
    except:
        print("can't find zip button")
        chrome_driver.close()
        chrome_driver.quit()
        return
    sleep(5)
    # date of birth
    date_of_birth = Submit_handle.get_auto_birthday(submit[Excel_10054]['dateofbirth'])
    for key in date_of_birth[0]:
        chrome_driver.find_element_by_xpath('//*[@id="dob"]').send_keys(key)
    for key in date_of_birth[1]:
        chrome_driver.find_element_by_xpath('//*[@id="dob"]').send_keys(key)
    for key in date_of_birth[2]:
        chrome_driver.find_element_by_xpath('//*[@id="dob"]').send_keys(key)
    # height fit
    num_info = Submit_handle.get_height_info()
    chrome_driver.find_element_by_xpath('//*[@id="height-feet"]').send_keys(str(num_info['Height_FT']))
    # height in
    chrome_driver.find_element_by_xpath('//*[@id="height-inches"]').send_keys(str(num_info['Height_Inch']))
    # weight
    chrome_driver.find_element_by_xpath('//*[@id="weight"]').send_keys(str(num_info['Weight']))
    sleep(3)
    # household Size
    index = random.randint(1,11)
    s1 = Select(chrome_driver.find_element_by_xpath('//*[@id="household-size"]'))
    s1.select_by_index(index)
    sleep(3)
    # gender
    num_gender = random.randint(0,1)
    if num_gender == 0:
        chrome_driver.find_element_by_xpath('//*[@id="section-one"]/div[4]/div/label[1]').click()
    else:
        chrome_driver.find_element_by_xpath('//*[@id="section-one"]/div[4]/div/label[2]').click()
    sleep(3)
    #  A&B
    num_AB = random.randint(0,1)
    if num_AB == 0:
        chrome_driver.find_element_by_xpath('//*[@id="section-one"]/div[5]/label[1]').click()
    else:
        chrome_driver.find_element_by_xpath('//*[@id="section-one"]/div[5]/label[2]').click()
    sleep(2)
    #  health conditions
    chrome_driver.find_element_by_xpath('//*[@id="section-one"]/div[6]/label[2]').click()
    sleep(2)
    # continue
    chrome_driver.find_element_by_xpath('//*[@id="submit"]').click()
    sleep(2)
    # fisrt name
    chrome_driver.find_element_by_xpath('//*[@id="first-name"]').send_keys(submit[Excel_10054]['firstname'])
    # last name
    sleep(2)
    chrome_driver.find_element_by_xpath('//*[@id="last-name"]').send_keys(submit[Excel_10054]['lastname'])
    # address
    sleep(2)
    chrome_driver.find_element_by_xpath('//*[@id="address"]').send_keys(submit[Excel_10054]['address'])
    # zip
    chrome_driver.find_element_by_xpath('//*[@id="zip-code"]').clear()
    zipcode = Submit_handle.get_zip(submit[Excel_10054])
    chrome_driver.find_element_by_xpath('//*[@id="zip-code"]').send_keys(zipcode)
    sleep(2)    
    # city 
    chrome_driver.find_element_by_xpath('//*[@id="city"]').send_keys(submit[Excel_10054]['city'])
    sleep(2)
    # state
    s1 = Select(chrome_driver.find_element_by_xpath('//*[@id="state"]'))
    s1.select_by_value(submit[Excel_10054]['state'])
    sleep(2)
    # phone
    homephone = Submit_handle.get_phone(submit[Excel_10054]['homephone'])
    chrome_driver.find_element_by_xpath('//*[@id="phone-number"]').send_keys(homephone)
    sleep(2)
    # email
    chrome_driver.find_element_by_xpath('//*[@id="email-address"]').send_keys(submit[Excel_10054]['email'])
    sleep(2)
    # click view quotes
    chrome_driver.find_element_by_xpath('//*[@id="submit"]').click()
    sleep(30)
    chrome_driver.close()
    chrome_driver.quit()
    return 1



def test():
    # db.email_test()
    Mission_list = ['10009']
    Excel_name = ['','Email']
    Email_list = ['hotmail.com','outlook.com','yahoo.com','aol.com','gmail.com']
    submit = db.read_one_excel(Mission_list,Excel_name,Email_list)
    db.read_all_info()
    # print(submit)
    # excel_list = []
    # for i in range(400):
    #     submit = db.read_one_excel(Mission_list,Excel_name,Email_list)
    #     # print(submit)
    #     excel_list.append(submit['Email']['Email_Id'])
    # # print(excel_list)
    # print(len(excel_list))
    # print(len(set(excel_list)))

    # date_of_birth = Submit_handle.get_auto_birthday(submit['Uspd']['date_of_birth'])
    # print(date_of_birth)
    # web_submit(submit,1)
    # print(submit['Uspd'])
    # print(submit['Uspd']['state'])
    # print(submit['Uspd']['city'])
    # print(submit['Uspd']['zip'])
    # print(submit['Uspd']['date_of_birth'])
    # print(submit['Uspd']['ssn'])

 

def test1():
    # num_gender = random.randint(0,1)
    # print(num_gender)
    Mission_list = ['10009']
    email_list = ['aol.com','yahoo.com']
    email = db.read_one_selected_email(Mission_list,email_list)
    # db.write_one_info(Mission_list,email,Cookie = '')
    print(email)

if __name__=='__main__':
    # test1()
    # print('......')
    date_of_birth = Submit_handle.get_auto_birthday('null')
    print(date_of_birth)
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
        site = 'https://go.byoffers.net/click?pid=170&offer_id=1268'
        submit['Site'] = site
    # js = 'window.location.href="%s"'(submit['Site'])
    chrome_driver.get(submit['Site'])
    chrome_driver.maximize_window()    
    # chrome_driver.refresh()
    chrome_driver.switch_to_frame('rsIframe')
    chrome_driver.find_element_by_xpath('//*[@id="page1"]/button[3]').click()
    sleep(5000)


def pwd_gen():
    result = []
    length = random.randint(9,15)
    for i in range(0, length):
      if i % 4 == 0:
          result.append(random.choice('1234567890'))
      if i % 4 == 1:
          result.append(random.choice('abcdefghijklmnisabella.wiedemann1997@outlook.deopqrstuvwxyz'))
      if i % 4 == 2:
          result.append(random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
      if i % 4 == 3:
          result.append(random.choice('!$%()+,-.:;>?@[]`{}'))
    random.shuffle(result)
    pwd = "".join(result)
    return pwd    


def test():
    # db.email_test()
    # date_of_birth = Submit_handle.get_auto_birthday('')  
    import luminati
    import de_gen
    Mission_list = ['10000','10001']    
    # ip = '192.168.89.145'
    # port = '24365'
    # luminati.refresh_proxy(ip,port)       
    Alliance = 'Byhand'
    account = '1'
    excel = 'de_basic'  
    excel2 = 'Uspd'  
    Excel_name = [excel,'']
    Email_list = ['hotmail.com','outlook.com','yahoo.com','aol.com','gmail.com']
    for num_test in range(1000):
        submit = db.read_one_excel(Mission_list,Excel_name,Email_list)
        blacklist = [' ','(',')','-']
        for key in blacklist:
            submit[excel]['phone'] = submit[excel]['phone'].replace(key,'') 
        submit[excel]['phone'] = submit[excel]['phone'][:5]+' '+submit[excel]['phone'][5:]    
        # if '@' not in submit[excel]['email']:
        #     continue
        submit[excel]['email'] = Submit_handle.get_email(submit[excel])
        submit[excel]['pwd'] = pwd_gen()   
        key_list1 = ['name','phone','email','dateofbirth']
        key_list2 = ['zipcode','city_byzip','city','street','building']
        key_list3 = ['bank','account','iban','blz','bic']
        key_list4 = ['pwd','id_number','expire']
        # key_list.sort()
        # [print(item,':',submit[excel][item]) for item in submit[excel]]  
        submit['Mission_Id'] = Mission_list[0]
        submit['Alliance'] = Alliance    
        submit['Account'] = account
        submit['ua'] = ''
        submit['ip_record'] = ''
        url = 'https://www.netcologne.de/themes/netcologne/ajax/availability_autocomplete.php?src=plz&plz=%s'%submit[excel]['zipcode']
        if submit['Mission_Id'] != 99:
            break
        res = de_gen.pickup(url)    
        print('test netcologne:',res)
        # break
        if len(res)==2:
            # [print(item,':',submit[excel][item]) for item in key_list]
            # break            
            continue
        else:
            print(len(res))            
            # [print(item,':',submit[excel][item]) for item in key_list]
            break
    print('\n\n')
    print('basic info:')
    [print(item,':',submit[excel][item]) for item in key_list1]
    print('\n\n')

    print('location info:')
    [print(item,':',submit[excel][item]) for item in key_list2]
    print('\n')

    print('bank info:')
    [print(item,':',submit[excel][item]) for item in key_list3]
    print('\n')

    print('idcard info:')
    [print(item,':',submit[excel][item]) for item in key_list4]
    print('\n')

    db.write_one_info(Mission_list,submit)
    # id_ = Submit_handle.get_id_number(submit[excel])
    # print(id_)
    # phone = submit[excel]['homephone']
    # phone = Submit_handle.get_uk_phone1(phone)
    # print(phone)
    # chrome_driver = Chrome_driver.get_chrome(submit)
    # web_submit(submit,chrome_driver,1)


if __name__=='__main__':
    for i in range(1):
        test()

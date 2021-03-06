import db
import random
from xlrd import xldate_as_tuple
import requests
import json
import os
import datetime
import de_gen
import re

# Delay, Config, Mission_conf, Email_list  = Cam4_allin.Config_read()

'''
Already handled:
['']
'''
def password_get(submit=''):
    '''
    随机生成密码，长度9-15位
    a = '0123456789'
    b = '!@#$%^&'
    c = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    d = 'abcdefghijklmnopqrstuvwxyz'    
    '''
    a = '0123456789'
    b = '!@#$%^&'
    c = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    d = 'abcdefghijklmnopqrstuvwxyz'
    num = random.randint(9,15)
    pwd = ''
    for i in range(num):
        num_pwd = random.randint(0,3)
        if i == 5:
            num_pwd = 0
        if i == 7:
            num_pwd = 1            
        if i == 3:
            num_pwd = 2  
        if i == 8:
            num_pwd = 3                         
        if num_pwd == 0:
            pwd += a[random.randint(0,len(a)-1)]
        elif num_pwd == 1:
            pwd += b[random.randint(0,len(b)-1)]
        elif num_pwd == 2:
            pwd += c[random.randint(0,len(c)-1)]
        else :
            pwd += d[random.randint(0,len(d)-1)]                                    
    return pwd

def password_get_Nostale(submit=''):
    '''
    0aA
    '''
    a = '0123456789'
    c = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    d = 'abcdefghijklmnopqrstuvwxyz'
    num = random.randint(8,15)
    pwd = ''
    for i in range(num):
        num_pwd = random.randint(0,3)
        if i == 5:
            num_pwd = 0
        if i == 7:
            num_pwd = 1            
        if i == 3:
            num_pwd = 2  
        if i == 8:
            num_pwd = 3                         
        if num_pwd == 0:
            pwd += a[random.randint(0,len(a)-1)]
        elif num_pwd == 1:
            pwd += a[random.randint(0,len(a)-1)]
        elif num_pwd == 2:
            pwd += c[random.randint(0,len(c)-1)]
        else :
            pwd += d[random.randint(0,len(d)-1)]                                    
    return pwd

def cvv_get(submit=''):
    '''
    cvv
    '''
    print('func name: cvv_get')
    print('submit:',submit)
    cvv = submit['cvv']
    print('cvv get fix..........:',cvv)
    cvv = str(cvv).split('.')[0]
    if len(cvv) == 1:
        cvv = '00'+cvv
    elif len(cvv) == 2:
        cvv = '0' + cvv
    else:
        pass
    print('cvv after fixed')
    return cvv

def get_pwd_real(submit=''):
    '''
    leecode123#!!@#$%^&
    pwd1
    '''
    with open(r'ini\pwd.ini','r') as f:
        lines  = f.readlines()
        pwds = []
        for line in lines:
            if line.strip(' ') == '':
                continue
            pwd = line.strip('\n')
            pwds.append(pwd)
    while True:
        num = random.randint(0,len(pwds)-1)
        pwd = pwds[num]
        if len(pwd)>=8:
            break
    b = '!@#$%^&'
    b_insert = random.randint(0,len(b)-1)
    rate = random.randint(0,2)
    if rate == 1:
        print(rate)
        insert_num = random.randint(1,6)
        pwd = pwd[0:insert_num]+b[b_insert]+pwd[insert_num:]
    return pwd

def get_pwd_real2(submit=''):
    '''
    leecode123
    pwd1
    '''
    with open(r'ini\pwd.ini','r') as f:
        lines  = f.readlines()
        pwds = []
        for line in lines:
            if line.strip(' ') == '':
                continue
            pwd = line.strip('\n')
            pwds.append(pwd)
    while True:
        num = random.randint(0,len(pwds)-1)
        pwd = pwds[num]
        if len(pwd)>=8:
            break
    return pwd

def get_pwd_real3(submit=''):
    '''
    leecode123#!!@#$%^&
    pwd2
    '''
    with open(r'ini\pwd2.ini','r') as f:
        lines  = f.readlines()
        pwds = []
        for line in lines:
            if line.strip(' ') == '':
                continue
            pwd = line.strip('\n')
            pwds.append(pwd)
    while True:
        num = random.randint(0,len(pwds)-1)
        pwd = pwds[num]
        if len(pwd)>=8:
            break
    b = '!@#$%^&'
    b_insert = random.randint(0,len(b)-1)
    rate = random.randint(0,2)
    if rate == 1:
        print(rate)
        insert_num = random.randint(1,6)
        pwd = pwd[0:insert_num]+b[b_insert]+pwd[insert_num:]
    return pwd

def get_pwd_real4(submit=''):
    '''
    leecode123
    pwd2
    '''
    with open(r'ini\pwd2.ini','r') as f:
        lines  = f.readlines()
        pwds = []
        for line in lines:
            if line.strip(' ') == '':
                continue
            pwd = line.strip('\n')
            pwds.append(pwd)
    while True:
        num = random.randint(0,len(pwds)-1)
        pwd = pwds[num]
        if len(pwd)>=8:
            break
    return pwd

def get_name_real(submit=''):
    '''
    直接从真实用户名文件里获取
    '''
    with open(r'ini\names.ini','r') as f:
        lines  = f.readlines()
        names = []
        for line in lines:
            if line.strip(' ') == '':
                continue
            name = line.strip('\n')
            names.append(name)
    num = random.randint(0,len(names)-1)
    name = names[num]
    return name

def Submit_handle(submit):
    try:
        submit['Home_phone'] = str(int(submit['Home_phone'])).replace('-','')
        submit['Zip'] = str(int(submit['Zip']))
        if len(submit['Zip']) == 4:
            submit['Zip'] = '0' + submit['Zip']
        if submit['Height_FT'] == '':
            submit['Height_FT'] = str(random.randint(4,7))
        if submit['Height_Inch'] == '':            
            submit['Height_Inch'] = '0'+str(random.randint(7,9))
        if submit['Weight'] == '':                        
            submit['Weight'] = str(int(random.randint(100,200)))
        type_float = type('1')
        print(type(submit['Date_of_birth']))
        if type(submit['Date_of_birth']) == type_float:
            print('===========')
            try:
                date = xldate_as_tuple(submit['Date_of_birth'],0)
                print(date)
            except Exception as e:
                print(str(e))
                date = [str(random.randint(1960,1980))] 
        else:
            # print(date)
            date = [str(random.randint(1960,1980))] 
        print(date)
        for item in date:
            if len(str(item)) == 2:
                if int(item) >= 50:
                    submit['Year'] = '19' + str(item)    
            if len(str(item)) == 4:
                submit['Year'] = str(item)
        submit['Month'] = str(random.randint(1,12))
        submit['Day'] = str(random.randint(1,25))
        submit['handle'] = True   
    except: 
        submit['handle'] = False          
    return submit

def get_zip(submit):
    '''
    四位数zip前添加0,
    处理zip后面的.0

    '''
    if 'zip' in submit:
        zip_ = submit['zip']
    elif 'katou' in submit:
        zip_ = submit['katou']
    zip_ = zip_.split('.')[0]
    if len(zip_) == 4:
        zip_ = '0' + zip_
    if len(zip_) == 3:
        zip_ = '00' + zip_        
    return zip_ 

def apt_get(submit):
    '''
    apt
    '''
    address = submit['address']
    if ' ' in address:
        apt = address.split(' ')[0]
        if not apt.isdecimal():
            apt = random.randint(30,300)
    else:
        apt = random.randint(30,300)
    return int(apt)

def get_city(submit):
    '''
    Reichshof - Welpe
    '''
    content = de_gen.get_city(submit['zipcode'])
    reg_contents_pattern = r'<tr><td >'+str(submit['zipcode'])+r'</td><td >(.*?)</td><td >(.*?)</td><td >'
    reg_contents= re.findall(reg_contents_pattern,content,re.S)
    print('city in submit:',submit['city'])    
    if len(reg_contents)  == 0:
        if '-' in submit['city']:
            submit['city'] = submit['city'].split('-')[0]
            submit['state'] = submit['state']
    elif len(reg_contents) ==1:
        submit['city'] = reg_contents[0][0]
        submit['state'] = reg_contents[0][1]        
    else:
        flag = 0
        for i in range(1,4):
            for item in reg_contents:
                t = 4-i
                if item[0][0:t] == submit['city'][0:t]:
                    flag = 1
                    submit ['city'] = item[0]
                    submit ['state'] = item[1]
            if flag == 1:
                break
        if flag == 0:
            submit['city'] = reg_contents[0][0]
            submit['state'] = reg_contents[0][1]
    print('city by zip found:',reg_contents)
    print('city after handled:',submit['city'])
    print('state found:',submit['state'])
    return submit['city'],submit['state']

def get_auto_birthday(submit):
    '''
    return MM/DD/Year 
    '''
    if 'date_of_birth' in submit:
        date = submit['date_of_birth']
        if date == None:
            date = ''
    else:
        date = ''
    if '/' in date:
        birthday = date.split('/')
    elif '-' in date:
        birthday = date.split('-')    
    else:
        # 'MM/DD/Year'
        if '.0' in date:
            birthday_ = xldate_as_tuple(float(date),0)
            birthday = [str(birthday_[1]),str(birthday_[2]),str(birthday_[0])]
        else:
            birthday = [str(random.randint(1,12)),str(random.randint(1,25)) ,str(random.randint(1970,2000))]  
    if len(str(birthday[0])) == 1:
        birthday[0] = '0'+str(birthday[0]) 
    else:
        birthday[0] = str(birthday[0])
    if len(str(birthday[1])) == 1:
        birthday[1] = '0'+str(birthday[1]) 
    else:
        birthday[1] = str(birthday[1])
    if len(str(birthday[2])) == 2:
        birthday[2] = '19'+birthday[2]
    if int(birthday[2]) <= 1970:
        birthday[2] = str(random.randint(1970,1990))
    return birthday

def get_employer_info(submit):
    '''
    generate employer
    '''
    employer = ''
    if 'employer' in submit:
        if submit['employer'] != '':
            employer = submit['employer']
    if employer == '':
        employer = db.get_employer()
    return employer

def get_occupation_info(submit):
    '''
    generate occupation
    '''
    occupation = ''
    if 'occupation' in submit:
        if submit['occupation'] != '':
            occupation = submit['occupation']
    if occupation == '':
        occupation = db.get_occupation()
    return occupation

def hire_date(submit):
    '''
    12/11/2019
    '''
    mm = random.randint(1,12)
    day = random.randint(1,25)
    year = random.randint(2013,2018)
    if len(str(mm)) == 1:
        mm = '0'+str(mm)
    else:
        mm = str(mm)  
    dd = mm      
    if len(str(dd)) == 1:
        dd = '0'+str(dd)
    else:
        dd = str(dd)        
    hire_date = mm+'/'+dd+'/'+str(year)
    return hire_date

def get_random_income(submit):
    '''
    income year
    40000-90000
    '''
    income = random.randint(40,90)
    income = income*1000
    return income

def get_year_atresidence(submit):
    '''
    1-7
    '''
    year = random.randint(1,7)
    return year

def get_birthday_mm(submit=''):
    '''
    return mm 04
    '''
    birthday = get_auto_birthday(submit)
    return birthday[0]

def get_birthday_mm_one(submit=''):
    '''
    return mm 4,5,6
    '''
    birthday = get_auto_birthday(submit)
    if len(birthday[0]) == 2:
        if birthday[0][0] == '0':
            birthday[0] = birthday[0][1]
    return birthday[0]


def get_birthday_dd(submit=''):
    '''
    return dd
    '''    
    birthday = get_auto_birthday(submit)
    if birthday[1][0] == '0':
        birthday[1] = birthday[1][1]
    return birthday[1]

def get_birthday_year(submit=''):
    '''
    return year
    '''    
    birthday = get_auto_birthday(submit)
    return birthday[2]

def get_birthday_all(submit=''):
    '''
    mm,dd,year
    05021997
    '''
    birthday = get_auto_birthday(submit)
    birthday = str(birthday[0])+str(birthday[1])+str(birthday[2])
    print('birthday:',birthday)
    return birthday  

def get_birthday_all_2(submit=''):
    '''
    mm/dd/year
    05/02/1997
    '''
    birthday = get_auto_birthday(submit)
    birthday = str(birthday[0])+'/'+str(birthday[1])+'/'+str(birthday[2])
    return birthday  

def get_height_info(submit=''):
    '''
    num_info = [ft,in,weight]
    '''
    num_ft = random.randint(5,7)
    num_in = random.randint(1,9)
    num_weight = random.randint(105,275)
    num_info = {}
    num_info['Height_FT'] = num_ft
    num_info['Height_Inch'] = num_in
    num_info['Weight'] = num_weight
    return num_info

def get_height_ft(submit=''):
    '''
    ft
    '''
    num_info = get_height_info()
    return num_info['Height_FT']

def get_height_inch(submit=''):
    '''
    inch
    '''
    num_info = get_height_info()
    return num_info['Height_Inch']

def get_height_weight(submit=''):
    '''
    weight
    '''
    num_info = get_height_info()
    return num_info['Weight']

def get_city_by_zip(zip_):
    url = 'https://tools.usps.com/tools/app/ziplookup/cityByZip'
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Accept-Language": "zh",
        "Cache-Control": "max-age=0",
        "Connection": "keep-alive",
        "Cookie": "NSC_uppmt-xbt8-mc=ffffffff3b2237bf45525d5f4f58455e445a4a4212d3; _gcl_au=1.1.1688992039.1565917935; mab_usps=81; _ga=GA1.2.1159374976.1565917935; _gid=GA1.2.577685537.1565917935; _ga=GA1.3.1159374976.1565917935; _gid=GA1.3.577685537.1565917935; kampyleUserSession=1565917958000; kampyleUserSessionsCount=1; kampyleSessionPageCounter=1; _dc_gtm_UA-80133954-3=1; _gat_UA-80133954-3=1",
        "dnt": "1",
        "origin":'https://tools.usps.com',
        "referer":"https://tools.usps.com/zip-code-lookup.htm?citybyzipcode",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",
    }

    data = {
    'zip':zip_
    }
    response = requests.post(url=url,data =data,headers =headers,timeout=10)
    # print(response.text)
    # print(type(response.text))
    response_dict = json.loads(response.text)
    # print(response_dict)
    city = response_dict['defaultCity']
    state = response_dict['defaultState']
    return city,state

    # print(requests.get('https://adpgtrack.com/click/5d43f1a4a03594103a75da46/146827/233486/subaccount').text) 

def chansfer_float_into_int(str_float):
    '''
    12354.0-->>12354
    '''
    str_int = (str_float.split('.'))[0]
    return str_int

def get_ssn(submit):
    '''
    ssn
    '''
    ssn = submit['ssn'].replace('-','')
    ssn = chansfer_float_into_int(ssn)
    num = random.randint(0,9)
    if len(ssn) == 8:
        ssn += str(num)
    return ssn

def ssn_last4(submit):
    '''
    last 4 of ssn
    '''
    ssn = get_ssn(submit)
    ssn_ = ssn[-4:]
    return ssn_

def ssn_first_3(submit):
    '''
    first 3 of ssn
    '''
    ssn = get_ssn(submit)
    ssn_ = ssn[0:3]
    return ssn_

def ssn_mid_2(submit):
    '''
    mid 2 of ssn
    '''
    ssn = get_ssn(submit)
    ssn_ = ssn[3:5]
    return ssn_

def get_routing_number(submit=''):
    '''
    verify routing    
    routing_number  999999999
    '''
    keys = ['routing_number','routing_nu']
    routing_number = get_value(keys,submit)
    routing_number = routing_number.replace('.0','') 
    routing_number = chansfer_float_into_int(routing_number)
    if len(routing_number) == 8:
        routing_number = '0' + routing_number
    if len(routing_number) >9:
        routing_number = routing_number[0:9]                
    return routing_number

def get_routing_number_verify(submit=''):
    '''
    routing_number
    '''
    keys = ['routing_number','routing_nu']
    routing_number = get_value(keys,submit)
    routing_number = routing_number.replace('.0','') 
    routing_number = chansfer_float_into_int(routing_number)
    if len(routing_number) == 8:
        routing_number = '0' + routing_number
    if len(routing_number) >9:
        routing_number = routing_number[0:9]        
    s = routing_verify(str(routing_number))
    routing_number_verify = ''
    if s!= 1:
        for i in range(10000):
            num_routing = random.randint(100000000,999999999)
            s = routing_verify(str(num_routing))
            if s == 1:
                routing_number_verify = str(num_routing)
                print('bad routing_number:',routing_number,'---get new one:',routing_number_verify)
                break
    else:
        routing_number_verify = str(routing_number)
        print('good routing number:',routing_number_verify)
    return routing_number_verify    

def routing_verify(s):
    '''
    verify routing
    '''
    s = str(s)
    if len(s) == 8:
        s = '0' + s
    if len(s) >9:
        s = s[0:9]     
    if len(s) <8:
        return 0
    n = 0
    for i in range(9):
        # print(i,(int(s[i])+10),(int(s[i+1])+10),(int(s[i+2])+10))
        n+=(int(s[i])+10)*3+(int(s[i+1])+10)*7+(int(s[i+2])+10)
        i+=3
        if i+3 >9:
            break
    # print(n)
    if n!= 0 and n%10==0:
        print('good routing:',s)
        return 1
    else:
        # print('bad routing')
        return 0


def get_account_number(submit=''):
    '''
    account_number
    '''
    keys = ['account_number','account_nu']
    account_number = get_value(keys,submit)
    account_number = account_number.replace('.0','')     
    account_number = chansfer_float_into_int(account_number)
    return account_number

def get_income(submit):
    '''
    20000-70000
    20000,30000...
    '''
    num = random.randint(2,7)
    num = num*10000
    return str(num)

def get_income_other(submit):
    '''
    0-3000
    '''
    num = random.randint(0,3000)
    return str(num)

def get_drivers_license(submit):
    '''
    drivers_license
    '''
    keys = ['drivers_license','drivers_li']
    drivers_license = get_value(keys,submit)
    drivers_license = drivers_license.replace('.0','')     
    drivers_license = chansfer_float_into_int(drivers_license)
    return drivers_license

def transfer_zipcode_into_city():
    with open('testzip.txt') as f:
        lines = f.readlines()
        for line in lines:
            zipcode = line.strip('\n')
            try:
                city,state = get_city_by_zip(zipcode)
                print(city)
            except:
                print('')

def get_fullname(submit):
    '''
    firstname+' '+lastname
    '''
    keys = ['firstname','first_name']
    firstname = get_value(keys,submit)
    keys = ['lastname','last_name']
    lastname = get_value(keys,submit)
    name = firstname + ' ' +lastname
    return name

def get_value(keys,submit):
    value = None
    for key in keys:
        if key in submit:
            if submit[key] != None:
                value = submit[key]
    return value


def get_courses(submit):
    '''
    generate a random course
    '''
    courses = ['GRAPHIC DESIGN','DIGITAL MARKETING','PHOTOGRAPHY','SPORTS AND EXERCISE NUTRITION','FINANCIAL TRADING AND INVESTMENT','NUTRITION','PHOTOSHOP','SOCIAL MEDIA MARKETING','CRYPTOCURRENCY','LEADERSHIP & MANAGEMENT','MOBILE APP DEVELOPMENT','ADOBE LIGHTROOM','FITNESS & WEIGHT LOSS','ENGLISH FOR BEGINNERS','VIRAL MARKETING','WEB DEVELOPMENT','WEB DESIGN','GUITAR','PERSONAL BEAUTY']
    num = random.randint(0,len(courses)-1)
    course = courses[num]
    return course

def get_phone(submit):
    '''
    处理电话后的.
    '''
    keys = ['homephone','home_phone','phone']
    phone = get_value(keys,submit)
    phone = str(phone)
    phone_ = phone.replace('(','').replace(')','').replace('-','')
    if '.' in phone_:
        phone_ = (phone_).split('.')[0]
    num = random.randint(0,9)        
    if len(str(phone_)) == 9:
        phone_ = phone_+str(num)
    if len(str(phone_)) == 8:
        phone_ = phone_+str(num)+str(num)        
    return phone_

def get_phone_plus1(submit):
    '''
    处理电话后的.
    '''
    keys = ['homephone','home_phone','phone']
    phone = get_value(keys,submit)
    phone_ = phone.replace('(','').replace(')','').replace('-','')
    if '.' in phone_:
        phone_ = (phone_).split('.')[0]
    num = random.randint(0,9)        
    if len(str(phone_)) == 9:
        phone_ = phone_+str(num)
    if len(str(phone_)) == 8:
        phone_ = phone_+str(num)+str(num)   
    if phone_[0] != '1':
        phone_ = '1'+phone_     
    return phone_


def get_firstname(submit):
    '''
    su lee--->su
    '''
    firstname = submit['name'].split(' ')[0]
    return firstname

def get_lastname(submit):
    '''
    su lee--->lee
    '''    
    lastname = submit['name'].split(' ')[1]
    return lastname

def get_email(submit):
    '''
    su lee--->su.lee@gmx.com
    @outlook.de
    @hotmail.de
    @web.de
    '''    
    if submit['email'] != '':
        return submit['email']
    end_list = ['@gmx.com','@outlook.de','@hotmail.de','@web.de','@mobile.de'] 
    num = random.randint(0,4)
    end = end_list[num]
    names = submit['name'].split(' ')
    name_num = random.randint(0,3)
    if name_num == 0:
        name = names[0]+'.'+names[1]
    elif name_num == 1:
        name = names[0]+names[1]+submit['dateofbirth'].split('.')[2][2:]
    elif name_num==2:
        name = names[0]+names[1][0].upper()+submit['dateofbirth'].split('.')[2][2:]
    else:
        name = names[0]+names[1]+submit['dateofbirth'].split('.')[2]
    email = name+end
    return email


def get_phone_de(submit):
    '''
    (0 95 69) 12 78
    '''
    phone = submit['phone'].replace('(','').replace(')','').replace(' ','')
    return phone

def get_phone_de_pre(submit):
    '''
    (0 95 69) 12 78
    -->0 95 69
    '''
    phone = get_phone_de(submit)
    pre = phone[:5]
    return pre

def get_phone_de_last(submit):
    '''
    (0 95 69) 12 78
    -->1278
    '''
    phone = get_phone_de(submit)
    last = phone[5:]
    return last

def get_name_de(submit):
    '''
    lee cun
    leecun
    '''
    name = submit['name'].replace(' ','')
    return name


def get_id_number(submit):
    '''
    4810690468<<D<<9602120<2702124<<<<<<<8    
    -->4810690468
    '''
    id_ = submit['id_number'].split('<<')[0]
    return id_ 


def get_phone_fr(submit):
    '''
    处理电话后的.
    '''
    keys = ['homephone','home_phone','phone']
    phone = get_value(keys,submit)
    phone_ = phone.replace('(','').replace(')','').replace('-','')
    if '.' in phone_:
        phone_ = (phone_).split('.')[0]
    if phone_[0:2] == '33':
        phone_ = phone_[2:]
    if phone_[0] != '0':
        phone_ = '0'+phone_
    return phone_

def get_phone_3(submit):
    '''
    phone: 1234567890
    return : 123

    '''
    phone = get_phone(submit)
    phone_ = phone[0:3]
    return phone_

def get_expiration_date(submit):
    '''
    MM/YY
    '''
    if len(submit['month']) == 1:
        mm = '0'+submit['month']
    else:
        mm = submit['month']
    if len(submit['year']) == 2:
        yy = submit['year']
    else:
        yy = submit['year'][-2:]        
    date = mm+yy
    return date

def get_phone_6(submit):
    '''
    phone: 1234567890
    return : 456

    '''
    phone = get_phone(submit)
    phone_ = phone[3:6]
    return phone_

def get_phone_10(submit):
    '''
    phone: 1234567890
    return : 7890

    '''
    phone = get_phone(submit)
    phone_ = phone[6:]
    return phone_

def get_workphone_3(submit):
    '''
    phone: 1234567890
    return : 123

    '''
    phone = get_workphone(submit)
    phone_ = phone[0:3]
    return phone_

def get_workphone_6(submit):
    '''
    phone: 1234567890
    return : 456

    '''
    phone = get_workphone(submit)
    phone_ = phone[3:6]
    return phone_

def get_workphone_10(submit):
    '''
    phone: 1234567890
    return : 7890

    '''
    phone = get_workphone(submit)
    phone_ = phone[6:]
    return phone_

def get_workphone(submit):
    '''
    处理电话后的.
    '''
    keys = ['workphone','work_phone','phone']
    phone = get_value(keys,submit)
    phone_ = phone.replace('(','').replace(')','').replace('-','')
    if '.' in phone_:
        phone_ = (phone_).split('.')[0]
    num = random.randint(0,9)
    if len(str(phone_)) == 9:
        phone_ = phone_+str(num)
    if len(str(phone_)) == 8:
        phone_ = phone_+str(num)+str(num)           
    return phone_

def get_workphone_unique(submit):
    '''
    homephone:123456789
    workphone:123456789-->123456780
    '''
    workphone = get_workphone(submit)
    for i in range(10):
        num = random.randint(0,9)
        if num == workphone[-1]:
            continue
        workphone = workphone[:-1]+str(num) 
        break
    return workphone


def get_phone_dadao(submit):
    '''
    123-123-12345
    '''
    phone = submit['phone']
    a = phone[0:3]
    b = phone[3:6]
    c = phone[6:]
    phone = a+'-'+b+'-'+c
    return phone

def get_uk_phone1(phone):
    phone = phone.replace(' ','')
    if phone[0] == '0':
        if phone[0:4] == '0044':
            phone = phone[4:]
        else:
            phone = phone[1:]
    elif phone[0:2] == '44':
        phone = phone[2:]
    elif phone[0:3] == '+44':
        phone = phone[3:]
    return phone

def get_payday_dict():
    paydaydict = {
    '2020':{
    '3':['13','26'],
    '4':['9','28'],
    '5':['7','21'],
    '6':['11','25'],
    '7':['9','23'],
    '8':['13','27'],
    '9':['9','23'],
    '10':['9','23'],
    '11':['9','23'],
    '12':['9','23'],
    }
    }
    return paydaydict    

def get_month_word(month):
    '''
    January
    '''
    month_word = ['January','February','March','April','May','June','July','August','September','October','November','December']
    month_list = [i+1 for i in range(12)]
    index = month_list.index(month)
    month = month_word[index]
    return month     

def month_change(submit=''):
    '''
    9.0 --> 09
    '''
    month = submit['month']
    month = str(month).split('.')[0]
    if len(month) == 1:
        month = '0'+ month
    return month

def year_change(submit):
    '''
    2020,2019
    '''
    year = str(submit['year']).split('.')[0]
    return year

def year_change_short(submit):
    '''
    98,97
    '''
    year = str(submit['year']).split('.')[0]
    if len(year) == 4:
        year = year[2:]
    return year

def get_next_payday_list(submit):
    '''
    [11,01,1991] 
    '''
    paydaydict = get_payday_dict()
    year = datetime.datetime.now().year
    month = datetime.datetime.now().month
    day = datetime.datetime.now().day
    day_1 = paydaydict[str(year)][str(month)][0]
    day_2 = paydaydict[str(year)][str(month)][1]    
    date = [0,0,0]    
    if day < int(day_1):
        day = day_1
        date[0] = month
        date[1] = day
        date[2] = year
    elif day >= int(day_1) and day <int(day_2):
        day = day_2
        date[0] = month
        date[1] = day
        date[2] = year
    else:
        if month != 12:
            month = month + 1
            day = paydaydict[str(year)][str(month+1)][0]
            date[0] = month
            date[1] = day
            date[2] = year
        else:
            month = 1
            day = paydaydict[str(year+1)]['1'][0]
            date[0] = month
            date[1] = day
            date[2] = year
    return date

def get_next_payday2_list(submit):
    '''
    [25,01,1991] 
    '''
    paydaydict = get_payday_dict()    
    date = get_next_payday_list(submit)
    month = date[0]
    day = date[1]
    year = date[2]
    date_monthly = [0,0,0] 
    if month == 12:
        if day == paydaydict[str(year)]['12'][0]:
            date_monthly[0] = 12
            date_monthly[1] = paydaydict[str(year)]['12'][1]
            date_monthly[2] = year
        else:
            date_monthly[0] = 1
            date_monthly[1] = paydaydict[str(year+1)]['1'][0]
            date_monthly[2] = year+1
    else:
        if day == paydaydict[str(year)][str(month)][0]:
            date_monthly[0] = month
            date_monthly[1] = paydaydict[str(year)][str(month)][1]
            date_monthly[2] = year
        else:
            date_monthly[0] = month + 1
            date_monthly[1] = paydaydict[str(year)][str(month+1)][0]
            date_monthly[2] = year
    # if day >= 30:
    #     day_pay = 15
    #     month = month + 1
    # month = get_month_word(month)

    return date_monthly

def get_next_payday(submit=''):
    '''
    [January,01,1991] 
    '''    
    date = get_next_payday_list('')
    month = date[0]
    month = get_month_word(month)
    date[0] = month
    return date

def get_next_payday2(submit=''):
    '''
    [January,01,1991] 
    '''        
    date = get_next_payday2_list('')
    month = date[0]
    month = get_month_word(month)
    date[0] = month
    return date

def get_next_payday_dd(submit):
    '''
    dd
    '''
    payday = get_next_payday_list('')
    payday_dd = str(payday[1])
    if len(payday)==1:
        payday = '0'+payday     
    return payday_dd

def get_next_payday2_dd(submit):
    '''
    dd
    '''
    payday = get_next_payday2_list('')
    payday_dd = str(payday[1])
    return payday_dd

def get_next_payday_mm(submit):
    '''
    mm--06
    '''
    payday = get_next_payday_list('')
    payday_mm = str(payday[0])
    if len(payday_mm)==1:
        payday_mm = '0'+payday_mm    
    return payday_mm

def get_next_payday_mm_signum(submit):
    '''
    mm-6
    '''
    payday = get_next_payday_list('')
    payday_mm = str(payday[0])   
    return payday_mm

def get_next_payday2_mm(submit):
    '''
    mm
    '''
    payday = get_next_payday2_list('')
    payday_mm = str(payday[0])
    if len(payday_mm)==1:
        payday_mm = '0'+payday_mm
    return payday_mm

def get_next_payday_mm_str(submit):
    '''
    mm_str
    '''
    payday = get_next_payday_list('')
    payday_mm = payday[0]
    payday_mm = get_month_word(payday_mm)
    return payday_mm

def get_next_payday2_mm_str(submit):
    '''
    mm_str
    '''
    payday = get_next_payday2_list('')
    payday_mm = payday[0]
    payday_mm = get_month_word(payday_mm)
    return payday_mm

def get_next_payday_year(submit):
    '''
    yy
    '''
    payday = get_next_payday_list('')
    payday_yy = payday[2]
    return payday_yy

def get_next_payday2_year(submit):
    '''
    yy
    '''
    payday = get_next_payday2_list('')
    payday_yy = payday[2]
    return payday_yy

def get_next_payday_all(submit=''):
    '''
    mm/dd/year
    '''
    payday = get_next_payday_list('')
    if len(str(payday[0])) == 1:
        payday[0] = '0' + str(payday[0])
    if len(str(payday[1])) == 1:
        payday[1] = '0' + str(payday[1])    
    payday_all = str(payday[0])+'/'+str(payday[1])+'/'+str(payday[2])
    return payday_all

def get_next_payday_all_str(submit=''):
    '''
    2020-02-12
    '''
    payday = get_next_payday_list('')
    if len(str(payday[0])) == 1:
        payday[0] = '0' + str(payday[0])
    if len(str(payday[1])) == 1:
        payday[1] = '0' + str(payday[1])    
    payday_all = str(payday[2])+'-'+str(payday[0])+'-'+str(payday[1])
    return payday_all

def get_next_payday2_all(submit=''):
    '''
    mm/dd/year
    '''
    payday = get_next_payday2_list('')    
    if len(str(payday[0])) == 1:
        payday[0] = '0' + str(payday[0])
    if len(str(payday[1])) == 1:
        payday[1] = '0' + str(payday[1])    
    payday_all = str(payday[0])+'/'+str(payday[1])+'/'+str(payday[2])
    return payday_all

def get_next_payday_bi_str(submit=''):
    '''
    Janauary 01,2020
    '''
    payday = get_next_payday()
    payday_ = payday[0]+' '+str(payday[1])+','+str(payday[2]) 
    return payday_   

def get_next_payday2_bi_str(submit=''):
    '''
    Janauary 01,2020
    '''
    payday = get_next_payday2()
    payday_ = payday[0]+' '+str(payday[1])+','+str(payday[2]) 
    return payday_   


def monthly_payment(submit=''):
    '''
    1000-3999
    '''
    payment = random.randint(100,300)*10
    return payment

def rent_payment(submit=''):
    '''
    2000-3000
    '''
    payment = random.randint(200,300)*10
    return payment

def get_state_byzip(zip_=''):
    '''
    find state by zip
    '''
    state = db.get_state_byzip(zip_)
    return state


def makedir_pic(path):
    isExists=os.path.exists(path)
    if isExists:
        return
    else:
        os.makedirs(path)

def test_d():
    address = '11235 OAK LEAF DR APT 1919'
    apt = apt_get(address)
    print(apt)

def select_email_type(email):
    pass



if __name__ == '__main__':
    birthday = monthly_payment('')
    print(birthday)

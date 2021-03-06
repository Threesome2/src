import sys
from luminati import ip_test,get_port_random,delete_port_s,add_proxy,get_lpm_ip
import threading
import threadpool
from db import update_port,get_account,read_plans
from time import sleep
import Chrome_driver
import emaillink
import random
import datetime



pool = threadpool.ThreadPool(30)

def traffic_test(traffic):
    uas = Chrome_driver.get_ua_all()
    ua = Chrome_driver.get_ua_random(uas)
    # print(ua)
    traffic['ua'] = ua   

    click = random.randint(24,40)
    referer = ''
    i = 0
    proxy_error_count = 0
    for i in range(click):
        sleep(10)
        proxy_flag = 0
        while True:
            if proxy_error_count>=5:
                print('proxy_error_count max 5 time,check luminati')  
                break
            flag,proxy_info = ip_test(traffic['port_lpm'])
            print(flag,proxy_info,'\n=========================')
            if flag == 1:
                proxy_flag = 1
                break
            elif flag == -1:
                print('bad port,change into new')
                port_new = get_port_random()
                update_port(traffic['port_lpm'],port_new)
                delete_port_s(traffic['port_lpm'])                
                traffic['port_lpm'] = port_new
                print(port_new)
                try:
                    add_proxy(port_new,country=traffic['Country'],proxy_config_name='zone2',ip_lpm=traffic['ip_lpm'])
                except Exception as e:
                    proxy_error_count+=1
                    print(str(e))
        if proxy_flag == 0:
            print('proxy error!!!!!!!!!!!!!!!!!!!!')
            now=datetime.datetime.now()
            t = now.strftime('%c')            
            content = '''
            Error time: %s
            plan_id:%s
            Mission_id:10000,10001
            Error:      Sending traffic errot,luminati can't open port,need check 
            '''%(str(t),traffic['Plan_Id'])
            emaillink.email_alert(content)            
            return
        print('Sending traffic:',i+1,'clicks for mission',traffic['Mission_Id'])
        # luminati.refresh_proxy(traffic['ip_lpm'],traffic['port_lpm'])
        if traffic['traffic_method'] == 'Crawl':
            print('Crawl')
            # print('fffffffffffffffffffffffff')
            try:
                get_lpm_ip(traffic['port_lpm'],url = traffic['url_link'],Referer = referer,debug=1)
            except Exception as e:
            	print(str(e))
        else:
            try:
                print('+++++++++++++++++++++++++++')
                get_unique_traffic(traffic)
            except Exception as e:
                print(str(e))
        # i += 1
    delete_port_s(traffic['port_lpm'])

def main(i):
    for j in range(111):
        account = get_account()
        plan_id = account['plan_id']    
        traffics = read_plans(i)
        # print(len(traffics))
        ip_lpm = account['IP']
        for traffic in traffics:
            # traffic['key'] = 'getaround'
            traffic['port_lpm'] = get_port_random()
            # traffic['Record'] = 3            
            # print('===========================')
            # print(traffic['Country'],traffic['port_lpm'])
            # luminati.add_proxy(traffic['port_lpm'],country=traffic['Country'],proxy_config_name='zone2',ip_lpm=ip_lpm)
            add_proxy(traffic['port_lpm'],country=traffic['Country'],proxy_config_name='zone2',ip_lpm=ip_lpm)            
        requests = threadpool.makeRequests(traffic_test, traffics)
        [pool.putRequest(req) for req in requests]
        pool.wait() 
        print('finish sending traffic,sleep for 30')
        sleep(3000)
        # return

def test():
    traffic = {}
    traffic['port_lpm'] = 24000
    traffic['Country'] = 'us'
    traffic['ip_lpm'] = '192.168.89.130'
    while True:    
        flag,proxy_info = ip_test(traffic['port_lpm'])
        print(flag,proxy_info,'\n=========================')
        if flag == 1:
            pass
        elif flag == -1:
            print('bad port,change into new')
            port_new = get_port_random()
            update_port(traffic['port_lpm'],port_new)
            delete_port_s(traffic['port_lpm'])                
            traffic['port_lpm'] = port_new
            print('New port:',port_new)
            try:
                add_proxy(port_new,country=traffic['Country'],proxy_config_name='zone2',ip_lpm=traffic['ip_lpm'])
            except Exception as e:
                print(str(e))

def get_unique_traffic(traffic):
    traffic['traffic'] = True
    chrome_driver = Chrome_driver.get_chrome(traffic)
    # traffic['url_link'] = 'https://www.moneymethods.net'
    chrome_driver.get(traffic['url_link'])
    flag_traffic = 0
    for i in range(15):
        print(chrome_driver.title,'----',traffic['traffic_key'])
        if traffic['traffic_key'] in chrome_driver.title:
            # sleep(500)
            sleep(5)
            chrome_driver.close()
            chrome_driver.quit()
            break
        else:
            sleep(1)
    try:
        chrome_driver.close()
        chrome_driver.quit()
    except:
        pass

if __name__ == '__main__':
    paras=sys.argv
    i = int(paras[1])
    # i = 9
    main(i)
    # test()



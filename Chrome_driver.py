from selenium import webdriver
import os
import sys
sys.path.append("..")
from time import sleep
import random
import zipfile

def get_ua_all():
    uas = []
    with open(r'../res/ua.txt') as f:
        lines = f.readlines()
        for line in lines:
            if line.strip('\n') != '':
                if 'Windows' not in line:
                    continue 
                if 'Chrome' in line:
                    uas.append(line.strip('"').strip("'").strip('\n'))

    # for ua in uas.split('/n'):
        # print(ua)
    return uas

def get_ua_random(uas):
    num = random.randint(0,len(uas)-1)
    # print(uas[num])
    return uas[num]


def get_chrome(submit = None):
    uas = get_ua_all()
    ua = get_ua_random(uas)
    print(ua)
    options = webdriver.ChromeOptions()
    path_download = get_dir()
    prefs = {"download.default_directory": path_download,
             "download.prompt_for_download": False,
             "download.directory_upgrade": True,
             "safebrowsing.enabled": True,
             'profile.default_content_settings.popups': 0
             # "profile.managed_default_content_settings.images": 2
             }    
    # options.add_experimental_option('prefs', prefs)
    # extension_path = '../tools/extension/1.1.0_0.crx'   
    # options.add_extension(extension_path) 
    # prefs = {
    # 'profile.default_content_setting_values': {
    # # "User-Agent": ua, # 更换UA
    # # 0 为屏蔽弹窗，1 为开启弹窗
    # 'profile.default_content_settings.popups': 0,
    # } 
    # }   
    options.add_argument('user-agent=' + ua) 
    if 'Mission_dir' in submit:
        submit['Mission_dir'] = submit['Mission_dir'].replace('//','\\') 
        print('Selenium in using user-data-dir:',submit['Mission_dir'])
        options.add_argument('--user-data-dir='+submit['Mission_dir'])
    if 'ip_lpm' in submit:
        ip = submit['ip_lpm']
        port = submit['prot_lpm']
        proxy = 'socks5://%s:%s'%(ip,port)
        options.add_argument('--proxy-server=%s'%proxy)
    # options.add_argument('--single-process')
    # options.add_argument('--process-per-tab')    
    # options.add_argument('--disable-gpu')        
    options.add_argument("--disable-automation")
    options.add_experimental_option("excludeSwitches" , ["enable-automation","load-extension"])
    options.add_experimental_option("prefs", prefs) 
    chrome_driver = webdriver.Chrome(chrome_options=options)
    chrome_driver.set_page_load_timeout(300)
    chrome_driver.implicitly_wait(20)  # 最长等待8秒  
    # chrome_driver.set_window_size(500,500)
    return chrome_driver

def get_dir():
    path = os.getcwd()
    print(path)
    path_up = path[:-3] 
    print(path_up)
    path_download = os.path.join(path_up,'download')
    print(path_download)
    return path_download

def clean_download():
    path_download = get_dir()
    misc_init(path_download)
    return 

def download_status():
    path_download = get_dir()
    modules = os.listdir(path_download)
    return modules



def misc_init(target_folder):
    import os
    import shutil
    import traceback
    # import globalvar    
    # clean the test result folder
    # get the current path
    current_path = target_folder
    # some folder not delete
    # except_folders = globalvar.Except_Folders
    except_folders = ['']
    # get the folder uder current path
    current_filelist = os.listdir(current_path)
    print(current_filelist)
    for f in current_filelist:
    # f should be a absolute path, if python is not run on current path
        if os.path.isdir(os.path.join(current_path,f)):
            print('------')
            if f in except_folders:
                continue
            else:
                print('++++++++++')
                real_folder_path = os.path.join(current_path, f)
                try:
                    for root, dirs, files in os.walk(real_folder_path):
                        for name in files:
                            print(name)
                            # delete the log and test result
                            del_file = os.path.join(root, name)
                            os.remove(del_file)
                            print('remove file[%s] successfully' % del_file)
                    shutil.rmtree(real_folder_path)
                    print('remove foler[%s] successfully' % real_folder_path)
                except Exception as e:
                    # traceback.print_exc()
                    print('===========')
        else:
            os.remove(os.path.join(current_path,f))



if __name__ == '__main__':
    # clean_download()
    chrome_driver = get_chrome()
    chrome_driver.get('http://whoer.net')
    sleep(1000)

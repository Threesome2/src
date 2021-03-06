


Input_Config ={
    'firstname' : ['get_name_real'],
    'first_name' : ['get_name_real'],    
    'lastname'  : ['get_name_real'],
    'last_name'  : ['get_name_real'],    
    'address'   : ['apt_get'],
    'homephone' : ['get_phone','get_phone_plus1','get_phone_3','get_phone_6','get_phone_10'],
    'home_phone' : ['get_phone','get_phone_3','get_phone_6','get_phone_10'],
    'workphone' : ['get_workphone','get_workphone_3','get_workphone_6','get_workphone_10','get_workphone_unique'],
    'work_phone' : ['get_workphone','get_workphone_3','get_workphone_6','get_workphone_10','get_workphone_unique'],    
    'zip'       : ['get_zip'],
    'dateofbirth' : ['get_birthday_mm','get_birthday_dd','get_birthday_year','get_birthday_all'],    
    'email'     : ['select_email_type'],
    'cvv'          : ['cvv_get'],
    'katou'     : ['get_zip'],
    'year'      : ['get_expiration_date'],
    'fullname'    : ['get_fullname'],  
    'phone'     : ['get_phone_dadao','get_phone_de','get_phone_de_pre','get_phone_de_last'],    
    'date_of_birth' : ['get_birthday_mm','get_birthday_dd','get_birthday_year','get_birthday_all','get_birthday_all_2'],    
    'ssn'           : ['get_ssn','ssn_first_3','ssn_mid_2','ssn_last4'],
    'drivers_license': ['get_drivers_license'],
    'routing_number' : ['get_routing_number'],
    'account_number' : ['get_account_number'],
    'net_monthly_income' : ['get_income','get_income_other'],
    'employer':['get_employer_info'],
    'occupation':['get_occupation_info'],  
    'name':['get_firstname','get_lastname','get_name_de'],
    'email':['get_email'],
    'id_number':['get_id_number']
}

Select_Config ={
    'state'       : ['get_name_real'],
    'date_of_birth' : ['get_birthday_mm','get_birthday_dd','get_birthday_year','get_birthday_all'],
    'requested_loan_amount':['get_next_payday_dd','get_next_payday_mm','get_next_payday_mm_str','get_next_payday_year','get_next_payday_all','get_next_payday_bi_str','get_next_payday2_dd','get_next_payday2_mm','get_next_payday2_mm_str','get_next_payday2_year','get_next_payday2_all','get_next_payday2_bi_str','get_next_payday_all_str'],
    'pay_period':['get_next_payday_dd','get_next_payday_mm','get_next_payday_mm_str','get_next_payday_year','get_next_payday_all','get_next_payday_bi_str','get_next_payday2_dd','get_next_payday2_mm','get_next_payday2_mm_str','get_next_payday2_year','get_next_payday2_all','get_next_payday2_bi_str','get_next_payday_all_str'],
    'katou':['get_state_byzip'],
    'month':['month_change'],
    'year':['year_change','year_change_short'],
}

Generate_Config = {
    'dateofbirth' : ['get_birthday_mm','get_birthday_dd','get_birthday_year','get_birthday_all','get_birthday_all_2'],    
    'pwd'         : ['password_get','password_get_Nostale','get_pwd_real','get_pwd_real2','get_pwd_real3','get_pwd_real4'],        
    'height'      : ['get_height_ft','get_height_inch','get_height_weight'],  
    'fullname'    : ['get_fullname'], 
    'firstname'   : ['get_name_real'],  
    'next_pay_day':['get_next_payday_bi_str','get_next_payday2_bi_str','get_next_payday_all','get_next_payday2_all'],
    'income'      :['get_random_income'],
    'nextpayday_dd'  :['get_next_payday_dd'],
    'nextpayday2_dd'  :['get_next_payday2_dd'],
    'nextpayday_mm'  :['get_next_payday_mm'],
    'nextpayday2_mm'  :['get_next_payday2_mm'],
    'nextpayday_mm_str'  :['get_next_payday_mm_str'],
    'nextpayday2_mm_str'  :['get_next_payday2_mm_str'],
    'nextpayday_yy'  :['get_next_payday_year'],
    'nextpayday2_yy'  :['get_next_payday2_year'],
    'nextpayday_all'  :['get_next_payday_all'],
    'nextpayday2_all'  :['get_next_payday2_all'],
    'nextpayday_bi_str'  :['get_next_payday_bi_str'],
    'nextpayday2_bi_str'  :['get_next_payday2_bi_str'],
    'hire_date':['hire_date'],
    'year_at_residence_gen':['get_year_atresidence'],
    'monthly_payment':['monthly_payment','rent_payment'],
    'course':['get_courses'],
    'email':['get_email'],
}


def get_input_config(key):
    global Input_Config
    print('Input_Config:',Input_Config)
    if key in Input_Config:
        print('Input_Config[key]:',Input_Config[key])
        return Input_Config[key]
    else:
        print('Input_Config[key]:=====[]')        
        return []


def get_select_config(key):
    global Select_Config
    if key in Select_Config:
        print('Input_Config[key]:',Select_Config[key])
        return Select_Config[key]
    else:
        # print('Input_Config[key]:=====[]')        
        return []

def get_generate_config(key):
    global Generate_Config
    if key in Generate_Config:
        print('Input_Config[key]:',Generate_Config[key])
        return Generate_Config[key]
    else:
        # print('Input_Config[key]:=====[]')        
        return []

def get_generate_items():
    global Generate_Config
    return Generate_Config    
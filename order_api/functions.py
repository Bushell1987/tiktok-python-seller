import yaml
import time
import hmac
import hashlib
from datetime import  timedelta,datetime
from pytz import timezone


def file_get():
    with open('./data_files/access.yaml') as f:
        data = yaml.load(f, Loader=yaml.FullLoader)
    with open('./data_files/refresh.yaml') as f:
        refresh = yaml.load(f, Loader=yaml.FullLoader)
    return  refresh,data


def req_timestamp():
    #change timezone 
    tz_London = timezone('Europe/London')
    datetime_London = datetime.now(tz_London)
    timestamp = int(datetime_London.timestamp())

    return timestamp


def sign_request(app_secret,end_point,params):



    sort_sting = []
    for i in params:
        sort_sting.append(i)
    sorted_sting = sorted(sort_sting)

    base_string = ''
    for i in sorted_sting:
        order_id_list = ''
        if i == 'order_id_list':
            for v in params[i]:
                order_id_list = order_id_list + str(v)
               

            base_string = str(base_string) + str(i) + str('576461344021252703576461344068634774')
           
        else:  
            base_string = str(base_string) + str(i) + str(params[i])
    base_string = app_secret +  end_point + base_string  + app_secret

    sign = hmac.new(key=app_secret.encode(), msg=base_string.encode(), digestmod=hashlib.sha256).hexdigest()


    return sign
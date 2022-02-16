
import requests
from functions import req_timestamp,sign_request,file_get
import json
timestamp = req_timestamp()
refresh,data = file_get()




if __name__ == '__main__':

    base_url =  "https://open-api.tiktokglobalshop.com/"
    end_point = "/api/logistics/shipping_providers"

    params = {}
 
    #required

    
    #please ensure theses follow the above params
    params['app_key'] = data['app_key']
    params['timestamp'] = timestamp
    params['sign'] = sign_request(data['app_secret'],end_point,params)
    params['access_token'] = refresh['access_token']





    url = base_url + end_point

    payload = {}
    headers = {
    'Content-Type': 'application/json'
    }

    response = requests.request("get", url, headers=headers, data=payload, params=params)

    #print(response.text)


    
    #Bonus to csv
    #pip install pandas


    import pandas as pd

    if response.json()['data']['delivery_option_list'][1]['delivery_option_name']  == 'LSV-SendBySeller-GB':
        json_data = response.json()['data']['delivery_option_list'][1]['shipping_provider_list']
    if response.json()['data']['delivery_option_list'][0]['delivery_option_name']  == 'LSV-SendBySeller-GB':
        json_data = response.json()['data']['delivery_option_list'][0]['shipping_provider_list']

    value_data = {}
    list_data = []
    
    for i in json_data:
        for k in i:
            value_data[k] = i[k]
        list_data.append(value_data)
        value_data = {}
    
    df = pd.DataFrame(list_data)
    df.to_csv('./logistics_api/delivery_data.csv')
    








    #print(data)
    """
    """




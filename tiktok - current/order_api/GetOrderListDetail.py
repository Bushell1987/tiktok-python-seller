
import requests
from functions import req_timestamp,sign_request,file_get
import json
timestamp = req_timestamp()
refresh,data = file_get()













if __name__ == '__main__':


    base_url =  "https://open-api.tiktokglobalshop.com/"
    end_point = "/api/orders/search"

    params = {}
 
    #required
    params['page_size'] = 2 # 1 - 50

    #not required 
    #uncomment the below when needed the additional params here

    #params['create_time_from'] = 1623812664 # fomat unix
    #params['create_time_to'] = 1623812664 # format unix
    #params['update_time_from'] = 1623812664 # format unix
    #params['update_time_to'] = 1623812664 # format unix

    """
        order_status
        UNPAID = 100;
        AWAITING_SHIPMENT = 111;
        AWAITING_COLLECTION = 112;
        IN_TRANSIT = 121;
        DELIVERED = 122;
        COMPLETED = 130;
        CANCELLED = 140;
    """
    #params['order_status'] = 100 # format unix

    #params['cursor'] = '' # paginate how to get the next set of data get next_cursor
    #params['sort_by'] = 'CREATE_TIME' #Default value: CREATE_TIME,Available values: CREATE_TIME,UPDATE_TIME
    #params['sort_type'] = 1 #1 (DESC),2 (ASC), Default = 11


  


    #please ensure theses follow the above params
    params['app_key'] = data['app_key']
    params['timestamp'] = timestamp
    params['sign'] = sign_request(data['app_secret'],end_point,params)
    params['access_token'] = refresh['access_token']





    url = base_url + end_point

    payload={}
    headers = {
    'Content-Type': 'application/json'
    }

    response = requests.request("post", url, headers=headers, data=payload, params=params)

  
    return_json = response.json()
    

    orders = []

    if return_json['message'] == 'Success':
        for i in return_json['data']['order_list']:
            orders.append(i['order_id'])
            



    end_point = "/api/orders/detail/query"

    params = {}
 
    #required

    
    #please ensure theses follow the above params
    params['app_key'] = data['app_key']
    params['timestamp'] = timestamp
    params['sign'] = sign_request(data['app_secret'],end_point,params)
    params['access_token'] = refresh['access_token']





    url = base_url + end_point

    payload = json.dumps({
                        "order_id_list": orders
                        })
    headers = {
    'Content-Type': 'application/json'
    }

    response = requests.request("post", url, headers=headers, data=payload, params=params)

    print(response.text)





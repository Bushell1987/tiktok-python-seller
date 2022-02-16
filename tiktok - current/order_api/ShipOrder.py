
import requests
from functions import req_timestamp,sign_request,file_get
import json
timestamp = req_timestamp()
refresh,data = file_get()




if __name__ == '__main__':


    base_url =  "https://open-api.tiktokglobalshop.com/"
    end_point = "/api/order/rts"

    params = {}
 
    #required
    params['order_id'] = ''
    params['tracking_number'] = '' 
    params['shipping_provider_id'] = '' 

    



  


    #please ensure theses follow the above params
    params['app_key'] = data['app_key']
    params['timestamp'] = timestamp
    params['sign'] = sign_request(data['app_secret'],end_point,params)
    params['access_token'] = refresh['access_token']



    url = base_url + end_point

    payload = json.dumps({
                        "order_id": ""
                        ,"tracking_number": ""
                        ,"shipping_provider_id": ""
                        
                        })
    headers = {
    'Content-Type': 'application/json'
    }

    response = requests.request("post", url, headers=headers, data=payload, params=params)

  
    print(response.text)
    





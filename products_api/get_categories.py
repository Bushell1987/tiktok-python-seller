
import requests
from functions import req_timestamp,sign_request,file_get
import json
import pandas as pd
timestamp = req_timestamp()
refresh,data = file_get()


if __name__ == '__main__':

    base_url =  "https://open-api.tiktokglobalshop.com/"
    end_point = "/api/products/categories"

    params = {}
 
    #required
    #please ensure theses follow the above params
    params['app_key'] = data['app_key']
    params['timestamp'] = timestamp
    params['sign'] = sign_request(data['app_secret'],end_point,params)
    params['access_token'] = refresh['access_token']
    url = base_url + end_point

    payload = ''
    headers = {
    'Content-Type': 'application/json'
    }

    response = requests.request("get", url, headers=headers, data=payload, params=params)

    ##print(response.text)






    #Additional pandas clean up leaf break down
    json_response = response.json()
    #print(json_response)



    
    #print(mydata)
    #print(json_response['message'])




    #exit()
    flow = {}
    data =[]
    if json_response['message'] == 'Success':
        for i in json_response['data']['category_list']:
            
            for k in i:
                flow[k] = i[k]
            data.append(flow)
            flow = {}
        
        #print(data)
        mydata = pd.DataFrame(data)
      
        print(len(mydata))




        #pandas
        """
        
        
        here we will make the data more usable for your table is you wish

        1. is_parent,is_child,is_leaf_df normalising the api return data, you can load these as single dataset and join late in your
        data environment

        2. joing the three table to make the data more usable 

        3. Final dataframe output, clean the column names as you wish

        id_leaf                     - Apply as index use this when create the product as this is the leaf id
        local_display_name_leaf     - index name


        
        """
        #1
        is_parent = mydata[mydata.parent_id == '0']
        is_child = mydata[mydata['is_leaf'] == False]
        is_leaf_df = mydata[mydata['is_leaf'] == True]
        
        

        #2
        leaf_child_join = is_leaf_df.merge(is_child, left_on='parent_id',right_on='id', how='left',suffixes=('_leaf','_child'))
        is_parent_join = leaf_child_join.merge(is_parent, left_on='parent_id_child',right_on='id', how='left')

        #2
        clean_df = is_parent_join[['id_leaf','local_display_name_leaf','id_child','local_display_name_child','id','local_display_name']].copy()
        #clean_df.to_csv('clean_df.csv')
        print(len(clean_df))


        

     
    else:
        print('fail') 











import requests
from get_tokens import get_token
import yaml
import time

def refresh_token(app_key,app_secret):


    with open('./data_files/refresh.yaml') as f:
        refresh = yaml.load(f, Loader=yaml.FullLoader)
    
    refresh_token = refresh['refresh_token']
    print(refresh_token)
    url = f"https://auth.tiktok-shops.com/api/token/refreshToken?app_key={app_key}&app_secret={app_secret}&refresh_token={refresh_token}&grant_type=refresh_token"

    payload={}
    headers = {}
    
    response = requests.request("POST", url, headers=headers, data=payload)

    json_data = response.json()
    print(json_data)
    message = json_data['message']


    print(message)

    



    if message == 'success':
        #set_resresh_token

        srt = json_data['data']


        refreshed_time = ((srt['access_token_expire_in'] - int(time.time()))/60/60/24)
        days_to_refresh = int(refreshed_time)
        refresh_comment = f'{days_to_refresh} Day/s left before access token can be refreshed'

        if int(refreshed_time) == 6:
            refresh_comment = 'Token Refreshed'
            refresh['access_token'] = srt['access_token']
            refresh['access_token_expire_in'] = srt['access_token_expire_in']
            refresh['refresh_token'] = srt['refresh_token']
            refresh['refresh_token_expire_in'] = srt['refresh_token_expire_in']
            refresh['open_id'] = srt['open_id']
            refresh['success'] = 1
        
    with open('./data_files/refresh.yaml', 'w') as f:
        yaml.dump(refresh, f)


    print(srt['refresh_token'])
    return message,refresh_comment

import requests
import yaml









def get_token(app_key,app_secret,auth_code):

    with open('./data_files/refresh.yaml') as f:
        refresh = yaml.load(f, Loader=yaml.FullLoader)

    url = f"https://auth.tiktok-shops.com/api/token/getAccessToken?app_key={app_key}&app_secret={app_secret}&auth_code={auth_code}&grant_type=authorized_code"

    payload={}
    headers = {}
    
    response = requests.request("POST", url, headers=headers, data=payload)

    json_data = response.json()

    message = json_data['message']

    if message == 'success':
        #set_resresh_token
        srt = json_data['data']
        refresh['access_token'] = srt['access_token']
        refresh['access_token_expire_in'] = srt['access_token_expire_in']
        refresh['refresh_token'] = srt['refresh_token']
        refresh['refresh_token_expire_in'] = srt['refresh_token_expire_in']
        refresh['open_id'] = srt['open_id']
        refresh['success'] = 1

    with open('./data_files/refresh.yaml', 'w') as f:
        yaml.dump(refresh, f)

    return message

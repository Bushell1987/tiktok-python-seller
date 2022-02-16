from cmath import atan
import requests
import yaml
from auth_seller import seller_auth
from refresh_token import refresh_token
import time
"""
before you start crearte a tiktok account https://developers.tiktok-shops.com
you need to follow the tiktok development -  https://bytedance.feishu.cn/docx/doxcncNO25WrjATpVmkCauvRQRd


  -- This has been built based on Seller inhouse system's and not ERP
  -- This is a simple build for inhouse connection's


1. Ensure you fill access.yaml with the correct information from your onboarding
 -- app_key:        # https://developers.tiktok-shops.com/console/app/list
 -- app_secret:     # https://developers.tiktok-shops.com/console/app/list
 -- state:          # random string with no spaces and encoded


once you have perfromned this then you are ready to go live with the next steps

"""

with open('./data_files/access.yaml') as f:
    data = yaml.load(f, Loader=yaml.FullLoader)
    print(data)




with open('./data_files/refresh.yaml') as f:
    refresh = yaml.load(f, Loader=yaml.FullLoader)

print(refresh)

"""
refresh['access_token'] = 'changed'
with open('access.yaml', 'w') as f:
    yaml.dump(refresh, f)
""" 

app_key = data['app_key']
state  = data['state']
app_secret = data['app_secret']
success = refresh['success']

if success == 0:
    return_code = seller_auth(app_key,state,app_secret)
    print(return_code)

    #{'code': 0, 'message': 'success', 'data': {'access_token': 'pcV2nM30md1vowWCiW51SdQ3urYLsES7D6cC8ugBMoAfgyncvlTKQ8yuCVSaOY_C', 'access_token_expire_in': 1642757169, 'refresh_token': 'MDU2YzY4ZDc1NjVhOTdkMzQwYTMzMzM3ODBiNDNjNDYzYzg2YTYxMGZhZTYwMQ', 'refresh_token_expire_in': 1642929969, 'open_id': '7052903009872807682', 'seller_name': 'ISAWITFIRST'}}

if success == 1:
    #frefresh token will expire in 9 days 
    #access token can be refreshed in the last 24 hours of the expiry
    #this check is taken into consideration
    return_code,refresh_comment = refresh_token(app_key,app_secret)
    print('return_code:=',return_code,', refresh_comment:=',refresh_comment)
    





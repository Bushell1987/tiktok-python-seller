
from get_tokens import get_token

def seller_auth(app_key,state,app_secret):

    url = f"https://auth.tiktok-shops.com/oauth/authorize?app_key={app_key}&state={state}" 

    print(f"Please go to {url} on your browser and return the auth_code here:")
    auth_code = input()

    return_codes = get_token(app_key,app_secret,auth_code)

    return return_codes
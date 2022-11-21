# import requests
# from config import *
# from get_token import create_bearer_token

# def get_additional_fields(user_name, password, ip_addr, port, mission):
#     token = create_bearer_token(user_name, password, ip_addr, port, mission)
#     url = 'https://%s:%s/v2/%s'%(ip_addr, port, mission)
#     headers = {
#                 'accept': 'text/plain',
#                 'prefer': 'sync',
#                 # Already added when you pass json= but not when you pass data=
#                 # 'Content-Type': 'application/json',
#                 'authorization': token,
#                 }

#     response = requests.get(url, headers=headers, verify=False)
#     if response.ok:
#         dict_add_fields = response.json()['Results']
#     else:
#         raise Exception("Can't get Additional Fields!")
#     return dict_add_fields
    
def create_header(accept, prefer, authorization, extend=None):
    headers = {
        'accept' : accept,
        'prefer' : prefer,
        'authorization' : authorization,
    }
    if extend:
        headers.update(extend)
    return headers
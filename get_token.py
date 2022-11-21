import uuid
import base64
import requests
import warnings
from create_headers import create_header

warnings.filterwarnings('ignore') 

def create_bearer_token(user_name, password, ip_addr, port, index='123'):
    _key_bytes = bytes("%s"%(user_name)+":"+"%s"%(password), 'UTF-8')
    _uToken = base64.b64encode(_key_bytes).decode("utf-8")
    _clientid = str(uuid.uuid5(uuid.NAMESPACE_DNS, index))
    extend_headers = {'cliendid' : _clientid}
    headers = create_header('text/plain', 'sync', 'basic %s'%(_uToken), extend_headers)
    url_link = 'https://%s:%s/v2/WebToken'%(ip_addr, port)
    response = requests.get(url_link, headers=headers, verify=False)
    if response.ok:
        token = 'Bearer ' + response.json()['Token']
    else:
        raise Exception("Can't get token!")
    return token

if __name__=="__main__":
    token = create_bearer_token('admin', 'Vdc@2022', '171.244.132.78', '9550', index='123')
    print(token)
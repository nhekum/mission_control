import requests
from datetime import datetime
from config import dict_incident_type
from get_token import create_bearer_token
from create_headers import create_header

def upload_file(file_name, url):
    files = open(file_name, "rb")
    response = requests.post(url, files = {"file": files})
    if response.ok:
        return True
    else:
        raise Exception("Upload failed!")

def trigger_incident(user_name, password, ip_addr, port, addition_fields, incident_type_name, user_comment, location, extend_headers={}):
    token = create_bearer_token(user_name, password, ip_addr, port)
    headers = create_header(accept='text/plain', prefer='sync', authorization=token, extend=extend_headers)
    url = 'https://%s:%s/v2/Incidents'%(ip_addr, port)
    assert incident_type_name in dict_incident_type, "Don't have this type"

    incident_type_id = dict_incident_type[incident_type_name]
    external_id = datetime.now().strftime("%H:%M:%S_%d-%m-20%y")
    sample_location = {"EntityId": "ca585558-0c9b-498b-9265-998d47f6a0ef",
                        "Latitude": 45.478759,
                        "Longitude": -73.761054}

    json_data = {
    'Type': 'TriggerIncident',
    'IncidentTypeId': incident_type_id,
    "Location": location if location else sample_location,
    'ExternalId': external_id,
    'Comment': user_comment if user_comment else "This is a comment",
    }
    json_data.update({'AdditionalFields': addition_fields})
    response = requests.post(url, headers=headers, json=json_data, verify=False)
    if response.ok:
        id_incident = response.json()['Id']
        return id_incident
    else:
        raise Exception("Trigger failed!")

if __name__=="__main__":
    addition_fields= [{'Name': 'Thời gian', 'Value': '', 'DataType': 'String'},
                        {'Name': 'Địa điểm', 'Value': '', 'DataType': 'String'},
                        {'Name': 'Loại phương tiện', 'Value': '', 'DataType': 'String'},
                        {'Name': 'Biển số', 'Value': '', 'DataType': 'String'},
                        {'Name': 'Màu biển số', 'Value': '', 'DataType': 'String'},
                        {'Name': 'Hành vi vi phạm', 'Value': '', 'DataType': 'String'},
                        {'Name': 'Thiết bị giám sát', 'Value': '', 'DataType': 'String'},
                        {'Name': 'Người vận hành thiết bị', 'Value': '', 'DataType': 'String'},
                        {'Name': 'Đơn vị vận hành', 'Value': '', 'DataType': 'String'},
                        {'Name': 'Tên file ảnh biển số', 'Value': '', 'DataType': 'String'},
                        {'Name': 'Tên file ảnh xe', 'Value': '', 'DataType': 'String'},
                        {'Name': 'Tên file video', 'Value': '', 'DataType': 'String'},
                        {'Name': 'Tên file thông tin xử phạt', 'Value': '', 'DataType': 'String'},
                        {'Name': 'Phương pháp phát hiện vi phạm', 'Value': '', 'DataType': 'String'},
                        {'Name': 'Hình thức xử phạt', 'Value': '', 'DataType': 'String'},
                        {'Name': 'Phòng/đơn vị xử lý vi phạm hành chính',
                                 'Value': '',
                                 'DataType': 'String'},
                        {'Name': 'Thông tin chi tiết', 'Value': '', 'DataType': 'String'},
                        {'Name': 'Cán bộ hiện trường', 'Value': '', 'DataType': 'String'},     
                        {'Name': 'Hướng vi phạm', 'Value': '', 'DataType': 'String'}]
    trigger_incident('admin', 'Vdc@2022', '171.244.132.78', '9550', addition_fields, incident_type_name='Vi phạm thủ công', user_comment=None, location=None, extend_headers={})
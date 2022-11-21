import requests
from config import mission_access
from get_token import create_bearer_token
from create_headers import create_header

# commond_available=["AddComment", "AddNote", "AttachEntities", "ChangeAdditionalFields", "ChangeComment", "ChangeDescription", "ChangeExternalId",
#                 "ChangeIncidentType", "ChangeLocation", "ChangePriority", "ChangeState", "ClearLocation","DeleteComment", "DetachEntities", 
#                 "ForwardIncident", "PlaceOnHold", "ReleaseOwnership", "TakeOwnership", "TransferIncident"]

def add_comment(comment="Hello"):
    _command = {"Type": "AddComment",
               "Comment": "%s"%(comment)}
    return _command

def add_note(notetype="5afb6c8e-9939-42d8-8505-18fad42dfbc1", displaytext="My new note", 
            payload="{\u0022Id\u0022:1,\u0022Name\u0022:\u0022It\u0027s a test\u0022}", PayloadFormat="JSON"):
    _command = {"Type": "AddNote",
                "NoteType": "%s"%(notetype),
                "DisplayText": "%s"%(displaytext),
                "Payload": "%s"%(payload),
                "PayloadFormat": "%s"%(PayloadFormat)
                }
    return _command

def attach_entities(entities=["c19de30b-5fc7-44b3-b8d3-1c81ae6fa25b"]):
    _command = {"Type": "AttachEntities",
                "Entities": entities
                }
    return _command

def change_additional_fields(field_name, fieldvalue):
    _command = {"Type": "ChangeAdditionalFields",
                "AdditionalFieldName": "%s"%(field_name),
                "AdditionalFieldUpdateValue": "%s"%(fieldvalue),
                "Operation": "ChangeTo"
                }

def change_comment(comment_id, new_comment):
    _command = {"Type": "ChangeComment",
                "CommentId": "%s"%(comment_id),
                "Comment": "%s"%(new_comment)
                }
    return _command
    
def change_description(description):
    _command = {"Type": "ChangeDescription",
                "Description": "%s"%(description)
                }
    return _command

def change_external_id(externalid):
    _command = {"Type": "ChangeExternalId",
                "ExternalId": "%s"%(externalid)
                }
    return _command

def change_location(entityid, lat, long):
    _command = {"Type": "ChangeLocation",
                "Location": {
                    "EntityId": "%s"%(entityid),
                    "Latitude": lat,
                    "Longitude": long
                }
                }
    return _command

def change_priority(priorityid):
    _command = {"Type": "ChangePriority",
                "PriorityId": "%s"%(priorityid)
                }
    return _command

def change_state(stateid):
    _command = {"Type": "ChangeState",
                "StateId": "%s"%(stateid)
                }
    return _command

def clear_location():
    _command = {"Type": "ClearLocation"}
    return _command

def delete_comment(comment_id):
    _command = {"Type": "DeleteComment",
                "CommentId": "%s"%(comment_id)
                }
    return _command

def detach_entities(entities=["c19de30b-5fc7-44b3-b8d3-1c81ae6fa25b"]):
    _command = {"Type": "DetachEntities",
                "Entities": entities
            }
    return _command

def forward_incident(recipients=["3d1e7eca-ce5b-4d87-b2e4-d597a9e962e5"]):
    _command = {"Type": "ForwardIncident",
                "Recipients": recipients
                }
    return _command

def place_on_hold(delayinseconds):
    _command = {"Type": "PlaceOnHold",
                "DelayInSeconds": int(delayinseconds)
                }
    return _command

def release_ownership():
    _command = {"Type": "ReleaseOwnership"}
    return _command

def take_ownership():
    _command = {"Type": "TakeOwnership"}
    return _command

def transfer_incident(recipients):
    _command = {"Type": "TransferIncident",
                "Recipients": recipients
                }
    return _command

def get_states_incident(user_name, password, ip_addr, port):
    token = create_bearer_token(user_name, password, ip_addr, port)
    headers = create_header('application/json', 'sync', token)
    url = 'https://%s:%s/v2/States'%(ip_addr, port)
    response = requests.get(url, headers=headers, verify=False)
    if response.ok:
        return response.json()['Results']
    else:
        raise Exception("Can't get states of incident!")

def get_priorities(user_name, password, ip_addr, port):
    token = create_bearer_token(user_name, password, ip_addr, port)
    headers = create_header('application/json', 'sync', token)
    url = 'https://%s:%s/v2/States'%(ip_addr, port)
    response = requests.get(url, headers=headers, verify=False)
    if response.ok:
        return response.json()['Results']
    else:
        raise Exception("Can't get priorities of incident!")

def get_incident_type(user_name, password, ip_addr, port):
    token = create_bearer_token(user_name, password, ip_addr, port)
    headers = create_header('application/json', 'sync', token)
    url = 'https://%s:%s/v2/IncidentTypes'%(ip_addr, port)
    response = requests.get(url, headers=headers, verify=False)
    if response.ok:
        return response.json()['Results']
    else:
        raise Exception("Can't get list type of incident!")

def get_procedures(user_name, password, ip_addr, port, current_id, revision=None):
    token = create_bearer_token(user_name, password, ip_addr, port)
    headers = create_header('application/json', 'sync', token)
    if not revision:
        url = 'https://%s:%s/v2/Procedures/%s'%(ip_addr, port, current_id)
        response = requests.get(url, headers=headers, verify=False)
    else:
        url = 'https://%s:%s/v2/Procedures/%s/Revisions/%s'%(ip_addr, port, current_id, revision)
        response = requests.get(url, headers=headers, verify=False)
    if response.ok:
        return response.json()['Results']
    else:
        raise Exception("Can't get procedures of incident!")

def command_incident(user_name, password, ip_addr, port, current_id, command_func, mission=None):
    token = create_bearer_token(user_name, password, ip_addr, port)
    headers = create_header('application/json', 'sync', token)
    if mission:
        assert mission in mission_access, "Name mission isn't available!"
        url = 'https://%s:%s/v2/Incidents/%s/%s'%(ip_addr, port, current_id, mission)
        response = requests.get(url, headers=headers, verify=False)
    else:
        url = 'https://%s:%s/v2/Incidents/%s'%(ip_addr, port, current_id)
        json_data = command_func
        response = requests.post(url, headers=headers, json=json_data, verify=False)
    if response.ok:
        return response.json()
    else:
        raise Exception("Can't run command!")
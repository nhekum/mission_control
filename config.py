list_user_id = {}

list_device_id = {}

dict_incident_type = {"Vi phạm thủ công":'a3c53074-c52f-4f19-a568-9b2c342ea32e',
                      "Vi phạm tự động":'9526315a-860e-4ff5-8340-9929e04ada68',
                      "Ùn tắc tự động":'ce2ee42d-a865-4bc9-86be-aeb7c8b5336a',
                      "Sự kiện khác thủ công":'c7335e81-bec1-49cf-8fc2-7465f5cfc511',
                      "Tai nạn thủ công":'b324dd2c-9356-45d0-af42-0c24a250d440',
                      "Tai nạn tự động":'8c6a43c0-008a-4d11-8d1f-418d3f4ebee8',
                      "Truy vết tự động":'f466685a-4bb4-4c14-b7de-03055207d83d',}

mission_access = ['CurrentProcedureStep', 'AdditionalFields', 'AggregatedEventSourcesIds',
                    'Events', 'LinkedIncidentIds', 'LocationAreaIds', 'ManuallyAttachedEntityIds',
                    'PossibleStateTransitons', 'SourceIds', 'SubIncidentIds', 'ActiveComments']

LIST_FIELDS_VIOLATION = [{'Name': 'Thời gian', 'Value': '', 'DataType': 'String'},
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
                        {'Name': 'Phương pháp phát hiện vi phạm', 'Value': '', 'DataType': 'String'},
                        {'Name': 'Hình thức xử phạt', 'Value': '', 'DataType': 'String'},
                        {'Name': 'Phòng/đơn vị xử lý vi phạm hành chính',
                                 'Value': '',
                                 'DataType': 'String'},
                        {'Name': 'Tên file video', 'Value': '', 'DataType': 'String'},
                        {'Name': 'Thông tin chi tiết', 'Value': '', 'DataType': 'String'},
                        {'Name': 'Cán bộ hiện trường', 'Value': '', 'DataType': 'String'},
                        {'Name': 'Tên file thông tin xử phạt', 'Value': '', 'DataType': 'String'},
                        {'Name': 'Hướng vi phạm', 'Value': '', 'DataType': 'String'}]

LIST_FIELDS_ACCIDENTS = [{'Name': 'Thời gian', 'Value': '', 'DataType': 'String'},
                        {'Name': 'Địa điểm', 'Value': '', 'DataType': 'String'},
                        {'Name': 'Loại phương tiện', 'Value': '', 'DataType': 'String'},
                        {'Name': 'Biển số', 'Value': '', 'DataType': 'String'},
                        {'Name': 'Màu biển số', 'Value': '', 'DataType': 'String'},
                        {'Name': 'Thiết bị giám sát', 'Value': '', 'DataType': 'String'},
                        {'Name': 'Người vận hành thiết bị', 'Value': '', 'DataType': 'String'},
                        {'Name': 'Đơn vị vận hành', 'Value': '', 'DataType': 'String'},
                        {'Name': 'Tên file ảnh biển số', 'Value': '', 'DataType': 'String'},
                        {'Name': 'Tên file ảnh xe', 'Value': '', 'DataType': 'String'},
                        {'Name': 'Mức độ tai nạn', 'Value': '', 'DataType': 'String'},
                        {'Name': 'Tên file video', 'Value': '', 'DataType': 'String'},
                        {'Name': 'Thông tin chi tiết', 'Value': '', 'DataType': 'String'},
                        {'Name': 'Cán bộ hiện trường', 'Value': '', 'DataType': 'String'},]

LIST_FIELDS_HOTLIST = [{'Name': 'Thời gian', 'Value': '', 'DataType': 'String'},
                        {'Name': 'Địa điểm', 'Value': '', 'DataType': 'String'},
                        {'Name': 'Loại phương tiện', 'Value': '', 'DataType': 'String'},
                        {'Name': 'Biển số', 'Value': '', 'DataType': 'String'},
                        {'Name': 'Màu biển số', 'Value': '', 'DataType': 'String'},
                        {'Name': 'Thiết bị giám sát', 'Value': '', 'DataType': 'String'},
                        {'Name': 'Người vận hành thiết bị', 'Value': '', 'DataType': 'String'},
                        {'Name': 'Đơn vị vận hành', 'Value': '', 'DataType': 'String'},
                        {'Name': 'Tên file ảnh biển số', 'Value': '', 'DataType': 'String'},
                        {'Name': 'Tên file ảnh xe', 'Value': '', 'DataType': 'String'},
                        {'Name': 'Tên file video', 'Value': '', 'DataType': 'String'},
                        {'Name': 'Thông tin chi tiết', 'Value': '', 'DataType': 'String'},
                        {'Name': 'Cán bộ hiện trường', 'Value': '', 'DataType': 'String'},]
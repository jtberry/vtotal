
import os
import requests
from pprint import pprint


def lambda_handler(event, context):
    print('## ENVIRONMENT VARIABLES')
    print(os.environ)

    url = 'https://www.virustotal.com/vtapi/v2/file/report'
    api_key = '4939dfcf824fb64580a1cac7400d826bada6264dca09270dcf4c9cf8a2ac0645'

    file = '9f101483662fc071b7c10f81c64bb34491ca4a877191d464ff46fd94c7247115'
    header = {'apikey':api_key, 'resource': file}
    response = requests.get(url ,params=header)
    status = response.status_code
    if status != 200:
        print('Something bad has happened...')
    else:
        pprint(response.json())
        

    print('## EVENT')
    print(event)
# v = virus_total()
# v.scanfile()

# #!/usr/bin/python3

# import requests
# from pprint import pprint

# class virus_total(object):
#     def __init__(self):
#         self.url = 'https://www.virustotal.com/vtapi/v2/file/report'
#         self.api_key = '4939dfcf824fb64580a1cac7400d826bada6264dca09270dcf4c9cf8a2ac0645'

#     def scanfile(self):
#         file = '9f101483662fc071b7c10f81c64bb34491ca4a877191d464ff46fd94c7247115'
#         header = {'apikey':self.api_key, 'resource': file}
#         response = requests.get(self.url ,params=header)
#         status = response.status_code
#         if status != 200:
#             print('Something bad has happened...')
#         else:
#             pprint(response.json())
        


# v = virus_total()
# v.scanfile()
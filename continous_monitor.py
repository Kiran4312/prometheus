import requests
import sys
import os
import jenkins
from redmail import outlook
outlook.user_name = "saikiran.vetapalem@elektrobit.com"
outlook.password = "[Vsssr]@4532#"
# we need to pass jenkins link and credentials(username and API key)
server = jenkins.Jenkins('https://asterix2-jenkins.ebgroup.elektrobit.com',
                         username='SAVE274835', password='11129fafddb18b8b79fdf434163e1fbfb5')
from requests.auth import HTTPBasicAuth
auth = HTTPBasicAuth('save274835', '11129fafddb18b8b79fdf434163e1fbfb5')
#print(node_list)
# server.disable_node("deulmaed2test02", "dummy text")
while True:
    res = requests.get("http://deulmctamonitor01:9090/api/v1/query?query=up" + "", verify=False, auth=auth).json()
    node_list = res['data']['result']
    for i in range(0, len(node_list)):
        instanceName = node_list[i]['metric']['instance']
        instanceStatus = node_list[i]['value'][1]
        if "deulmaed2test" not in instanceName:
            continue
        if instanceStatus != '1':
            print("Status: testbot {} is down please check and fix issue".format(instanceName))
            info = server.get_node_info(instanceName)
            if info['offline']:
                print("Node already disabled in jenkins. No worries....")
            # else:
            #     server.disable_node(instanceName, "lost connection")


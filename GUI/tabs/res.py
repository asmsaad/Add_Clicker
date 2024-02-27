
import json
from tabs.res import *

# tab_details = {
#     "fingerprints": {"Device types": ["Mobile + Desktop", "Desktop", "Mobile"]}
# }





def making_command_log_formate(): 
    DATA_COMMAND = {
        "Main" : "",
        "Proxy" : "",
        # "Visits",
        "Emulation": "",    
        # "Profiles",
        "Fingerprints" : "",
        # "Captcha",
        # "Timeouts",
        # "Timeouts",
        'Utility' : "",
    }

    with open(".command_log.txt","w") as WF:
        WF.write(json.dumps(DATA_COMMAND,indent=4))
    WF.close()

def update_command_log(tab_name,command):
    with open('.command_log.txt', 'r') as RF:
        DATA_COMMAND = json.load(RF)
    RF.close()

    DATA_COMMAND[tab_name] = command

    with open(".command_log.txt","w") as WF:
        WF.write(json.dumps(DATA_COMMAND,indent=4))
    WF.close()



def making_run_command():

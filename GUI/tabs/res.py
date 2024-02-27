
import json
from tabs.res import *
import os

# tab_details = {
#     "fingerprints": {"Device types": ["Mobile + Desktop", "Desktop", "Mobile"]}
# }





def making_command_log_formate(): 
    DATA_COMMAND = {
        "Main" : "",
        "Proxy" : "",
        "Proxy required" : "",
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
    with open('.command_log.txt', 'r') as RF:
        DATA_COMMAND = json.load(RF)
    RF.close()


    
    if DATA_COMMAND["Proxy"].strip() == "":
        DATA_COMMAND["Proxy required"] = ""
    

    run_command = []
    for each_command_unit in DATA_COMMAND:
        run_command.append(DATA_COMMAND[each_command_unit])

    run_command = " ".join(run_command)
    print(run_command)

    print('>>',os.getcwd())
    os.system(run_command)


    return run_command



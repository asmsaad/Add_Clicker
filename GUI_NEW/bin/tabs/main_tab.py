from tkinter import *
from tkinter import filedialog
from tkinter import ttk
from PIL import Image, ImageTk
import os,json
from tabs.res import *

# tab_details = {
#     "fingerprints": {"Device types": ["Mobile + Desktop", "Desktop", "Mobile"]}
# }


a={
    
}


tab_details = {
    "main": {
        "Run in Loop": {"type": "cb", "values": ["Yes","No"], "default": "Yes"},
        # "Mode": {"type": "cb", "values": ["Any sites"], "default": "Any sites"},
        "Keywords" : {"type": "entry","browse":True,"browse_file_type":'',"initial_loc":"./../../"},
        # "Chance of error %" : {"type": "sb", "default": "1" , "from":'0', 'to': '100'},
        # "Number of clicks" : {"type": "sb", "default": "30" , "from":'1', 'to': '100'},
        "Domains that will be ignored" : {"type": "entry","browse":True,"browse_file_type":'',"initial_loc":"./../../"},
        # "Click option": {"type": "cb", "values": ["Google Shope + Context"], "default": "Google Shope + Context"},
        # "Click on the phone number": {"type": "cb", "values": ["Yes", "No"], "default": "No"},
        "Wait between runs (Sec.)" : {"type": "sb", "default": "0", "from":'0', 'to': '1000'},
        "Browser count (Proxy required)" : {"type": "sb", "default": "5", "from":'5', 'to': '20'},
        "Threads (Proxy required)" : {"type": "sb", "default": "1", "from":'1', 'to': '2'}
    }
}


fonts_ = {
    "body": {"tabs": ("Arial", 14, "normal")},
    "cb": ("Arial", 12, "normal"),
}


dimension = {
    "app": {"height": 550, "width": 900},
    # "header": {"height": 20, "width": 0},
    "footer": {"height": 50, "width": 0},
    "body": {
        "height": 550 - 50,
        "width": 150,
        "tabs": {"height": 550 - 50, "width": 150},
        "work": {"height": 550 - 50, "width": 900 - 150},
    },
}

color = {
    "app": {"height": 550, "width": 800},
    # "header": {"height": 20, "width": 0},
    "footer": {"bg": "#313131", "fg": 0},
    "body": {
        "bg": "red",
        "fg": "red",
        "tabs": {
            "bg": "#2c3136",
            "fg": "red",
            "b": {"bg": "#303334", "fg": "#9AACB7", "abg": "#202020", "afg": "#A1C2D6"},
        },
        "work": {"bg": "#202020", "fg": "red"},
    },
}

GUI_SETTINGS = {
    "d": dimension,
    "c": color,
    "f": fonts_,
}




# ,width=dimension['width'],height=dimension['height']
def main_tab(base_frame, dimension):
    
    selected_param_data = {
        "Run in Loop": "Yes",
        "Keywords" : "",
        "Domains that will be ignored" : "",
        "Wait between runs (Sec.)" : "0",
        "Browser count (Proxy required)": "5",
        "Threads (Proxy required)" : "1"
        
    }
    
    
    fingerprints_tab_frame = Canvas(
        base_frame,
        background=GUI_SETTINGS["c"]["body"]["work"]["bg"],
        border=0,
        borderwidth=0,
        highlightthickness=0,
    )
    fingerprints_tab_frame.place(x=0, y=0)

    Label(
        fingerprints_tab_frame,
        background=GUI_SETTINGS["c"]["body"]["work"]["bg"],
        padx=346,
        border=0,
        borderwidth=0,
        highlightthickness=0,
    ).grid(row=0, column=1)
    # Label(fingerprints_tab_frame, background="red", padx=342).grid(row=1, column=0, rowsp)

    main_tab_widgets = {}

    main_tab_widgets["cb_frame"] = Frame(
        fingerprints_tab_frame,
        background=GUI_SETTINGS["c"]["body"]["work"]["bg"],
        border=0,
        borderwidth=0,
        highlightthickness=0,
    )
    main_tab_widgets["cb_frame"].grid(row=1, column=1)
    
    
    
    def open_file_dialog(entry_widget,data_name):
        initial_dir = "./../../"
        file_types = [("Text Files", "*.txt"), ("All Files", "*.*")]  # Specify file types
        file_path = filedialog.askopenfilename(initialdir=initial_dir, title="Select File", filetypes=file_types)
        # print("Selected file:", file_path)
        
        entry_widget.delete(0, "end")  # Clear any existing value
        entry_widget.insert(0, file_path)  # Insert the default value
        
        #Update Data
        widget_selected_value(entry_widget,data_name)
    
    
    
    def proxy_enable_disable(selected_data):
        
        selected_param_data["Use proxy"] = selected_data
        
        #Store Instruction on Every Changes
        store_instruction()
        
        if selected_data == 'Yes':
            for index, each_options in enumerate(tab_details["main"].keys()):
                if index != 0:
                    main_tab_widgets[each_options + "_label_placeholder"].grid(row=index, column=1, ipady=5)
                    main_tab_widgets[each_options + "_label"].grid(row=index, column=1, sticky="e", ipadx=10)
                     # ComboBox
                    if tab_details["main"][each_options]["type"] == "cb":
                        # Default Value
                        main_tab_widgets[each_options + "_cb"].set(tab_details["main"][each_options]["default"])
                        # Placement
                        main_tab_widgets[each_options + "_cb"].grid(row=index, column=2, ipadx=0)
                    
                    #SpinBox 
                    elif tab_details["main"][each_options]["type"] == "sb":
                        # Default Value
                        main_tab_widgets[each_options + "_sb"]["state"] = NORMAL
                        main_tab_widgets[each_options + "_sb"].delete( 0, "end")  # Clear any existing value
                        main_tab_widgets[each_options + "_sb"].insert(0, int(tab_details["main"][each_options]["default"]))  # Insert the default value
                        main_tab_widgets[each_options + "_sb"]["state"] = "readonly"
                        # Placement
                        main_tab_widgets[each_options + "_sb"].grid(row=index, column=2, ipadx=3)
                        
                    #Entry
                    elif tab_details["main"][each_options]["type"] == "entry":   
                        # Default Value
                        main_tab_widgets[each_options+"_entry"].delete(0, "end")  # Clear any existing value
                        main_tab_widgets[each_options + "_entry"].grid(row=index, column=2, ipadx=0, sticky=W)
                        #Browse 
                        if  tab_details["main"][each_options]['browse'] == True:
                            main_tab_widgets[each_options + "_entry_browse_btn"].grid(row=index, column=2, ipadx=0, sticky=E )
                            
                        
        elif selected_data == 'No':
            for index, each_options in enumerate(tab_details["main"].keys()):
                if index != 0:
                    main_tab_widgets[each_options + "_label_placeholder"].grid_forget()
                    main_tab_widgets[each_options + "_label"].grid_forget()
                     # ComboBox
                    if tab_details["main"][each_options]["type"] == "cb":
                        # Placement
                        main_tab_widgets[each_options + "_cb"].grid_forget()
                    
                    #SpinBox 
                    elif tab_details["main"][each_options]["type"] == "sb":
                        # Placement
                        main_tab_widgets[each_options + "_sb"].grid_forget()
                        
                    #Entry
                    elif tab_details["main"][each_options]["type"] == "entry":   
                        # Default Value
                        main_tab_widgets[each_options + "_entry"].grid_forget()
                        #Browse 
                        if  tab_details["main"][each_options]['browse'] == True:
                            main_tab_widgets[each_options + "_entry_browse_btn"].grid_forget()
                            
    def run_in_Loop_EL(e,selected_data):
        selected_data = selected_data.get()
        if selected_data == 'Yes' :
            pass
        else:
            pass
        
        
        
       
    def widget_selected_value(selected_data,data_name):
        selected_data = selected_data.get()
        selected_param_data[data_name] = selected_data       
        # print(data_name,selected_data)
        
        #Store Instruction on Every Changes
        store_instruction()
    
     
    def widget_selected_value_EL(e,selected_data,data_name):
        widget_selected_value(selected_data,data_name)
        
        
        
    def making_instruction(): 
        # selected_param_data = {
        #     "Run in Loop": "No",
        #     "Keywords" : "",
        #     "Domains that will be ignored" : "",
        #     "Browser count (Proxy required)": "5",
        #     "Threads (Proxy required)" : "1"
        # }

        
        command_text = {
            "file_name" : "",
            "query" : "",
            "excludes_text" : "",
            # "browser_count" : "",
            # "Threads (Proxy required)" : "",
            "Wait between runs (Sec.)" : "0"
        }

        command_text2 = {
            "browser_count" : "",
            "Threads (Proxy required)" : "",
        }

        


        #Loop ? / !
        if selected_param_data["Run in Loop"] == "No":
            command_text["file_name"] = "python ad_clicker.py"
        else:
            command_text["file_name"] = "python run_in_loop.py"

        # Search Query
        if os.path.isfile(str(selected_param_data["Keywords"]).strip()):
            command_text["query"] = f"-qf {str(selected_param_data['Keywords']).strip()}"
        else:
            command_text["query"] = '-q "'+ str(selected_param_data['Keywords']).strip() + '"'

        # Browser Count
        command_text2["browser_count"] = f'-bc {str(selected_param_data["Browser count (Proxy required)"]).strip()}'

        # Multiprocess style
        command_text2["Threads (Proxy required)"] = f"-ms {str(selected_param_data['Threads (Proxy required)']).strip()}"

        # Exclude Word
        if os.path.isfile(str(selected_param_data["Domains that will be ignored"]).strip()):
            with open(str(selected_param_data["Domains that will be ignored"]).strip() , 'r') as RF:
                exclude_word = RF.read()
            RF.close()
            exclude_word = exclude_word.replace('\n'," ")
            command_text["excludes_text"] = f'-e "{exclude_word}"'
        elif str(selected_param_data["Domains that will be ignored"]).strip() == "":
            command_text["excludes_text"] = ""
        else:
            command_text["excludes_text"] = f'-e "' + str(selected_param_data['Domains that will be ignored']).strip() + '"'

        # Wait between runs (Sec.) 
        if str(selected_param_data["Wait between runs (Sec.)"]).strip() == "0":
            command_text["Wait between runs (Sec.)"] = ""
        else:
            command_text["Wait between runs (Sec.)"] = "-wt "+ str(selected_param_data["Wait between runs (Sec.)"]).strip()



        generated_command = []
        for each_command in command_text:
            generated_command.append(command_text[each_command])

        generated_command2 = []
        for each_command in command_text2:
            generated_command2.append(command_text2[each_command])
        

        # print(" ".join(generated_command))
        # print(" ".join(generated_command2))


        # return " ".join(generated_command)
        generated_command1_and_2 = {
        "Main" : " ".join(generated_command),
        "Proxy required" : " ".join(generated_command2),
        }
        
        return generated_command1_and_2
        
                
            
                
                
    def store_instruction():
        # print(json.dumps(selected_param_data, indent=4))  
        # print('>>> ',making_instruction(), '<<<')
        # update_command_log("Main",making_instruction())
        command = making_instruction()
        update_command_log("Main",command["Main"])
        update_command_log("Proxy required",command["Proxy required"])
        # print(command)
                      
                        
                    
            
        
    

    for index, each_options in enumerate(tab_details["main"].keys()):
        # PlaceHolder Label
        main_tab_widgets[each_options + "_label_placeholder"] = Label(
            main_tab_widgets["cb_frame"],
            width=28,
            # background="green",
            background=GUI_SETTINGS["c"]["body"]["work"]["bg"],
            border=0,
            borderwidth=0,
            highlightthickness=0,
            font=fonts_["cb"],
        )
        main_tab_widgets[each_options + "_label_placeholder"].grid(
            row=index, column=1, ipady=5
        )

        # Label
        main_tab_widgets[each_options + "_label"] = Label(
            main_tab_widgets["cb_frame"],
            font=fonts_["cb"],
            text=each_options,
            background=GUI_SETTINGS["c"]["body"]["work"]["bg"],
            border=0,
            borderwidth=0,
            highlightthickness=0,
            foreground="white",
        )
        main_tab_widgets[each_options + "_label"].grid(
            row=index, column=1, sticky="e", ipadx=10
        )

        # ComboBox
        if tab_details["main"][each_options]["type"] == "cb":
            main_tab_widgets[each_options + "_cb"] = ttk.Combobox(
                main_tab_widgets["cb_frame"],
                width=35,
                values=tab_details["main"][each_options]["values"],
                font=fonts_["cb"],
                state="readonly",
                background=GUI_SETTINGS["c"]["body"]["work"]["bg"],
            )
            # Default Value
            main_tab_widgets[each_options + "_cb"].set(
                tab_details["main"][each_options]["default"]
            )
            # Placement
            main_tab_widgets[each_options + "_cb"].grid(row=index, column=2, ipadx=0)

            # # Actions
            # if each_options == "Run in Loop":
            #     main_tab_widgets[each_options+"_cb"].bind("<<ComboboxSelected>>", lambda e , selected_data = main_tab_widgets[each_options + "_cb"] : run_in_Loop_EL(e,selected_data))
            # else:
            main_tab_widgets[each_options+"_cb"].bind("<<ComboboxSelected>>", lambda e , selected_data = main_tab_widgets[each_options + "_cb"], data_name=each_options :widget_selected_value_EL(e,selected_data,data_name))

        #SpinBox
        elif tab_details["main"][each_options]["type"] == "sb":
            main_tab_widgets[each_options + "_sb"] = Spinbox(
                main_tab_widgets["cb_frame"],
                width=35,
                font=fonts_["cb"],
                from_=tab_details["main"][each_options]["from"],
                to=tab_details["main"][each_options]["to"],
            )
            # Default Value
            main_tab_widgets[each_options + "_sb"].delete( 0, "end")  # Clear any existing value
            main_tab_widgets[each_options + "_sb"].insert(0, int(tab_details["main"][each_options]["default"]))  # Insert the default value
            main_tab_widgets[each_options + "_sb"]["state"] = "readonly"
            # Placement
            main_tab_widgets[each_options + "_sb"].grid(row=index, column=2, ipadx=3)

            # Actions
            main_tab_widgets[each_options+"_sb"]["command"] = lambda  selected_data = main_tab_widgets[each_options+"_sb"] , data_name=each_options : widget_selected_value(selected_data,data_name)

        #EntryBox
        elif tab_details["main"][each_options]["type"] == "entry":
            main_tab_widgets[each_options + "_entry"] = Entry( main_tab_widgets["cb_frame"], width=34, font=fonts_["cb"],)
            # Default Value
            main_tab_widgets[each_options+"_entry"].delete(0, "end")  # Clear any existing value
            # Placement
            main_tab_widgets[each_options + "_entry"].grid(row=index, column=2, ipadx=0, sticky=W)
            # Actions
            main_tab_widgets[each_options + "_entry"].bind("<KeyRelease>", lambda e , selected_data = main_tab_widgets[each_options + "_entry"] , data_name=each_options :widget_selected_value_EL(e,selected_data,data_name))
            
            
            if  tab_details["main"][each_options]['browse'] == True:
                text_img = Image.open("res/list.png")
                text_img = text_img.resize((24, 24), Image.LANCZOS)
                text_img = ImageTk.PhotoImage(text_img)

                main_tab_widgets[each_options + "_entry_browse_btn"] = Button(
                    main_tab_widgets["cb_frame"],
                    text="Hi",
                    image= text_img,
                    background=GUI_SETTINGS["c"]["body"]["work"]["bg"],
                    activebackground=GUI_SETTINGS["c"]["body"]["work"]["bg"],
                    border=0,
                    borderwidth=0,
                    highlightthickness=0,
                )
                main_tab_widgets[each_options + "_entry_browse_btn"].image = text_img
                main_tab_widgets[each_options + "_entry_browse_btn"].grid(row=index, column=2, ipadx=0, sticky=E)
                
                # Actions
                main_tab_widgets[each_options + "_entry_browse_btn"]['command'] = lambda entry_widget = main_tab_widgets[each_options + "_entry"] , data_name = each_options : open_file_dialog(entry_widget,data_name)

                
    
    
    
    #Default Selection
    # proxy_enable_disable("No")
    #Default Instruction
    store_instruction()
    
    



if __name__ == "__main__":
    root = Tk()
    main_tab(root)

    root.mainloop()

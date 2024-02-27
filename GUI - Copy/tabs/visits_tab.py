from tkinter import *
from tkinter import filedialog
from tkinter import ttk
from PIL import Image, ImageTk
import os,json

# tab_details = {
#     "fingerprints": {"Device types": ["Mobile + Desktop", "Desktop", "Mobile"]}
# }


a={
    
    "Depth of view              Minimum Value" : {"type": "sb", "default": "1" , "from":'0', 'to': '100'},
    "Depth of view              Maximum Value" : {"type": "sb", "default": "3" , "from":'0', 'to': '100'},
    
    "Page view time (sec)       Minimum Value" : {"type": "sb", "default": "10" , "from":'0', 'to': '100'},
    "Page view time (sec)       Maximum Value" : {"type": "sb", "default": "30" , "from":'0', 'to': '100'},
    
}


tab_details = {
    "visits_tab": {
        "Depth of view              Minimum Value" : {"type": "sb", "default": "1" , "from":'0', 'to': '100'},
        "Depth of view              Maximum Value" : {"type": "sb", "default": "3" , "from":'0', 'to': '100'},
        
        "Page view time (sec)       Minimum Value" : {"type": "sb", "default": "10" , "from":'0', 'to': '100'},
        "Page view time (sec)       Maximum Value" : {"type": "sb", "default": "30" , "from":'0', 'to': '100'},
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
def visits_tab(base_frame, dimension):
    
    selected_param_data = {
        "Depth of view              Minimum Value" : "1",
        "Depth of view              Maximum Value" : "3",

        "Page view time (sec)       Minimum Value" : "10",
        "Page view time (sec)       Maximum Value" : "30",
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

    visits_tab_widgets = {}

    visits_tab_widgets["cb_frame"] = Frame(
        fingerprints_tab_frame,
        background=GUI_SETTINGS["c"]["body"]["work"]["bg"],
        border=0,
        borderwidth=0,
        highlightthickness=0,
    )
    visits_tab_widgets["cb_frame"].grid(row=1, column=1)
    
    
    
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
            for index, each_options in enumerate(tab_details["visits_tab"].keys()):
                if index != 0:
                    visits_tab_widgets[each_options + "_label_placeholder"].grid(row=index, column=1, ipady=5)
                    visits_tab_widgets[each_options + "_label"].grid(row=index, column=1, sticky="e", ipadx=10)
                     # ComboBox
                    if tab_details["visits_tab"][each_options]["type"] == "cb":
                        # Default Value
                        visits_tab_widgets[each_options + "_cb"].set(tab_details["visits_tab"][each_options]["default"])
                        # Placement
                        visits_tab_widgets[each_options + "_cb"].grid(row=index, column=2, ipadx=0)
                    
                    #SpinBox 
                    elif tab_details["visits_tab"][each_options]["type"] == "sb":
                        # Default Value
                        visits_tab_widgets[each_options + "_sb"]["state"] = NORMAL
                        visits_tab_widgets[each_options + "_sb"].delete( 0, "end")  # Clear any existing value
                        visits_tab_widgets[each_options + "_sb"].insert(0, int(tab_details["visits_tab"][each_options]["default"]))  # Insert the default value
                        visits_tab_widgets[each_options + "_sb"]["state"] = "readonly"
                        # Placement
                        visits_tab_widgets[each_options + "_sb"].grid(row=index, column=2, ipadx=3)
                        
                    #Entry
                    elif tab_details["visits_tab"][each_options]["type"] == "entry":   
                        # Default Value
                        visits_tab_widgets[each_options+"_entry"].delete(0, "end")  # Clear any existing value
                        visits_tab_widgets[each_options + "_entry"].grid(row=index, column=2, ipadx=0, sticky=W)
                        #Browse 
                        if  tab_details["visits_tab"][each_options]['browse'] == True:
                            visits_tab_widgets[each_options + "_entry_browse_btn"].grid(row=index, column=2, ipadx=0, sticky=E )
                            
                        
        elif selected_data == 'No':
            for index, each_options in enumerate(tab_details["visits_tab"].keys()):
                if index != 0:
                    visits_tab_widgets[each_options + "_label_placeholder"].grid_forget()
                    visits_tab_widgets[each_options + "_label"].grid_forget()
                     # ComboBox
                    if tab_details["visits_tab"][each_options]["type"] == "cb":
                        # Placement
                        visits_tab_widgets[each_options + "_cb"].grid_forget()
                    
                    #SpinBox 
                    elif tab_details["visits_tab"][each_options]["type"] == "sb":
                        # Placement
                        visits_tab_widgets[each_options + "_sb"].grid_forget()
                        
                    #Entry
                    elif tab_details["visits_tab"][each_options]["type"] == "entry":   
                        # Default Value
                        visits_tab_widgets[each_options + "_entry"].grid_forget()
                        #Browse 
                        if  tab_details["visits_tab"][each_options]['browse'] == True:
                            visits_tab_widgets[each_options + "_entry_browse_btn"].grid_forget()
                            
    def proxy_enable_disable_EL(e,selected_data):
        selected_data = selected_data.get()
        proxy_enable_disable(selected_data)  
        
        
        
       
    def widget_selected_value(selected_data,data_name):
        selected_data = selected_data.get()
        selected_param_data[data_name] = selected_data       
        # print(data_name,selected_data)
        
        #Store Instruction on Every Changes
        store_instruction()
    
     
    def widget_selected_value_EL(e,selected_data,data_name):
        widget_selected_value(selected_data,data_name)
        
        
        
    def making_instruction(): 
        return ""
        
        if selected_param_data["Use proxy"] == "No":
            return ""
        else: 
            if selected_param_data["Proxy format"] == "host:port":
                if os.path.isfile(str(selected_param_data["Proxy"]).strip()):
                    return f"-pf {str(selected_param_data['Proxy']).strip()}"
                elif str(selected_param_data["Proxy"]).strip() == "":
                    return ""
                else:
                    return f"-p {str(selected_param_data['Proxy']).strip()}"
                    
            elif selected_param_data["Proxy format"] == "username:password@host:port":
                if os.path.isfile(str(selected_param_data["Proxy"]).strip()):
                    return f"--auth -pf {str(selected_param_data['Proxy']).strip()}"
                elif str(selected_param_data["Proxy"]).strip() == "":
                    return ""
                else:
                    return f"--auth -p {str(selected_param_data['Proxy']).strip()}"
                
            
                
                
    def store_instruction():
        print(json.dumps(selected_param_data, indent=4))  
        print('>>> ',making_instruction(), '<<<')
                      
                        
                    
            
        
    

    for index, each_options in enumerate(tab_details["visits_tab"].keys()):
        # PlaceHolder Label
        visits_tab_widgets[each_options + "_label_placeholder"] = Label(
            visits_tab_widgets["cb_frame"],
            width=28,
            # background="green",
            background=GUI_SETTINGS["c"]["body"]["work"]["bg"],
            border=0,
            borderwidth=0,
            highlightthickness=0,
            font=fonts_["cb"],
        )
        visits_tab_widgets[each_options + "_label_placeholder"].grid(
            row=index, column=1, ipady=5
        )

        # Label
        visits_tab_widgets[each_options + "_label"] = Label(
            visits_tab_widgets["cb_frame"],
            font=fonts_["cb"],
            text=each_options,
            background=GUI_SETTINGS["c"]["body"]["work"]["bg"],
            border=0,
            borderwidth=0,
            highlightthickness=0,
            foreground="white",
        )
        visits_tab_widgets[each_options + "_label"].grid(
            row=index, column=1, sticky="e", ipadx=10
        )

        # ComboBox
        if tab_details["visits_tab"][each_options]["type"] == "cb":
            visits_tab_widgets[each_options + "_cb"] = ttk.Combobox(
                visits_tab_widgets["cb_frame"],
                width=35,
                values=tab_details["visits_tab"][each_options]["values"],
                font=fonts_["cb"],
                state="readonly",
                background=GUI_SETTINGS["c"]["body"]["work"]["bg"],
            )
            # Default Value
            visits_tab_widgets[each_options + "_cb"].set(
                tab_details["visits_tab"][each_options]["default"]
            )
            # Placement
            visits_tab_widgets[each_options + "_cb"].grid(row=index, column=2, ipadx=0)

            # Actions
            # if each_options == 'Use proxy':
            #     # visits_tab_widgets[each_options+"_cb"].bind("<<ComboboxSelected>>", lambda e , selected_data = visits_tab_widgets[each_options + "_cb"] :proxy_enable_disable_EL(e,selected_data))
            # else:
            visits_tab_widgets[each_options+"_cb"].bind("<<ComboboxSelected>>", lambda e , selected_data = visits_tab_widgets[each_options + "_cb"], data_name=each_options :widget_selected_value_EL(e,selected_data,data_name))

        #SpinBox
        elif tab_details["visits_tab"][each_options]["type"] == "sb":
            visits_tab_widgets[each_options + "_sb"] = Spinbox(
                visits_tab_widgets["cb_frame"],
                width=35,
                font=fonts_["cb"],
                from_=0,
                to=100,
            )
            # Default Value
            visits_tab_widgets[each_options + "_sb"].delete(
                0, "end"
            )  # Clear any existing value
            visits_tab_widgets[each_options + "_sb"].insert(
                0, int(tab_details["visits_tab"][each_options]["default"])
            )  # Insert the default value
            visits_tab_widgets[each_options + "_sb"]["state"] = "readonly"
            # Placement
            visits_tab_widgets[each_options + "_sb"].grid(row=index, column=2, ipadx=3)

            # Actions
            visits_tab_widgets[each_options+"_sb"]["command"] = lambda  selected_data = visits_tab_widgets[each_options+"_sb"] , data_name=each_options : widget_selected_value(selected_data,data_name)

        #EntryBox
        elif tab_details["visits_tab"][each_options]["type"] == "entry":
            visits_tab_widgets[each_options + "_entry"] = Entry( visits_tab_widgets["cb_frame"], width=34, font=fonts_["cb"],)
            # Default Value
            visits_tab_widgets[each_options+"_entry"].delete(0, "end")  # Clear any existing value
            # Placement
            visits_tab_widgets[each_options + "_entry"].grid(row=index, column=2, ipadx=0, sticky=W)
            # Actions
            visits_tab_widgets[each_options + "_entry"].bind("<KeyRelease>", lambda e , selected_data = visits_tab_widgets[each_options + "_entry"] , data_name=each_options :widget_selected_value_EL(e,selected_data,data_name))
            
            
            if  tab_details["visits_tab"][each_options]['browse'] == True:
                text_img = Image.open("res/list.png")
                text_img = text_img.resize((24, 24), Image.LANCZOS)
                text_img = ImageTk.PhotoImage(text_img)

                visits_tab_widgets[each_options + "_entry_browse_btn"] = Button(
                    visits_tab_widgets["cb_frame"],
                    text="Hi",
                    image= text_img,
                    background=GUI_SETTINGS["c"]["body"]["work"]["bg"],
                    activebackground=GUI_SETTINGS["c"]["body"]["work"]["bg"],
                    border=0,
                    borderwidth=0,
                    highlightthickness=0,
                )
                visits_tab_widgets[each_options + "_entry_browse_btn"].image = text_img
                visits_tab_widgets[each_options + "_entry_browse_btn"].grid(row=index, column=2, ipadx=0, sticky=E)
                
                # Actions
                visits_tab_widgets[each_options + "_entry_browse_btn"]['command'] = lambda entry_widget = visits_tab_widgets[each_options + "_entry"] , data_name = each_options : open_file_dialog(entry_widget,data_name)

                
    
    
    
    #Default Selection
    # proxy_enable_disable("No")
    #Default Instruction
    store_instruction()
    
    



if __name__ == "__main__":
    root = Tk()
    visits_tab(root)

    root.mainloop()
